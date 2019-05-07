import sys
#Abridged Problem Description:
#Let (x, y) be the coordinates of a student’s house on a 2D plane. There are 2N students
#and we want to pair them into N groups. Let di be the distance between the houses
#of 2 students in group i. Form N groups such that cost = sum of d_i is minimized.
#Output the minimum cost. Constraints: 1 ≤ N ≤ 8 and 0 ≤ x, y ≤ 1000.
#Sample input:
#N = 2; Coordinates of the 2N = 4 houses are {1, 1}, {8, 6}, {6, 8}, and {1, 3}.
#Sample output:
#cost = 4.83.

def distance(x,y):
    return round(((x[0]-y[0])**2+(x[1]-y[1])**2)**.5,2)
def solve(array):
    
    return None
                

          
def main():
    sys.stdout.flush()
    N = input.strip().split()
    while N:
        N = int(N)
        array  = []
        for i in range(2*N):
            item  = input.strip().split()
            x     = int(item[1])
            y     = int(item[2])
            array.append(x,y)
        result = solve(array)
    print ("Case {}: {}".format(i+1,result))
if __name__ =="__main__":
    main()
    