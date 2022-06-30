print(" ")
print("Resolution Calculator 2019 || Made By Francis-Shin")
print("---------------------------------------------------")
f = open('device_res.txt', 'r')
res = f.readlines()
for i in range(0, 2):
    res[i] = res[i].replace('\n','')
print("Currently saved device's rsolution")
f.close()
print("Width : %s"%res[0])
print("Height : %s"%res[1])

renew = input("Do you want to change device's resolution? (y/n) ")
if renew is "y":
    f = open('device_res.txt', 'w')
    f.write(input("Please, input device's width  "))
    f.write("\n")
    f.write(input("And, input device's height  "))
    f.close()
else:
    pass
device_res = []
get_file = open('device_res.txt', 'r')
lines = get_file.readlines()
for line in lines:
    device_res.append(line.strip('\n'))
get_file.close()
c = input("Please, input target's absolute_res['x']  ")
d = input("And, input target's absolute_res['y']   ")
absolute_res = [c, d]
relative_res = []
for i in range(0,2):
    relative_res.append(int(absolute_res[i])/int(device_res[i]))
print(relative_res)
