test_file = open("test.txt").readlines()
print(test_file)

for i in range(len(test_file)):
    test_file[i] = int(test_file[i])
print(test_file)

for i in test_file:
    i = int(i)
print(test_file)


