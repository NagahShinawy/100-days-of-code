row1 = ["😊", "😊", "😊"]
row2 = ["😊", "😊", "😊"]
row3 = ["😊", "😊", "😊"]
_map = [row1, row2, row3]
print(f"\t1\t\t2\t\t3")
print(f"1 {row1}\n2 {row2}\n3 {row3}\n")

position = input("Enter Position Row Col")

row = int(position[0]) - 1
col = int(position[1]) - 1

print(row, col)

treasure = "Gold"

_map[row][col] = treasure

print(_map)
