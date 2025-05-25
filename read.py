data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %代表求餘數
			print(len(data))
print(len(data))
print('---------------------------------------')
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for each_data in data:
	sum_len += len(each_data)
print('每一筆留言的平均長度是:', sum_len/len(data), '個字')