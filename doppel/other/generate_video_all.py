from fastapi import FastAPI, HTTPException
from zhipuai import ZhipuAI
from user_storage import load_user_info
from page2.communicate import load_role_info
import json

app = FastAPI()
client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF")  # 请填写您的APIKey

# 加载场景描述、图片和对话记录
def load_scenario(file_path='scenario.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("场景文件不存在。")
        return None

def load_conversation_log(file_path='conversation_log.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f).get("conversation", [])
    except FileNotFoundError:
        print("对话记录文件不存在。")
        return []

# 保存生成的视频信息
def save_video_info(video_info, file_path='video_info.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(video_info, f, ensure_ascii=False, indent=4)

@app.post("/generate-video")
async def generate_video():
    user_info = load_user_info()
    role_info = load_role_info()
    scenario = load_scenario()
    conversation = load_conversation_log()

    if not user_info or not role_info or not scenario:
        raise HTTPException(status_code=400, detail="缺少用户信息、角色信息或场景信息。")

    # 构建视频生成的描述
    video_prompt = (
        f"这是一个以{user_info['name']}和{role_info['role_name']}为主角的场景。"
        f"{scenario['scenario_description']}。场景图像展示了{scenario['scenario_url']}。"
        f"对话内容为：{' '.join([f'{item['role']}说：“{item['content']}”' for item in conversation])}。"
    )

    try:
        # 请求智谱API生成视频
        response = client.videos.generations(
            model="cogvideox",
            prompt=video_prompt
        )

        video_id = response.id

        # 查询视频生成状态
        video_result = client.videos.retrieve_videos_result(id=video_id)

        # 检查任务状态
        if video_result['task_status'] == "SUCCESS":
            video_url = video_result['video_result'][0]['url']
            cover_image_url = video_result['video_result'][0]['cover_image_url']

            video_info = {
                "video_id": video_id,
                "status": "SUCCESS",
                "video_url": video_url,
                "cover_image_url": cover_image_url
            }

            # 保存视频信息
            save_video_info(video_info)

            return {"video_url": video_url, "cover_image_url": cover_image_url}
        else:
            return {"status": video_result['task_status'], "message": "视频生成处理中，请稍后查询。"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成视频时出错: {str(e)}")

# 启动应用的入口点
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
