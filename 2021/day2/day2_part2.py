# 2021 day2
# to find horizontal down position and mulitply them
def find_final_pos(filename : str ='input') -> int:
    with open(filename,'r') as fh:
        horizontal = 0
        depth = 0
        aim = 0
        for movement in fh:
            m = movement.split(' ')
            command, distance = m[0], int(m[1])
            if command=='forward':
                horizontal+=distance
                depth+=(aim*distance)
            elif command=='up':
                aim-=distance
            elif command=='down':
                aim+=distance
    return horizontal, depth

if __name__=='__main__':
    h, d = find_final_pos()
    print(h * d) # 1781819478
