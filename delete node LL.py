
from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    count =0 
    while(head):
        count+=1
        head = head.next
    return count


def deleteNode(head, pos) :
    #Your code goes here
    if pos<0 and pos>length(head):
        return head
    
    curr = head
    prev = None
    count = 0
    while(curr is not None) and (count<pos-1):
        count += 1
        curr = curr.next
        
        
    if(curr is None) or (curr.next is None):
        return head
    if(pos == 0):
        head = head.next
    else:
        curr.next = curr.next.next
       	
        
    return head







#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1