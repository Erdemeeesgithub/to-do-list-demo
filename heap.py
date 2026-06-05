# left child 2i + 1 
# right child 2i + 2
# parent (i-1) // 2

class MinHeap: 
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)
        
    def pop(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        item = self.heap.pop()
        self._bubble_down(0)
        return item
        
    def _bubble_up(self, i):
        while i > 0:
            parent = (i-1) // 2 
            if self.heap[i]['priority'] < self.heap[parent]['priority']:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
            
    def _bubble_down(self, i):
        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i
        
            if left < len(self.heap) and self.heap[left]['priority'] < self.heap[smallest]['priority']:
                smallest = left
        
            if right < len(self.heap) and self.heap[right]['priority'] < self.heap[smallest]['priority']:
                smallest = right
        
            if smallest == i:
                break
        
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest