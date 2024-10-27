from zhipuai import ZhipuAI
client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF") # 请填写您自己的APIKey

response = client.videos.retrieve_videos_result(
    id="377317298370411329145797884156638518"
)
print(response)