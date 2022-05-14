# 2021 day1 part2
# to find number of times sum of sliding window increases
def count_sum_sliding_window_increases(filename : str ='input', window_range : int =3) -> int:
    with open(filename,'r') as fh:
        count=0
        sliding_window = [int(fh.readline()) for i in range(window_range)]
        for depth in fh:
            prev_sum = sum(sliding_window)
            sliding_window[:window_range-1]= sliding_window[1:]
            sliding_window[-1] = int(depth)
            if prev_sum < sum(sliding_window):
                count+=1
    return count

if __name__=='__main__':
    print(count_sum_sliding_window_increases()) # 1127
