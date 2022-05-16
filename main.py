first = ['1','2','3','4']
second = ['2','12','14','10']

def outdoor(first, second):
    return [x for x in first if x not in second]

array = ['0','1','2','5','6','0']
def notzero(array):
    return [x for x in array if x != '0']
    

if __name__ == '__main__':
    print (notzero(array))


