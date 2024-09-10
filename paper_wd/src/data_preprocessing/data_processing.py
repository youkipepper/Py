import pandas as pd
import numpy as np

def filter_data(df, column_name, z_threshold= 2, filter_step= 100, same_threshold=20):
    value_counts = df[column_name].value_counts()
    values_to_filter = value_counts[value_counts > same_threshold].index

    # 初始化过滤后的索引
    filtered_indices = []

    # 分段处理
    for start in range(0, len(df), filter_step):
        end = start + filter_step
        subset = df.iloc[start:end]

        # 计算Z分数
        mean = subset[column_name].mean()
        std = subset[column_name].std()

        if std == 0:  # 防止标准差为0时出错
            z_scores = np.zeros_like(subset[column_name], dtype=float)
        else:
            z_scores = np.abs((subset[column_name] - mean) / std)

        # 筛除异常值
        subset_filtered = subset[z_scores < z_threshold]

        # 筛除出现次数超过阈值的值
        subset_filtered = subset_filtered[~subset_filtered[column_name].isin(values_to_filter)]

        filtered_indices.extend(subset_filtered.index)

    return df.loc[filtered_indices]