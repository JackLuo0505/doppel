import json

def preprocess_chat_data(input_file):
    # Placeholder implementation for preprocessing chat data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    cleaned_data = [line.strip() for line in data if line.strip()]
    return cleaned_data

def save_preprocessed_data(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            json_line = json.dumps({"text": entry}, ensure_ascii=False)
            f.write(json_line + '\n')

# 示例使用
if __name__ == '__main__':
    cleaned_data = preprocess_chat_data('uploaded_data/example_chat.txt')
    save_preprocessed_data(cleaned_data, 'processed_data.jsonl')
