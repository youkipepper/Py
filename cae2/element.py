import numpy as np
import matplotlib.pyplot as plt
import gmsh

def generate_cantilever_beam_mesh(length, height, num_elements_x, num_elements_y):
    gmsh.initialize()
    gmsh.model.add("cantilever_beam")

    lc = 0.05  # 网格划分的特征长度

    # 创建节点
    gmsh.model.geo.addPoint(0, 0, 0, lc, 1)         
    gmsh.model.geo.addPoint(length, 0, 0, lc, 2)    
    gmsh.model.geo.addPoint(length, height, 0, lc, 3)
    gmsh.model.geo.addPoint(0, height, 0, lc, 4)    

    # 创建线段
    gmsh.model.geo.addLine(1, 2, 1)     
    gmsh.model.geo.addLine(2, 3, 2)     
    gmsh.model.geo.addLine(3, 4, 3)     
    gmsh.model.geo.addLine(4, 1, 4)     

    # 创建线环
    gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)

    # 创建平面
    gmsh.model.geo.addPlaneSurface([1], 1)

    # 生成网格
    gmsh.model.mesh.generate(2)

    # 获取网格数据
    nodes = gmsh.model.mesh.getNodes()
    elements = gmsh.model.mesh.getElements(2, 2)[1]  # 注意这里的 [1]

    gmsh.finalize()
    
    nodes = np.array(nodes)
    elements = np.array(elements)
    return nodes[:, 1:4], elements[:, 1:]

# 参数
length = 10.0
height = 2.0
num_elements_x = 20
num_elements_y = 5

# 生成网格
nodes, elements = generate_cantilever_beam_mesh(length, height, num_elements_x, num_elements_y)

# 可视化（可选）
plt.figure(figsize=(10, 5))
for elem in elements:
    elem_nodes = nodes[elem - 1, :]
    elem_nodes = np.vstack((elem_nodes, elem_nodes[0]))
    plt.plot(elem_nodes[:, 0], elem_nodes[:, 1], 'b-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('生成的网格：悬臂梁')
plt.show()
