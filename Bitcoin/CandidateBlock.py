
from queue import Queue
from dataclasses import dataclass
import dataclasses as dc
from typing import List

import miner
from Block import Block
from exceptions import TransactionException
from miner import Miner
from Message import Message
import rsa

from random import random


# def make_nonce():
#     nonce = str(random.randint(1000, 10000))  # a random 4 digit number to send to the miner
#     return nonce


@dataclass
class CandidateBlock:
    minerAddress:rsa.PublicKey
    final_transactions: List[Message]
    blockchain: List[Block] #block_chain
    temp_queue: Queue
    prev_block_hash: str
    index: int
    nonce:str = '0000' #this var is the riddle \ תעלומה

    def get_prev_block_hash(self):
        self.prev_block_hash = self.blockchain[:-1].current_block_hash
        return self.prev_block_hash

    def get_index(self):
        self.index = self.blockchain[:-1].index + 1
        return self.index

    def check_and_update_amount(tokens, sender_addr)->bool:
        sender = Miner.get_miner_by_key(Miner.users,sender_addr)
        return sender.update_sender_balance(tokens)


    def check_amount(tokens, sender_addr)->bool: # double spending not resolved!
        sender:Miner = Miner.get_miner_by_key(Miner.users,sender_addr)
        if (sender.amount - tokens) >= 0:
            return True
        return False

    def create_new_block_to_list(self): # func 2
        """
        checks the user's resources so that there is no double spending problem.
        :return:
        list of all checked transactions.
        """
        self.get_index() # initialize the index of the candidate block
        self.get_prev_block_hash() # initialize the prev_block_hash of the candidate block
        block_nonce = self.nonce

        winner_miner: Miner = miner.get_miner_by_key(miner.users, self.minerAddress)  # will gives us the current miner from the list


        while not self.temp_queue.empty():
            transaction:Message = self.temp_queue.get()


            winner_miner.find_nonce_hash(block_nonce, self.index,transaction.message_signature, self.prev_block_hash)  # compute the nonce (we can save the result that return from: find_hash_nonce() )


            # miner found the nonce hash and than can add the transaction to  the final block.
            # update accounts
            sender_miner: Miner = miner.get_miner_by_key(miner.users,transaction.sender_addr)  # find the receiver user in each transaction
            receiver_miner: Miner = miner.get_miner_by_key(miner.users,transaction.receiver_addr)  # find the receiver user in each transaction
            have_money = self.check_and_update_amount(transaction.amount,sender_miner)

            if have_money: # if sender has enough money, and we successfully updated sender amount -> prevent double spending
                receiver_miner.update_receiver_balance(transaction.amount)  # update receiver amount
                self.final_transactions.append(transaction)

        # create new block and at the right place
        if len(self.blockchain) == 0:
            new_block = Block(" ", 0, self.final_transactions)
        else:
            new_block = Block(self.blockchain[-1].current_block_hash, self.blockchain[-1].index + 1, self.final_transactions)

        new_block.current_block_hash = new_block.compute_block_hash()

        # create new block and add the final transactions
        # new_block = Block(self.blockchain[-1].current_block_hash, self.blockchain[-1].index + 1, self.final_transactions)
        self.blockchain.append(new_block)  # add the block to the block chain
        winner_miner.update_receiver_balance(Block.TOKEN_PRIZE)  # reward to miner

        return new_block


    def add_transaction_to_queue(self,new_transaction:Message): # func 3
        """
        This method receives a new transaction. She will perform two validations -
        one for security and one for the money in the transaction to transfer.
        """
        result_verify = Message.verify_message(new_transaction) # check integrity of Message (transaction)
        if isinstance(result_verify,TransactionException):
            return False
        # check amount in sender account.  and update it! -> to prevent double spending situation

        have_money = self.check_amount(new_transaction.amount,new_transaction.sender_addr)
        if have_money:
            self.temp_queue._put(new_transaction)
            return True
        return False



