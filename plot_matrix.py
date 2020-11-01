import numpy as np
import matplotlib.pyplot as plt


"""
作业热身题，目的是熟悉github classroom的操作流程
"""


def generate_random_matrix(m, n):
    """生成一个m*n的二值矩阵，元素值为0,1"""
    matrix = np.random.randint(0, 2, (m, n))
    return matrix


def save_matrix(matrix, file_name):
    """将矩阵保存为图片"""
    plt.imsave(file_name, matrix, cmap='gray')


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
