#Python program to perform Selection Sort in Python

def selection_sort(unsorted_list):
    for i in range(0,len(unsorted_list)-1):
        smallest=i
        for j in range(i+1,len(unsorted_list)):
            if unsorted_list[j]<unsorted_list[smallest]:
                smallest=j
        unsorted_list[i], unsorted_list[smallest]=unsorted_list[smallest],unsorted_list[i]
unsorted_list = input('Enter unsorted numbers : ').split()
unsorted_list = [int(x) for x in unsorted_list]
selection_sort(unsorted_list)

print(unsorted_list)