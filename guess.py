# 產生一個隨機整數1到100
import random
start = input('請決字隨機數字範圍開始值:')
end = input('請決字隨機數字範圍結束值')
start = int(start)
end = int(end)
count =0
r = random.randint(1, 100)
while True:
	count += 1 # count = count + 1
	number = input('請猜數字')
	number = int(number)
	if number == r:
		print('你猜中了')
		print('這是你猜的第', count,'次')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('這是你猜的第', count,'次')
