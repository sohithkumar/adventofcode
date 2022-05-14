# 2021 day3 part2
# to find 
def find_gamma_epsilon(filename : str ='input') -> int:
    with open(filename,'r') as fh:
        dict_freq = {}
        bs = fh.readline()
        for i in range(len(bs.strip())):
            dict_freq[i]={}
            if bs[i]=='1':
                dict_freq[i]['1']=1
                dict_freq[i]['0']=0
            else:
                dict_freq[i]['1']=0
                dict_freq[i]['0']=1
        for bs in fh:
            for i,s in enumerate(bs.strip()):
                dict_freq[i][s]+=1
    gamma = ''
    epsilon = ''
    for i in range(len(dict_freq)):
        if dict_freq[i]['1']>dict_freq[i]['0']:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
        print(gamma,epsilon)
    return int(gamma,2), int(epsilon,2)

if __name__=='__main__':
    g, e = find_gamma_epsilon()
    print(g * e) # 2724524
