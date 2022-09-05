class node:

def __init__(s,x):

s.data=x
s.next=None

class queueList:

def __init__(self):
self.front=None
self.rear=None

def enqueue(self,n):
N d d ( )

newNode = node(n)

if(self.front == None):
self.front = newNode

return

else:

temp = self.front
while(temp.next != None):

temp = temp.next
temp.next = newNode

def display(self):

if self.front==None:

print("stack is empty")

else:

temp=self.front
while temp!=None:

print(temp.data)
temp=temp.next

def dequeue(self):
temp=self.rear
self.front=self.front.next

ql=queueList()
while(1):

print("1.Enqueue

2.Dequeue

ch=int(input("Enter your choice:"))
if ch==1:

3.Display

n=int(input("Enter the data to be pushed:"))
ql.enqueue(n)

elif ch==2:

ql.dequeue()

elif ch==3:

ql.display()

else:

break
