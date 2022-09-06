
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
het = int(position[0])
vet = int(position[1])
map[vet-1][het-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


