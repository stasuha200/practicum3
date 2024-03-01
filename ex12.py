a = list(map(int, input().split()))
att = a[0]
comp = a[1]
yds = a[2]
td = a[3]
inter = a[4]
a = (comp / att - 0.3) * 5
b = (yds / att - 3) * 0.25
c = (td / att) * 20
d = 2.375 - (inter / att * 25)
print((a + b + c + d) / 6 * 100)
