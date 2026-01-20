class Node: 
    def __init__(self,data):
        self.data=data 
        self.next = None 
        
# Create nodes 
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Node connections 
head.next = node2 
node2.next = node3
node3.next = node4
node4.next = node5

# print the node 
print("OG Node =")
current = head 

while current is not None:
    print(current.data,end="=>")
    current=current.next
print("None")
#o/p =  OG Node =10=>20=>30=>40=>50=>None

# task = add new element 70 between 30 and 40
        