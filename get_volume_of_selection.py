import trimatic
selected = trimatic.get_selection()
i = 0
for x in selected:
    i = x.volume + i

i = i*0.001
print(i)
