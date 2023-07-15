import numpy as np
from mpi4py import MPI

# 初始化MPI通信
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    assert(cols_A == rows_B)

    # 定义划分方式
    block_size = rows_A // size  # 每个进程处理的行数

    # 划分矩阵 A 的行，并发送到各个进程
    A_block = np.zeros((block_size, cols_A))
    comm.Scatter(A, A_block, root=0)

    # 广播矩阵 B 到所有进程
    comm.Bcast(B, root=0)

    # 计算每个进程的局部矩阵 C_local
    C_local = np.dot(A_block, B)

    # 收集所有进程计算得到的局部矩阵 C_local 到主进程上
    C = None
    if rank == 0:
        C = np.zeros((rows_A, cols_B))
    comm.Gather(C_local, C, root=0)

    return C

# 创建两个矩阵 A 和 B，只在主进程上生成
if rank == 0:
    rows_A = 100
    cols_A = 50
    rows_B = 50
    cols_B = 200
    A = np.random.rand(rows_A, cols_A)
    B = np.random.rand(rows_B, cols_B)
else:
    A = None
    B = None

# 并行计算矩阵相乘
C = matrix_multiply(A, B)

# 打印主进程上的最终结果 C，只在主进程上打印
if rank == 0:
    print("Matrix C:")
    print(C)
