class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    

input = [9,8,7,6,5,4,3,2,1]
class HeapBuilder:
        class MinHeap:
            def __init__(self):
                self.a=[]
                  
            #insert a new element into the minheap
            def insert(self,val):
                self.a.append(val)
                i = len(self.a) -1
                while i > 0 and self.a[(i-1) //2] > self.a[i]:
                     self.a[i],self.a[(i-1)//2] = self.a[(i-1) //2],self.a[i]
                     i = (i-1)//2

            def minHeapify(self,i,n):
                 #Formula for finding the left and right child of any element in the heap 
                smallest = i
                left = 2* i +1
                right = 2*i+2

                if left < n and self.a[left] < self.a[smallest]:
                      smallest = left
                if right < n and self.a[right] < self.a[smallest]:
                     smallest = right
                if smallest != i:
                     self.a[i],self.a[smallest] = self.a[smallest],self.a[i]
                     self.minHeapify(smallest,n)

            def printheap(self):
                print("min Heap", self.a)
                 

minheap = HeapBuilder.MinHeap()                 
for val in input:
     minheap.insert(val)
minheap.printheap()
     

    

            

