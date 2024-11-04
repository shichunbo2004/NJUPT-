import heapq
def find_top_1000(numbers):
    def find_top_1000_in_subset(subset):
        #分组数据个数大于1000
        if len(subset) <= 1000:
            return sorted(subset, reverse=True)[:1000]
        #初始化
        min_heap = []
        #前十个数据入堆
        for number in subset:
            if len(min_heap) < 1000:
                heapq.heappush(min_heap, number)
            else:
                #如果堆已满，比较当前成绩和堆顶元素
                if number > min_heap[0]:
                    heapq.heapreplace(min_heap, number)
        return sorted(min_heap, reverse=True)

    # 合并多个子集的结果
    def merge_top_1000(results):
        min_heap = []
        #对合并的结果找出前1000大的数
        for result in results:
            for number in result:
                if len(min_heap) < 1000:
                    heapq.heappush(min_heap, number)
                else:
                    if number > min_heap[0]:
                        heapq.heapreplace(min_heap, number)
        return sorted(min_heap, reverse=True)

    # 分割数据集
    num_subsets = 100
    #每个数据集大小
    subset_size = len(numbers) // num_subsets
    #每个数据集的范围
    subsets = [numbers[i * subset_size:(i + 1) * subset_size] for i in range(num_subsets)]

    # 对每个子集找出前1000大的数
    top_1000_in_subsets = [find_top_1000_in_subset(subset) for subset in subsets]

    # 合并结果
    return merge_top_1000(top_1000_in_subsets)
#导入文件data2.txt
with open('data2.txt', 'r') as file:
    numbers = []
    for line in file.readlines():
        numbers.extend([int(num) for num in line.strip().split('   ')])
top_1000_numbers = find_top_1000(numbers)
#打印出结果
print(top_1000_numbers)

input("程序已运行完成，按Enter键退出...")   