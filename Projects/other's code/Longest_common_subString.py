
def LCSubString(String1, String2):
    l1 = len(String1) + 1
    l2 = len(String2) + 1
    grid = [[0 for i in range(l1)] for j in range(l2)]
    longest = 0
    for i in range(l1):
    	for j in range(l2):
    		if i > 0 and j > 0:
    			if String1[i-1] == String2[j-1]:
    				grid[i][j] = grid[i-1][j-1]+1
    				longest = max(longest , grid[i][j])
    # print(grid)
    return longest

def LCSubSequence(String1, String2):
    l1 = len(String1) + 1
    l2 = len(String2) + 1
    grid = [[0 for i in range(l1)] for j in range(l2)]
    longest = 0
    for i in range(l1):
    	for j in range(l2):
    		if i > 0 and j > 0:
    			if String1[i-1] == String2[j-1]:
    				grid[i][j] = grid[i-1][j-1]+1
    			else:
    				grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    print(grid)
    return grid[-1][-1]




if __name__ == '__main__':
    s1 = "fish"
    s2 = "fosh"
    s3 = "fort"
    common1 = LCSubSequence(s1, s2)
    common2 = LCSubSequence(s2, s3)
    print(common1, common2)