import matplotlib.pyplot as plt



'''This module contain cool functions that i wrote for End of course project. ex: 'draw3Cicrcles' using matplotlib class,'printNumsWithSum', 'drawFace'. '''

'''
The Function Draw3Circles: Receives 3 radius and draws 3 circles according to them.

The function performs a check according to compare the size of the circles:

The smallest circle will be in the center in red with a thick line.

The middle circle will also be in the center around the small circle, it will be yellow, and with a medium line.

The large circle will also be in the center around the middle circle, it will be blue, and with a thin line.
recomended: 'Draw3Circles(10,30,20)'
'''
def Draw3Circles(n1,n2,n3):
    
        arr = [n1,n2,n3]#storing the 3 radius inside an array
        r1 = max(arr) # biggest circle
        arr.remove(max(arr))
        r3 = min(arr) # smallest circle
        arr.remove(min(arr))
        r2 = arr[0] # medium circle

        
        figure, axes = plt.subplots()
        #storing the 3 circles inside veriable
        Drawing_colored_circle1 = plt.Circle((50, 50), radius=r1, fill=False, linewidth=1, color="blue") # biggest circle
        Drawing_colored_circle2 = plt.Circle((50, 50), radius=r2, fill=False, linewidth=3, color="yellow") # medium circle
        Drawing_colored_circle3 = plt.Circle((50, 50), radius=r3, fill=False, linewidth=5, color="red") # smallest circle
    
        # axes define the Graphic table scales:
        axes.set_aspect(1)
        axes.set_xlim(0, 100)
        axes.set_ylim(0, 100)
        #ploting the 3 circles
        axes.add_artist(Drawing_colored_circle1)
        axes.add_artist(Drawing_colored_circle2)
        axes.add_artist(Drawing_colored_circle3)
        plt.title('Circles')
        plt.show()

'''The Function: 'findSumOfNumber' used to sum the digit of a given number. ex: findSumOfNumber(100) will return: 1, findSumOfNumber(105) will return: 6'''
# important note: use only on int positive numbers.
def findSumOfNumber(n):
     
    sum = 0
    for num in str(n):  
      sum += int(num)       
    return sum

'''The Function:'PrintNumsWithSum' takes two numbers and prints on the screen all the small numbers from n whose sum of digits is exactly equal to m. the function use- 'findSumOfNumber' function.'''
def PrintNumsWithSum(n,m):
	i = m # i takes the value of m
	arr= []
	for i in range(n):
		if findSumOfNumber(i) == m:
			arr.append(i) # storing all the results in array arr
	
	i = 0 # Reset i
	while i < (len(arr)-1):
	    print(arr[i], end=", ") #printing  with an ', ' after it exept for the last value in the array
	    i += 1 
	
	print(arr[i], end=" ") # print the last value in array. will look like this: ' 1, 2, 3 ' instead of: ' 1, 2, 3, '


'''The Function: 'drawFace' - This function draws a face screen where the radius of the left eye is eye1, the radius of the right eye is eye2, the mouth is mouth length and the nose is nose.
Clarifications: The eyes are circles, the mouth is a line while the nose is a rectangle. '''
'''recomended: 'DrawFace(10,10,20, 60)' '''
def DrawFace(eye1,eye2, mouth, nose):

	arr = [eye1,eye2,mouth,nose]
	r1 = arr[0] # eye1
	r2 = arr[1] # eye2
	l1 = arr[2] # line mouth start
	l2 = 4*l1 # line mouth end
	rec1= arr[3] # rectangle nose width
	rec2= rec1/2 # rectangle nose height
	

	figure, axes = plt.subplots()
	Drawing_colored_circle1 = plt.Circle((70, 80), radius=r1, fill="blue", linewidth=5, color="blue") # eye1
	Drawing_colored_circle2 = plt.Circle((30, 80), radius=r2, fill="blue", linewidth=5, color="blue") # eye2
	Drawing_colored_line1 = axes.hlines(y=20, xmin=l1, xmax=l2, linewidth=5, color='r') # mouth
	Drawing_colored_rectongle1 = plt.Rectangle((20, 30), rec1, rec2, fill=False, linewidth=5, color="black") # nose

        # axes define the Graphic table scales:
	axes.set_aspect(1)
	axes.set_xlim(0, 100)
	axes.set_ylim(0, 100)
	axes.add_artist(Drawing_colored_circle1) # eye1
	axes.add_artist(Drawing_colored_circle2) # eye2
	axes.add_artist(Drawing_colored_line1)   # mouth
	axes.add_artist(Drawing_colored_rectongle1) # nose
	plt.title('Face')

	plt.show()

