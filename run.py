# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
nd = search.GPSProblem('N', 'D'
                       , search.romania)
mf = search.GPSProblem('M', 'F'
                       , search.romania)

print("\n------------------Breadth Search----------------")
print(search.breadth_first_graph_search(ab).path())
print(search.breadth_first_graph_search(oe).path())
print(search.breadth_first_graph_search(gz).path())
print(search.breadth_first_graph_search(nd).path())
print(search.breadth_first_graph_search(mf).path())

print("\n------------------Depth Search------------------")
print(search.depth_first_graph_search(ab).path())
print(search.depth_first_graph_search(oe).path())
print(search.depth_first_graph_search(gz).path())
print(search.depth_first_graph_search(nd).path())
print(search.depth_first_graph_search(mf).path())

print("\n------------------Search in Branching and Bounding------------------")
print(search.branch_and_bound(ab).path())
print(search.branch_and_bound(oe).path())
print(search.branch_and_bound(gz).path())
print(search.branch_and_bound(nd).path())
print(search.branch_and_bound(mf).path())

print('\n------------------Search in Branching and Bounding with Heuristics------------------')
print(search.branch_and_bound_heuristic(ab).path())
print(search.branch_and_bound_heuristic(oe).path())
print(search.branch_and_bound_heuristic(gz).path())
print(search.branch_and_bound_heuristic(nd).path())
print(search.branch_and_bound_heuristic(mf).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, !<Node A>] : 211 + 99 + 140 = 450

