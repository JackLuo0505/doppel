from flask import Flask, request, jsonify
import os
import re

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "没有文件上传"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "文件名为空"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # 对数据进行预处理
    cleaned_data = preprocess_chat_data(file_path)

    return jsonify({"message": "文件上传成功", "cleaned_data": cleaned_data}), 200

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
