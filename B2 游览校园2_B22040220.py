# def find_disjoint_paths(graph, start1, end1, start2, end2, required_nodes):
#     def find_all_paths(graph, start, end, visited=None, path=None):
#         """Find all paths from start to end in a graph, avoiding revisiting nodes."""
#         if visited is None:
#             visited = set()
#         if path is None:
#             path = []

#         visited.add(start)
#         path.append(start)

#         if start == end:
#             yield path[:]
#         else:
#             for neighbor in graph.get(start, []):
#                 if neighbor not in visited:
#                     yield from find_all_paths(graph, neighbor, end, visited, path)

#         visited.remove(start)
#         path.pop()

#     # Find all possible paths for the first route
#     all_first_paths = list(find_all_paths(graph, start1, end1))

#     for first_path in all_first_paths:
#         # Calculate remaining required nodes and construct a subgraph excluding the first path nodes
#         first_path_set = set(first_path)
#         remaining_required_nodes = required_nodes - first_path_set
#         remaining_graph = {node: [neighbor for neighbor in neighbors if neighbor not in first_path_set]
#                            for node, neighbors in graph.items() if node not in first_path_set}

#         # Find all possible paths for the second route in the remaining graph
#         all_second_paths = list(find_all_paths(remaining_graph, start2, end2))

#         for second_path in all_second_paths:
#             # Check if the second path covers all remaining required nodes
#             if remaining_required_nodes.issubset(second_path):
#                 return first_path, second_path

#     # If no valid paths found, return None
#     return None, None

# # Define the adjacency list (graph)
# graph = {
#     '北门': ['体育场', '计算机学科楼'],
#     '体育场': ['北门', '计算机学科楼', '三食堂'],
#     '计算机学科楼': ['北门', '西门', '体育场', '三食堂', '图书馆'],
#     '南门': ['一食堂', '教学楼', '办公楼'],
#     '一食堂': ['南门', '宿舍楼', '教学楼'],
#     '教学楼': ['南门', '西门', '图书馆', '办公楼', '宿舍楼', '一食堂'],
#     '办公楼': ['南门', '教学楼'],
#     '西门': ['计算机学科楼', '图书馆', '教学楼'],
#     '图书馆': ['西门', '计算机学科楼', '二食堂', '宿舍楼', '教学楼'],
#     '东门': ['二食堂', '三食堂'],
#     '二食堂': ['东门', '三食堂', '图书馆', '宿舍楼'],
#     '三食堂': ['东门', '体育场', '计算机学科楼', '二食堂'],
#     '宿舍楼': ['二食堂', '一食堂', '图书馆', '教学楼'],
# }

# # Define required non-gate nodes that must be visited across both paths
# required_nodes = {'体育场', '计算机学科楼', '三食堂', '二食堂', '一食堂', '图书馆', '宿舍楼', '教学楼', '办公楼'}

# # Set the starting and ending gates for the two paths
# start1, end1 = '西门', '北门'
# start2, end2 = '东门', '南门'

# # Find the two disjoint paths
# first_path, second_path = find_disjoint_paths(graph, start1, end1, start2, end2, required_nodes)
# print("First Path:", first_path)
# print("Second Path:", second_path)
from itertools import permutations

