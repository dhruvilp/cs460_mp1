# cs460_mp1

## Problem 1 [50 points] 
Multilateration in 3D. You are to implement the function named multilaterate(distances) in the provided template python code in the file `multilaterate.py`. The function multilaterate(distances) takes a list of lists as its input. The list should have four landmark locations with associated (x, y, z, d) in formation in which x, y, z are the location of the landmark in 3D and d is the distance of the landmark to the unknown point to be localized. You should test your program to ensure it works with different input points correctly. Your program will
be tested on several different setups and should provide reasonable output (i.e. for each coordinate of (x, y, z), either the absolute or relative error is less than 10−6). multilaterate.py takes a single argument: the datafile name. Your program should then print out the location that is computed.
A skeleton multilaterate.py is provided.

For your submission, besides the implementation, you need to provide a PDF file placed in the
same folder to explain your implementation, i.e., how do you compute the location. This does not
need to too mathematical, i.e., you can use mostly verbal descriptions to explain the main ideas
behind your computation.

## Problem 2 [50 points]. 
Implementation of a 2D Kalman filter. Suppose that there is a point mass moving in 2D with the system equation being...

For your solution, you should provide
1. The Kalman filter update equations for this system (in a .pdf file). Put this file under the same folder as the other files for this problem.
2. A python file named kalman2d.py that you need to implement to process the given data (a skeleton file is provided). The python program takes four additional arguments. The first argument is the data file name. The second and third arguments are ˆx1,0 and ˆx2,0, respectively. The last argument is a value λ that will be used to compute P0 as P0 = λI in which I is the identity matrix. After getting the predicted (x1,k, x2,k) values, plot them using matplotlib as a set of 2D points and connect them sequentially using line segments. Do the same in the same plot to the observations (i.e., (z1,k, z2,k)) using a different color.
