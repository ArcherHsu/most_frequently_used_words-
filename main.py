#讀檔
def r_file(file):
    lines = []
    with open(file, 'r') as line:
        for i in line:
            lines.append(i)
    return lines        


#轉換
def c_file(lines):
    f_l = []
    for line in lines:
        f = line.split()
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


#主運行段落
def main(file):
    read = r_file(file)
    count = c_file(read)
    d = dis(count)
    return d


#運行
file_name = 'reviews.txt'
main = main(file_name)


for word in main:
    if main[word] > 1000000:
        print(word, '的出現次數為', main[word], '次')

max_key = max(main, key=lambda k: main[k])
print('使用最多的單字為', max_key, '使用次數為', main[max_key], '次')

while True:
    inp = input('請輸入想查詢的單字')
    if inp =='q':
        break
    elif inp in main:
        print(inp, '出現的次數為', main[inp], '次') 
    else:
        print('留言中沒有',inp ,'的紀錄,請使用別的單字或鍵入 q 離開')    
print('歡迎體驗本次查詢')  