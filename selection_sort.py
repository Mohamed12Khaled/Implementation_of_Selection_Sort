l = []
x = int(input("enter the number of elements in the list"))
for i in range(x):
    y = int(input("enter the number"))
    l.append(y)
def selection_sort(l):
    for i in range(len(l)-1, 0, -1):
        max=0
        for j in range(1, i+1):
            if l[j] > l[max]:
                max = j
        print(l)
        l[i], l[max] = l[max], l[i]
selection_sort(l)