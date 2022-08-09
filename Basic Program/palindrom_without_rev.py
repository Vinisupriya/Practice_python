text = 'madam'
i=0
j= len(text)-1
while i<j:
    if text[i]!=text[j]:
        print("NOT PALINDROM")
        break
    i=i+1
    j=j-1
else:
        print("PALINDROM")