s = "MCMXCIV"
sum = 0  # 累加数字
rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
i = 0
while i < len(s):
    if i < len(s) - 1 and rome.get(s[i]) < rome.get(s[i + 1]):
        sum += rome.get(s[i + 1]) - rome.get(s[i])
        i += 2
        continue
    sum += rome.get(s[i])
    i += 1
print(sum)
