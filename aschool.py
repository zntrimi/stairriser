a = "konnʲitɕiɰa ɰa taɕino‾"

d ={}
chh = ''
max = 0 
for ch in a : d[ch] = d.get(ch,0) +1 
for val in sorted(d.items(),reverse=True , key = lambda ch : ch[1]):
    chh = ch
    max  = d.get(ch)


print(chh)  
print(max)  