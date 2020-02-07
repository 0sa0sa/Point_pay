first_money, bus_num = map(int,input().split())
cost_list = [int(input()) for _ in range(bus_num)]

#print((cost_list[1]))
point = 0
residue = first_money
for i in range(bus_num):
    #print(i)
    if cost_list[i] < point:
        point -= cost_list[i]
    else:
        point += int(cost_list[i]*0.1)
        residue -= int(cost_list[i])
    print(residue,point)
