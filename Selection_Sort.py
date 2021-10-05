#Python program to perform Selection Sort in Python

def selectionSort(unsorted_list):
    for i in range(0, len(unsortedList)-1):
        smallest=i
        for j in range(i+1,len(unsortedList)):
            if unsortedList[j]<unsortedList[smallest]:
                smallest=j
        unsortedList[i], unsortedList[smallest]=unsortedList[smallest],unsortedList[i]
unsortedList = input('Enter unsorted numbers : ').split()
unsortedList = [int(x) for x in unsortedList]
selectionSort(unsortedList)

print(unsortedList)
