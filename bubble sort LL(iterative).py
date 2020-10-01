class Node:
    def init(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head) :
   
    end = None
    while end != head:
        p = head
        while p.next != end:
            q = p.next
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            p = p.next
        end = p

    return end
    pass

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = bubbleSortLL(l)
printll(l)