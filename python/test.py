class heap():
    l = len(arr)

    def swap(self, arr, i ,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


    def adjustTree(self, arr, i):
        max = i
        if 2*i+1 < self.l and arr[i] < arr[2*i+1]:
            max = 2*i+1
        if 2*i+2 < self.l and arr[i] < arr[2*i+2]:
            max = 2*i+2
        if max != i:
            swap(arr, max, i)
            adjustTree(arr, max) #继续比较直到完成一次最大堆

    def buildMaxHeap(self, arr): #从最后一个非子叶点开始构建
        for i in range(int(len(arr)/2)-1,-1,-1):
            adjustTree(arr, i)

    def heapSort(self, arr):
        buildMaxHeap(arr)
        print('1',arr)
        for i in range(len(arr)-1,-1,-1):
            swap(arr, 0, i)
            self.l -= 1
            print('2',arr)
            adjustTree(arr, 0)
            print('3',arr)
        return arr

if __name__ == "__main__":
    arr = [1,6,7,2,3,4,5]

print(heap.heapSort(1, arr))