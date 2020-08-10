# kulina-test
Applicant`s name : Steven

Python version used : Python 3

# Files
There are 3 files in this repository. Each of them is named with the number in the question.

## Question No.1 (the answer is in file no1.py)
Nick works at a clothing store. He has a large pile of socks that he must pair by color for
sale. Given an array of integers representing the color of each sock, determine how many
pairs of socks with matching colors there are.
For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2]. There is one pair of
color 1 and one of color 2. There are three odd socks left, one of each color. The number of
pairs is 2.
Function Description
Complete the sock merchant function in the editor below. It must return an integer
representing the number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
● n : the number of socks in the pile
● ar : the colors of each sock
Input Format
The first line contains an integer n , the number of socks represented in ar .
The second line contains n space-separated integers describing the colors ar [ i ] of the
socks in the pile.
Constraints
1 ≤ n ≤ 100
1 ≤ ar [ i ] ≤ 100 where 0 ≤ i < n

## Question No.2 (the answer is in file no2.py)
Bill is an avid hiker. He tracks his hikes meticulously, paying close attention to small details
like topography. During his last hike he took exactly n steps. For every step he took, he
noted if it was an uphill, U , or a downhill, D step. Gary's hikes start and end at sea level
and each step up or down represents a 1 unit change in altitude. We define the following
terms:
● A mountain is a sequence of consecutive steps above sea level, starting with a step
up from sea level and ending with a step down to sea level.
● A valley is a sequence of consecutive steps below sea level, starting with a step
down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number
of valleys he walked through.
For example, if Gary's path is s = [D D U U U U D D] , he first enters a valley 2 units deep.
Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and
ends his hike.
Function Description
Complete the countingValleys function in the editor below. It must return an integer that
denotes the number of valleys Gary traversed.
countingValleys has the following parameter(s):
● n : the number of steps Gary takes
● s: a string describing his path
Input Format
The first line contains an integer n , the number of steps in Gary's hike.
The second line contains a single string s , of n characters that describe his path.
Constraints
● 2 ≤ n ≤ 10⁶
● s[i] ∈ { U D }

## Question No.4 (the answer is in file no4.py)
Andrew walks through 100 switches from point A to point B with 1 to 100 as the number.
At the first trip, Andrew presses all of the switches so lamps are on. Second trip, Andrew
only presses switches that multiplying of two. The next trip, Andrew presses switches
that multiplying of three. Andrew repeats his trips from A to B for 100 times. Write down
the code to determine how many lamps will turn on after 100 trips from A to B.

# How to run the code
Make sure you have installed Python 3.x in your computer.
After you have installed do the following steps:
- Download the file from this repository.
- Open Command Prompt go to the location where the file is located.
- To run the program type "python name_file.py" (ex: "python no1.py")

