# def find_required_coverage_path(graph, current, end, required_nodes, visited=None, path=None):
#     if visited is None:
#         visited = set()
#     if path is None:
#         path = []

#     # Mark the current node as visited and add it to the path
#     visited.add(current)
#     path.append(current)

#     # Check if we reached the end node and have visited all required nodes
#     if current == end and required_nodes.issubset(visited):
#         return path[:]

#     # Variable to store the longest valid path found
#     longest_valid_path = None

#     # Explore neighbors
#     for neighbor in graph[current]:
#         if neighbor not in visited:  # Only visit unvisited nodes
#             result_path = find_required_coverage_path(graph, neighbor, end, required_nodes, visited, path)
#             if result_path:
#                 # Update longest_valid_path if the new path covers more required nodes
#                 if longest_valid_path is None or len(result_path) > len(longest_valid_path):
#                     longest_valid_path = result_path

#     # Backtrack: remove the current node from visited and path
#     visited.remove(current)
#     path.pop()

#     return longest_valid_path

# # Define the adjacency list (graph) as provided
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

# # Define required non-gate nodes that must be visited
# required_nodes = {'体育场', '计算机学科楼', '三食堂', '二食堂', '一食堂', '图书馆', '宿舍楼', '教学楼', '办公楼'}

# # Set the starting and ending gates
# start_gate = '东门'
# end_gate = '北门'

# # Find the path
# required_coverage_path = find_required_coverage_path(graph, start_gate, end_gate, required_nodes)
# print("Path from", start_gate, "to", end_gate, ":", required_coverage_path)
def find_all_paths(graph, current, end, required_nodes, visited=None, path=None, all_paths=None):
    """
    在图中找到所有从当前节点到结束节点的路径，同时确保访问了所有必需的节点。
    
    :param graph: 图的邻接表表示
    :param current: 当前节点
    :param end: 结束节点
    :param required_nodes: 必须访问的节点集合
    :param visited: 已访问的节点集合
    :param path: 当前路径
    :param all_paths: 所有路径的集合
    :return: 包含所有路径的列表
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    # 标记当前节点为已访问，并将其添加到路径中
    visited.add(current)
    path.append(current)

    # 检查是否到达结束节点，并且已访问所有必需的节点
    if current == end and required_nodes.issubset(visited):
        all_paths.append(path[:])
    else:
        # 探索邻居节点
        for neighbor in graph[current]:
            if neighbor not in visited:  # 只访问未访问过的节点
                find_all_paths(graph, neighbor, end, required_nodes, visited, path, all_paths)

    # 回溯：从已访问的节点和路径中移除当前节点
    visited.remove(current)
    path.pop()
    return all_paths

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

# 设置起始和结束的门
gates = ['北门', '南门', '西门', '东门']

# 为所有起始和结束门的组合找到所有路径
all_results = []
for start_gate in gates:
    for end_gate in gates:
        if start_gate != end_gate:
            paths = find_all_paths(graph, start_gate, end_gate, required_nodes)
            for path in paths:
                all_results.append((start_gate, end_gate, path))

# 打印所有结果
for start_gate, end_gate, path in all_results:
    print(f"从{start_gate}到{end_gate}的路径：{path}")

with open('travel.txt', 'w', encoding='utf-8') as file:
    for start_gate, end_gate, path in all_results:
        file.write(f"从{start_gate}到{end_gate}的路径：{' -> '.join(path)}\n")

print("所有路径已写入travel.txt")

input("程序已运行完成，按Enter键退出...")