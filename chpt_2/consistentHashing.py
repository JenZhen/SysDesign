# http://lintcode.com/en/problem/consistent-hashing/
#
# Clarification
# If the maximal interval is [x, y], and it belongs to machine id z, when you add a new machine with id n, you should divide [x, y, z] into two intervals:

# [x, (x + y) / 2, z] and [(x + y) / 2 + 1, y, n]

# Example
# for n = 1, return

# [
#   [0,359,1]
# ]
# represent 0~359 belongs to machine 1.

# for n = 2, return

# [
#   [0,179,1],
#   [180,359,2]
# ]
# for n = 3, return

# [
#   [0,89,1]
#   [90,179,3],
#   [180,359,2]
# ]
# for n = 4, return

# [
#   [0,89,1],
#   [90,179,3],
#   [180,269,2],
#   [270,359,4]
# ]
# for n = 5, return

# [
#   [0,44,1],
#   [45,89,5],
#   [90,179,3],
#   [180,269,2],
#   [270,359,4]
# ]

class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        # write your code here
        if n == 0:
            return [[]]
        ret = [[0, 359, 1]]
        # i loop iterates i times to
        # caculate i intervals
        for i in range(1, n):
            # splitAt indicates which interval to split
            splitAt = 0
            # iterate thru i (current intervals)
            # to find the biggest to split
            for j in range(i):
                if ret[j][1] - ret[j][0] > ret[splitAt][1] - ret[splitAt][0]:
                    splitAt = j
            start = ret[splitAt][0]
            end = ret[splitAt][1]

            ret[splitAt][1] = int((start + end) / 2)
            newInterval = [int((start + end) / 2 + 1), end, i + 1]
            ret.append(newInterval)
        return ret


def printIntervals(ret):
    numMachines = len(ret)
    print('[')
    for i in range(numMachines):
        print('[' + ', '.join(map(str, ret[i])) + ']')
    print(']')

if __name__ == "__main__":
    solution =  Solution()
    ret = solution.consistentHashing(2)
    printIntervals(ret)
