import os

def comm(numberWorkers, representationSize, walkLength, windowSize):
    input = '../network/community(a).txt'   # 修改为自己的路径（存放网络）
    output = '../network/' + numberWorkers + 'v' + representationSize + 'v'\
             + walkLength +'v'+windowSize + '.embeddings'
    numberWorkers = ' --number-walks ' + numberWorkers
    representationSize = ' --representation-size ' + representationSize
    walkLength = ' --walk-length ' + walkLength
    windowSize = ' --window-size ' + windowSize

    comm = "python __main__.py --format edgelist --input " + input + ' --output ' + output + \
           numberWorkers + representationSize + walkLength + windowSize    # 如果使用的是其他网络格式，修改format
    print(comm)
    d = os.system(comm)
    print(d)


if __name__ == '__main__':
    '''
    这里遍历不同的参数，便于后面找到最优值
    '''
    for i in [1, 3, 10, 30, 50, 90]:
        for j in [4, 8, 16, 32, 64, 128]:
            for k in [20, 40, 60, 80]:
                for l in range(5, 35, 5):
                    comm(str(i), str(j), str(k), str(l))

