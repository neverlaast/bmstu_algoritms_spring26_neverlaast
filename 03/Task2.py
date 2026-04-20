import heapq

def find_k_max_with_heap(nums, k):
    
    heap = []

    for num in nums:

        #добавляем элемент в кучу
        heapq.heappush(heap, num)
        #проверяем размер кучи
        if len(heap) > k:
            heapq.heappop(heap)
            
    #остается k наибольших элементов с k-max наверху
    return heapq.heappop(heap)
