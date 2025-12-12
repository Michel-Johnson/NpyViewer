'''
Author: Michel-Johnson           micheljohnsonofficial@gmail.com
Date: 2025-12-13 00:31:27
LastEditors: Michel-Johnson      micheljohnsonofficial@gmail.com
LastEditTime: 2025-12-13 00:31:38
FilePath: \Desktop\npy_viewer.py
Description: 
Copyright (c) 2025 by Beihang Robotics team, All Rights Reserved. 
'''
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox, Tk

# 隐藏 Tkinter 的主窗口，只用于弹窗
root = Tk()
root.withdraw()

def show_error(title, message):
    messagebox.showerror(title, message)

def visualize_npy(file_path):
    try:
        # 读取 npy 文件
        data = np.load(file_path, allow_pickle=True)
        
        # 获取基本信息
        shape = data.shape
        dtype = data.dtype
        ndim = data.ndim

        # 设置绘图窗口标题
        plt.figure(figsize=(8, 6))
        plt.suptitle(f"File: {os.path.basename(file_path)}\nShape: {shape} | Type: {dtype}", fontsize=10)

        # 根据维度决定如何显示
        if ndim == 1:
            # 1维数据：画曲线图
            plt.plot(data)
            plt.title("1D Array Visualization")
            plt.grid(True)
        
        elif ndim == 2:
            # 2维数据：画热力图/图像
            plt.imshow(data, cmap='viridis', aspect='auto')
            plt.colorbar()
            plt.title("2D Array Visualization")
        
        elif ndim >= 3:
            # 3维及以上：显示第一个切片（通常是图像批次或通道）
            # 这里为了通用性，取最后两个维度显示，前面的维度取第0个索引
            slice_data = data
            while slice_data.ndim > 2:
                slice_data = slice_data[0]
            
            plt.imshow(slice_data, cmap='viridis', aspect='auto')
            plt.colorbar()
            plt.title(f"Multi-D Array (Showing slice [0...])")

        else:
            # 0维标量
            plt.text(0.5, 0.5, str(data), fontsize=20, ha='center')
            plt.title("Scalar Value")

        plt.show()

    except Exception as e:
        show_error("Error", f"Failed to open .npy file:\n{str(e)}")

if __name__ == "__main__":
    # Windows 双击文件打开时，文件路径会作为第二个参数传入 (sys.argv[1])
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        visualize_npy(file_path)
    else:
        show_error("Warning", "Please run this program by double-clicking a .npy file.")