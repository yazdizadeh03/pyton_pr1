listf = ["apple", "banana", "cherry", "apple", "cherry"]
lengn = 0
nlen = 1

while lengn != nlen:
    lengn = len(listf)
    if "apple" in listf:
        listf.remove("apple")
    nlen = len(listf)

print(listf)
