import heapq

def find_top_10(scores):
    # 初始化最小堆，heapq默认是最小堆
    min_heap = []
    
    # 遍历所有成绩
    for score in scores:
        # 如果堆未满，直接添加(自动上浮)
        if len(min_heap) < 10:
            heapq.heappush(min_heap, score)
        # 如果堆已满，比较当前成绩和堆顶元素
        else:
            # 如果当前成绩大于堆顶元素，则替换堆顶元素
            if score > min_heap[0]:
                heapq.heapreplace(min_heap, score)
    # 堆中元素即为前10名成绩，取出并反转
    return sorted(min_heap, reverse=True)

# 假设这是所有考生的成绩,从data.txt导入
with open('data.txt', 'r') as file:
    scores = []
    for line in file.readlines():
        scores.extend([int(num) for num in line.strip().split(',')])
top_10_scores = find_top_10(scores)
# 打印成绩，每行输出一个数
for score in top_10_scores:
    print(score)


input("程序已运行完成，按Enter键退出...")   