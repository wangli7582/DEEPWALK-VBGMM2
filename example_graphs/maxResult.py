f = open('VBGMM_result.txt', 'r', encoding="utf-8")
# 读取文件的每一行
lines = f.readlines()
maxscore, maxpara = [], []
for i, line in enumerate(lines):
    # 以冒号作为分割，每一行的字符串分成两部分
    (para, score) = line.strip().split(':')
    # 当maxscore数组中的元素数目小于10的时候直接放到maxscore中
    maxscore.append(score)
maxscore.sort(reverse=True)
print(maxscore)

#     if float(score) > maxscore:
#         maxscore = float(score)
#         maxpara = para
#
# print(maxpara, maxscore)

