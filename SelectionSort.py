def swap(A, x, y):
    A[x], A[y] = A[y],A[x]

def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)

def main():
    my_list = [5.76, 4.7, 25.3, 4.6, 32.4, 55.3, 52.3, 7.6, 7.3, 86.7, 43.5]
    selectionSort(my_list)
    print(my_list)

if __name__ == '__main__':
    main()
