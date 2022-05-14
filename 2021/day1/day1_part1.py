# 2021 day1 
# to find number of times depth increased
def count_depth_increases(filename : str ='input') -> int:
    with open(filename,'r') as fh:
        count=0
        curr_depth = int(fh.readline())
        for depth in fh:
            if curr_depth<int(depth):
                count+=1
            curr_depth = int(depth)
    return count

if __name__=='__main__':
    print(count_depth_increases()) # 1154
