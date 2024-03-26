candle = [4,4,1,3]
dic_cand = {}
for i in candle:
    if i in dic_cand:
        dic_cand[i] += 1
    else:
        dic_cand[i] = 1

max_candle = max(candle)
print(max_candle)
print(dic_cand)

for i in dic_cand:
    if i == max_candle:
        print("Loose Koothi Solution", dic_cand[i])