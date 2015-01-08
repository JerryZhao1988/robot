CONTENTS OF THIS FILE
---------------------
* Introduction
* Starting the app
* Testing


 Introduction
 ------------
 This app use a star algorithm to search the shorest path in matrix
 When user set the start point and end point, it would find the path
 or no path is aviliable.


 Starting the app
 ----------------
 A hex matrix should be give for running.
 The default start point is (0,0), end point (5,5)

 App should be running by:
 python robot.py [file path] + [option]

 $ python robot.py test1
 ['r', 'r', 'd', 'd', 'r', 'd', 'd', 'r', 'r', 'd']

 $ python robot.py test1 1 1 4 4
 ['d', 'r', 'r', 'd', 'd', 'r']

 (1,1) is startpoint (4,4) is endpoint


 Testing
 -------

 test.py do unittest