def find_disjoint_paths(graph, start1, end1, start2, end2, required_nodes):
    """
    在图中找到两条不相交的路径，每条路径都从指定的起点到终点，并且两条路径一起覆盖所有必需的节点。
    
    :param graph: 图的邻接表表示
    :param start1: 第一条路径的起点
    :param end1: 第一条路径的终点
    :param start2: 第二条路径的起点
    :param end2: 第二条路径的终点
    :param required_nodes: 必须访问的节点集合
    :return: 生成所有不相交的路径对
    """
    def find_all_paths(graph, start, end, visited=None, path=None):
        """
        在图中找到从起点到终点的所有路径，避免重复访问节点。
        
        :param graph: 图的邻接表表示
        :param start: 起点
        :param end: 终点
        :param visited: 已访问的节点集合
        :param path: 当前路径
        :yield: 生成所有路径
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path.append(start)

        if start == end:
            yield path[:]  # 如果到达终点，生成当前路径
        else:
            for neighbor in graph.get(start, []):  # 遍历邻居节点
                if neighbor not in visited:
                    yield from find_all_paths(graph, neighbor, end, visited, path)  # 递归查找路径

        visited.remove(start)  # 回溯，移除当前节点
        path.pop()

    # 为第一条路线找到所有可能的路径
    all_first_paths = list(find_all_paths(graph, start1, end1))

    for first_path in all_first_paths:
        # 计算剩余需要访问的节点，并构建排除第一条路径节点的子图
        first_path_set = set(first_path)
        remaining_required_nodes = required_nodes - first_path_set
        remaining_graph = {node: [neighbor for neighbor in neighbors if neighbor not in first_path_set]
                           for node, neighbors in graph.items() if node not in first_path_set}

        # 在剩余图中为第二条路线找到所有可能的路径
        all_second_paths = list(find_all_paths(remaining_graph, start2, end2))

        for second_path in all_second_paths:
            # 检查第二条路径是否覆盖了所有剩余需要访问的节点
            if remaining_required_nodes.issubset(second_path):
                yield first_path, second_path

# 定义图的邻接表
graph = {
    '北门': ['体育场', '计算机学科楼'],
    '体育场': ['北门', '计算机学科楼', '三食堂'],
    '计算机学科楼': ['北门', '西门', '体育场', '三食堂', '图书馆'],
    '南门': ['一食堂', '教学楼', '办公楼'],
    '一食堂': ['南门', '宿舍楼', '教学楼'],
    '教学楼': ['南门', '西门', '图书馆', '办公楼', '宿舍楼', '一食堂'],
    '办公楼': ['南门', '教学楼'],
    '西门': ['计算机学科楼', '图书馆', '教学楼'],
    '图书馆': ['西门', '计算机学科楼', '二食堂', '宿舍楼', '教学楼'],
    '东门': ['二食堂', '三食堂'],
    '二食堂': ['东门', '三食堂', '图书馆', '宿舍楼'],
    '三食堂': ['东门', '体育场', '计算机学科楼', '二食堂'],
    '宿舍楼': ['二食堂', '一食堂', '图书馆', '教学楼'],
}

# 定义必须访问的非门节点
required_nodes = {'体育场', '计算机学科楼', '三食堂', '二食堂', '一食堂', '图书馆', '宿舍楼', '教学楼', '办公楼'}

# 定义所有门
gates = ['北门', '南门', '西门', '东门']

# 存储所有有效的路径组合
all_solutions = []

# 遍历所有门的排列组合
for (start1, end1, start2, end2) in permutations(gates, 4):
    # 为每个门组合找到不相交的路径
    for first_path, second_path in find_disjoint_paths(graph, start1, end1, start2, end2, required_nodes):
        all_solutions.append({
            'First Path': first_path,
            'Second Path': second_path,
            'Gate Combination': f"{start1}-{end1} 和 {start2}-{end2}"
        })

# 输出所有解决方案
for solution in all_solutions:
    print("门的组合:", solution['Gate Combination'])
    print("第一条路径:", solution['First Path'])
    print("第二条路径:", solution['Second Path'])
    print("-" * 50)

# 定义文件路径
file_path = "travel2.txt"

# 将结果保存到文件
with open(file_path, "w", encoding="utf-8") as file:
    for solution in all_solutions:
        file.write(f"门的组合: {solution['Gate Combination']}\n")
        for node in solution['First Path']:
            file.write(f"-> {node}")
        file.write("\n")
        for node in solution['Second Path']:
            file.write(f"-> {node}")
        file.write("\n\n")
        file.write("-" * 50 + "\n")

print(f"结果已保存到 {file_path}")

input("程序已运行完成，按Enter键退出...")