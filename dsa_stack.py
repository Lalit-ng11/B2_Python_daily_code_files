stack = []

# push elements in stack
stack.append(10)
stack.append(40)
stack.append(20)
stack.append(50)
# print("stack elements =",stack)
# o/p: stack elements = [10, 40, 20, 50]

# remove/ delete elements
stack.pop()
# print("updated stack=",stack)
# updated stack= [10, 40, 20]
top_element=stack[-1]
# print(top_element) 

# checking whether stack is empty or not
if not stack:
    print("stack is empty...!")
else:
    print("stack is not-empty...!")
print("final stack values",stack)