x = int(input())
hours = x // 30
minutes = hours * 60 + ((x - hours * 30) // 2)
print(hours, minutes)
