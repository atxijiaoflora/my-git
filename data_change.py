input_file = r"F:\Practice\45-45000-20260311-2.se5"
output_file = r"F:\Practice\45-45000-20260311-2_new.se5"

with open(input_file, "r", encoding="utf-8") as f_read, \
        open(output_file, "w", encoding="utf-8") as f_write:
    # 读取并写入第 1 行表头
    header = f_read.readline()
    f_write.write(header)

    # 读取并写入第 2 行列名（不做修改）
    column_names = f_read.readline()
    f_write.write(column_names)

    # 遍历剩余的所有数据行（从第 3 行开始）
    for line in f_read:
        line = line.strip()
        # 跳过空行
        if not line:
            continue
        # 按逗号分割列
        cols = line.split(",")
        # 只对数据行做数值计算
        cols[1] = str(float(cols[1]) / 100)  # 第二列 ru81 ÷100
        cols[2] = str(float(cols[2]) * 4)  # 第三列 ru07 ×4
        # 重新拼接并写入
        new_line = ",".join(cols) + "\n"
        f_write.write(new_line)

print("✅ 修改完成！新文件已生成：", output_file)

