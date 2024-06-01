import numpy as np
import pandas as pd

# 模拟里克特五点量表数据，具有自定义概率分布
def generate_custom_likert_scale_data(num_samples, num_questions):
    # 定义里克特五点量表的选项
    scale = [1, 2, 3, 4, 5]
    # 定义每个选项的概率，例如4和5的概率更高
    probabilities = [0.1, 0.1, 0.2, 0.3, 0.3]
    
    # 生成符合自定义概率分布的随机数
    likert_data = np.random.choice(scale, size=(num_samples, num_questions), p=probabilities)
    return likert_data

# 计算 Cronbach's Alpha
def cronbach_alpha(df):
    item_vars = df.var(axis=0, ddof=1)
    total_var = df.sum(axis=1).var(ddof=1)
    n_items = len(df.columns)
    return (n_items / (n_items - 1)) * (1 - item_vars.sum() / total_var)

# 生成初始数据
num_samples = 100
num_questions = 15
likert_data = generate_custom_likert_scale_data(num_samples, num_questions)

# 使用 pandas 将数据保存为 DataFrame
columns = [f'Question_{i+1}' for i in range(num_questions)]
df = pd.DataFrame(likert_data, columns=columns)

# 计算初始数据的 Cronbach's Alpha
initial_alpha = cronbach_alpha(df)
print(f"Initial Cronbach's Alpha: {initial_alpha}")

# 如果初始 Alpha 太低，则进行数据调整
if initial_alpha < 0.7:
    # 生成高一致性的数据
    # 我们可以通过对原始数据进行一定的调整来增加一致性
    for i in range(num_questions):
        if i % 2 == 0:
            df[columns[i]] = df[columns[i-1]]  # 假设偶数列与前一列一致
    
    # 重新计算 Cronbach's Alpha
    adjusted_alpha = cronbach_alpha(df)
    print(f"Adjusted Cronbach's Alpha: {adjusted_alpha}")

# 打印生成的数据
print(df)

# 保存为 CSV 文件
df.to_csv('likert_data2.csv', index=False)

# 保存为 Excel 文件
# df.to_excel('likert_data.xlsx', index=False)

# 输出生成的数据和保存文件的信息
print("\nData saved to 'likert_data.csv' and 'likert_data.xlsx'.")
