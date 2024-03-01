a = list(map(int, input().split()))
rub = a[0]
kop = a[1]
counts = a[2]
pr_rub = rub * counts + (kop * counts // 100)
pr_kop = kop * counts % 100
print(pr_rub, 'руб.', pr_kop, 'коп.')
