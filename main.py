#讀檔
def r_file(file):
    count = 0
    lines = []
    with open(file, 'r') as line:
        for i in line:
            lines.append(i)
            count += 1
            if count >= 100:
                break
    return lines        

#轉換
def c_file(lines):
    f_l = []
    for line in lines:
        f = line.split(' ')
        f_l.append(f)
    return f_l
#s = list.split(' ')

#計數
def dis(lines):
    dis ={}
    for line in lines:
        for i in line:
            if i in dis:
                dis[i] += 1
            else:
                dis[i] = 1    
    return dis


def main(file):
    read = r_file(file)
    count = c_file(read)
    d = dis(count)
    return d
file_name = 'reviews.txt'


main = main(file_name)

max_key = max(main, key=lambda k: main[k])

print('使用最多的單字為', max_key, '使用次數為', main[max_key], '次')
