# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:49:32 2019

@author: huyn
"""

import re
#/*
# * Acme Co. has created a sensor that produces data in the form of discrete
# * messages that are each 120 bytes long. The messages are transmitted over a
# * noisy physical link that might drop data. Due to communication limitations,
# * the measurements are divided into 10 fragments and transmitted one fragment
# * at a time. Your task is to write a function that reads the next complete
# * message from a stream of incoming fragments. If the communication ends before
# * a complete message is received, then the function should report failure. Code
# * to read the fragment binary data is provided for you. Your code is
# * responsible for decoding the fragments.
# *
# * Each fragment is 16 bytes long and consists of two parts: a 4-byte header,
# * and 12 bytes of fragment payload.
# *  - byte 0: Message ID, upper 8 bits
# *  - byte 1: Message ID, lower 8 bits
# *  - byte 2: Fragment ID
# *  - byte 3: Message data checksum
# *  - bytes 4-15: Fragment payload (12 bytes)
# *
# * The fields are explained as:
# *  - Message ID : 16-bit unsigned integer that identifies the message. Every
# *    fragment in a single message is transmitted with the same message ID. The
# *    sensor increments this field with every new message transmitted.
# *  - Fragment ID : 8-bit unsigned integer that identifies the fragment, and
# *    ranges from 0 for the first message fragment to 9 for the last message
# *    fragment.
# *  - Message data checksum : 8-bit naive checksum, calculated as the lower
# *    8-bits of the sum of all 120 unsigned bytes in a message. All fragments in
# *    the same message will report the same message data checksum. Sequential
# *    fragments from the same message carry successive 12 byte portions of the
# *    message data in the fragment payloads. For example, fragment 0 carries
# *    bytes 0-11, fragment 1 carries bytes 12-23, etc.
# *
# * Sequential fragments from the same message carry successive 12 byte portions
# * of the message data in the fragment payloads. For example, fragment 0 carries
# * bytes 0-11, fragment 1 carries bytes 12-23, etc.
# *
# * Things to keep in mind
# *  - The communication link is lossy and may silently drop fragments.
# *  - Fragments are always delivered in the order they are transmitted. Your
# *    code does not need to handle interleaved messages or out of order
# *    delivery.
# *
# * Example 0
# *  - Successive calls to ReadFragment() return fragments 0 - 9 of message 0
# *  - ReadMessage() should populate the output buffer with the contents of
# *    message 0 and return true
# *
# * Example 1
# * - Successive calls to ReadFragment() return
# *    - fragments 0-7 of message 0
# *    - fragment 9 of message 0
# *    - fragments 5-9 of message 1
# *    - fragments 0-9 of message 2
# * - ReadMessage() should populate the output buffer with the contents of
# *   message 2 and return true
# */
class Fragment:
    def __init__(self,messageID,fragMentID,CheckSum,payLoad):
        self.messageID= messageID
        self.fragmentID = fragMentID
        self.checkSum= CheckSum
        self.payLoad= payLoad


#/*
# * A pixel color is defined as a 24 bit integer. Each of the 3 bytes making up
# * the integer represents one of three colors: red, green or blue. The intensity
# * of a pixel is proportional to its byte value which will range from 0 which
# * results in none of that color, to 255, the maximum intensity.
# *
# * Determine which of the pure colors a series of pixels are nearest to. To do
# * this, calculate the Euclidean distance of each of the RGB values of a pixel
# * to the RGB values of a pure color. For the distance between two pixels having
# * RGB values (r 1 , g 1 , b 1 ) and (r 2 , g 2 , b 2 ), it is calculated as
# * follows: d = sqrt( (r1-r2)^2 + (g1-g2)^2 + (b1-b2^2) )
# *
# * For reference, the RGB values are defined as follows:
# *
# * |  Pure Color  |  R  |  G  |  B  |
# * |--------------|-----|-----|-----|
# * | Black        |  0  |  0  |  0  |
# * | White        | 255 | 255 | 255 |
# * | Red          | 255 |  0  |  0  |
# * | Green        |  0  | 255 |  0  |
# * | Blue         |  0  |  0  | 255 |
# *
# * Given a 24-bit binary string describing a pixel, identify which of these five
# * colors the pixel is closest to using the Euclidean distance calculation. Then
# * return the closest pure color: Red, Green, Blue, Black, White or if the pixel
# * is equidistant from two or more colors, return Ambiguous.
# *
# * For example, the pixel described by the binary string
# * 000000001111111100000110 has the following three components:
# *  1. red = (00000000) 2 = (0) 10
# *  2. green = (11111111) 2 = (255) 10
# *  3. blue = (00000110) 2 = (6) 10
# *
# * This means the pixel's RGB value is (0, 255, 6). Now, calculate its Euclidean
# * distance to each color:
# *
# *  - Pure Black: d = 255.0705785
# *  - Pure White: d = 356.4070706
# *  - Pure Red: d = 360.6743684
# *  - Pure Green: d = 6
# *  - Pure Blue: d = 356.4070706
# *
# * The color with the smallest distance to the pixel is Pure Green, so the
# * answer is Green.
# *
# * Complete the function closestColor in the editor below. The function must
# * return an array of strings each representing the closest color for the pixels
# * in the order presented.
# *
# * Sample Input 0
# * - 101111010110011011100100
# * - 110000010101011111101111
# * - 100110101100111111101101
# * - 010111011010010110000011
# * - 000000001111111111111111
# *
# * Sample Output 0
# *  - White
# *  - White
# *  - White
# *  - Green
# *  - Ambiguous
# *
# * Explanation 0: Process the following n = 5 binary strings:
# * 0. 101111010110011011100100 → (189, 102, 228) is closest to White:
# *     - The distance to pure White is 168.80165875962237.
# *     - The distance to pure Blue is 216.45784809056934.
# *     - The distance to pure Red is 258.3486016993318.
# *     - The distance to pure Black is 313.22356233208257.
# *     - The distance to pure Green is 333.33766663850037.
# * 1. 110000010101011111101111 → (193, 87, 239) is closest to White:
# *     - The distance to pure White is 179.78876494375282.
# *     - The distance to pure Blue is 212.30638238168913.
# *     - The distance to pure Red is 261.7899921692959.
# *     - The distance to pure Black is 319.2788749666974.
# *     - The distance to pure Green is 350.13425996323184.
# * 2. 100110101100111111101101 → (154, 207, 237) is closest to White:
# *     - The distance to pure White is 113.26517558367179.
# *     - The distance to pure Blue is 258.62907802488104.
# *     - The distance to pure Green is 286.6862396418775.
# *     - The distance to pure Red is 330.4829798945779.
# *     - The distance to pure Black is 350.334126228091.
# * 3. Etc.
# *
# * Return the array ["White", "White", "White", "Green", "Ambiguous"] as the
# * answer.
# */
class Color():
    def __init__(self,string):        
        self.red= int(string[:8],2)
        self.green = int(string[8:16],2)
        self.black = int(string[16:],2)
    def compare(self,otherColor):
        return (self.red-otherColor.red)**2+(self.green-otherColor.green)**2+(self.black-otherColor.black)**2
    def isClosest(self,colorDic):
        minimum= float("inf")
        minColor = None
        count    = 0
        for key in colorDic:
            distance = self.compare(colorDic[key])
            if distance<minimum:
                minimum = distance
                minColor = key
                count = 1
            elif distance == minimum:
                count+=1
        if count ==1:
            return minColor
        return "Ambiguous"
def closestColor(binColors):
    colorDic= {"Red":Color("111111110000000000000000"),"Black":Color("000000000000000000000000"),
           "White":Color("111111111111111111111111"),"Green":Color("000000001111111100000000"),
            "Blue":Color("000000000000000011111111")}
    answ=[]
    for color in binColors:
        color = Color(color)
        answ.append(color.isClosest(colorDic))
    return answ
#binColors = ["101111010110011011100100","110000010101011111101111","100110101100111111101101","010111011010010110000011",
#             "000000001111111111111111"]
#print (closestColor(binColors))

#/*
# * Number of paths in a matrix
# *
# * Consider a maze mapped to a matrix with an upper left corner at coordinates
# * (row, column) = (0, 0). Any movement must be in increasing row or column
# * direction. Determine the number of distinct paths through the maze. Always
# * start at position (0, 0), the top left, and end up at (max(row),
# * max(column)), the bottom right.
# *
# * As an example, consider the following diagram where 1 indicates an open cell
# * and 0 indicates blocked. It is only possible to travel through open cells, so
# * no path can go through the cell at (0, 2). There are two distinct paths to
# * the goal.
# *
# * +---+---+---+---+
# * | 1 | 1 | 0 | 1 |
# * +---+---+---+---+
# * | 1 | 1 | 1 | 1 |
# * +---+---+---+---+
# *
# * Complete the function numberOfPaths in the editor below. The function must
# * return the number of paths through the matrix, modulo (10^9 + 7).
# *
# * Constraints
# *   - 1 ≤ n, m ≤ 1000
# *   - Each cell in matrix a contains either a 0 or a 1.
# */
def numberOfPaths(grid):
    row = len(grid)
    col = len(grid[0])
    matrix = [[0]*col for i in range(row)]
    matrix[0][0]=grid[0][0]
    for i in range(1,row):
        matrix[i][0] = min(matrix[i-1][0],grid[i][0])
        
    for j in range(1,col):
        matrix[0][j]= min(matrix[0][j-1],grid[0][j])
    for i in range(1,row):
        for j in range(1,col):
            if not grid[i][j]:
                matrix[i][j]=0
            else:
                matrix[i][j]= matrix[i-1][j]+matrix[i][j-1]
    return matrix[row-1][col-1]
grid = [[1,1,0,1],[1,1,1,1]]
print (numberOfPaths(grid))

#/*
# * There are n particles numbered from 0 to n − 1 lined up from smallest to
# * largest ID along the x-axis.
# *
# * The particles are all released simultaneously. Once released, each particle
# * travels indefinitely in a straight line along the positive x-axis at a speed.
# * When two particles collide, the faster particle moves through the slower
# * particle and they both continue moving without changing speed or direction.
# *
# * Complete the function collision in the editor below. The function must return
# * the number of collisions occurring with particle pos.
# */
def collision(speeds,pos):
    n = len(speeds)
    count =0 
    for i in range(pos):
        if speeds[i]>speeds[pos]:
            count+=1
    for i in range(pos+1,n):
        if speeds[pos]>speeds[i]:
            count+=1
    return count
#/**
# * We consider a software version string (major).(minor)(modifier) to be a valid
# * version identifier if it 4 satisfies the following constraints:
# * - (major) is a sequence of one ore more digits denoted by the character class
# *   [0-9]
# * - (minor) is a sequence of one ore more digits denoted by the character class
# *   [0-9]
# * - (modifier) is an optional string of the following form:
# *     - Starts with the tilde "~" character
# *     - The tilde is followed by exactly one of the release type strings
# *       "alpha", "beta", or "rc"
# *     - The release type string is followed a sequence of one or more digits
# *       denoted by the character class [0-9] 5 For example, "1.2" and
# *       "3.4~alpha0" are valid version strings, but "567" is not.
# *
# * For example, "1.2" and "3.4~alpha0" are valid version strings, but "567" is
# * not.
# *
# * Your task is to create a regular expression that exactly matches valid
# * version strings.

texts = {"1x2~rc1":False,
        "123~alpha":False,
        "12345.~alpha1":False,
        "67890.1":True,
        "67890.1~beta973":True,
        "23415.67~alpha0":True,
        "83461.678~rc12":True,
        "91734.9012~alpha938":True,
        "31679.00000~rc432":True,
        "7371.00000~beta99":True,
        "371.98316~alpha1":True,
        "31.19260~rc2":True,
        "1.92167~beta98":True,
        ".92167~97":False,
        "43.98~alpha53486":True,
        "43.98~alpha5":True}
        
for s in texts:
    pattern = re.search(r'(^\d+\.\d+)(~(alpha|beta|rc)\d+){0,1}$',s)
    if pattern and not texts[s]:
        print (pattern.group())
    if not pattern and texts[s]:
        print (s)