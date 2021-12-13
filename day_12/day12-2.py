# Takes liberal inspiration from: https://www.python.org/doc/essays/graphs/
def count_paths(_graph, _start, _end, path=[], repeated_cave = ''):
    path = path + [_start]
    path_count = 0

    if _start == _end:  # recursion base case
        #print(f"Path: {path}")
        return 1

    else:
        for node in _graph[_start]:
            if node.isupper() or (node not in path):
                path_count += count_paths(_graph, node, _end, path, repeated_cave)
            elif node in path and repeated_cave == '' and (node != 'start' and node != 'end'):
                path_count += count_paths(_graph, node, _end, path, node)
            else:
                #print(f"Dead end: {path + [node]}")
                path_count += 0
    
    return path_count

file = open("day_12_input.txt", "r")
data = file.read().strip().split("\n")

# Build Map Graph Data Structure
graph = dict()
for line in data:
    _src_node, _dst_node = line.split('-')

    if _src_node not in graph:
        graph[_src_node] = [_dst_node]
    else:
        graph[_src_node].append(_dst_node)

    if _dst_node not in graph:
        graph[_dst_node] = [_src_node]
    else:
        graph[_dst_node].append(_src_node)
# for k in graph:
#     print(f"{k} connects to {graph[k]}")

final_count_paths = count_paths(graph, "start", "end")
print(f"Number unique paths: {final_count_paths}")

file.close()