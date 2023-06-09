import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('留言的平均長度是: ', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆資料提到good')

# 文字計數
start_time = time.time()
wc = {}  # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:  # 把字典的key找出來
    if wc[word] > 10000:
        print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print('總數量: ', len(wc))


while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')
