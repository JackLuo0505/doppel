import re

# 数据预处理函数
def preprocess_chat_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    cleaned_data = []
    for line in data:
        # 去除特殊符号和多余空格
        cleaned_line = re.sub(r'[^\w\s]', '', line).strip()
        if cleaned_line:
            cleaned_data.append(cleaned_line)

    return cleaned_data

# 示例使用
if __name__ == '__main__':
    file_path = 'uploaded_data/example_chat.txt'
    cleaned_data = preprocess_chat_data(file_path)
    for line in cleaned_data:
        print(line)
