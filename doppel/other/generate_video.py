from zhipuai import ZhipuAI
client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF") # 请填写您自己的APIKey

response = client.videos.generations(
    model="cogvideox",
    prompt="浩然和经瑞在清华大学校园里的咖啡厅开心得聊着创业的未来。"
)
print(response)