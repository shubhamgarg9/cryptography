key = 'zebras'

mapList = []
for i in key:
	mapList.append(i)

for i in range(97,123):
	if chr(i) not in key:
		mapList.append(chr(i))

message = 'flee at once. we are discovered!'
ans = ""

for i in message:
	print i
for i in message:
	if ord(i)>96 and ord(i)<123:
		ans = ans + mapList[ord(i)-97]
	else:
		ans = ans + i

print ans