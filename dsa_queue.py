# Queue 
from collections import deque
queue=deque()

queue.append(30)
queue.append(10)
queue.append(40)
queue.append(70)
print(queue)
# o/p = [30, 10, 40, 70]
queue.popleft()
print("updated queue",queue)

if not queue:
    print("queue is empty...!")
else:
    print("queue is not-empty...!")
print("final queue values",queue)