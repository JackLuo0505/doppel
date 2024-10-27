from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# 初始化FastAPI应用
app = FastAPI()

# 定义用户数据模型
class UserInfo(BaseModel):
    # 基础信息模块
    age: int  # 年龄
    occupation: str  # 职业和工作领域
    username: str  # 用户名
    gender: str  # 性别（男、女、其他）
    
    # 个性特征模块
    social_type: str  # 社交类型（内向、外向、两者皆有）
    communication_tendency: str  # 沟通倾向（主动或被动）
    communication_style: str  # 沟通风格（理性、感性、幽默）
    decision_making_style: str  # 决策风格（快速决定、深思熟虑、视情况而定）

    # 兴趣爱好模块
    interests: str  # 主要兴趣爱好（阅读、电影、运动等）
    preferred_topics: str  # 关注的新闻或信息类型（科技、娱乐等）
    favorite_activity: str  # 最喜欢的活动或消遣方式
    social_activity_frequency: bool  # 是否经常参加社交活动或线上交流

    # 沟通偏好模块
    language_preference: str  # 日常沟通语言偏好（正式、随意、幽默、专业等）
    response_preference: str  # 回复偏好（长篇大论或简洁）
    use_of_emojis: bool  # 是否倾向于添加表情、图片或GIF
    conflict_response: str  # 矛盾时的反应（冷静处理、直接表达、回避）
    sharing_preference: str  # 更喜欢主动分享或倾听他人观点

    # 情绪管理与表达模块
    mood_exposure: str  # 情绪的外显程度（外露或内敛）
    negative_mood_management: str  # 负面情绪处理方式（自我调节、向他人寻求帮助）
    emotion_trigger_topics: str  # 容易情绪波动的话题类型（工作、家庭等）
    joy_expression: str  # 愉悦的表达方式（笑脸表情、直接表达、幽默语言等）

    # 理想化数字形象偏好模块
    ideal_character_traits: str  # 希望的数字形象特征（冷静、幽默等）
    communication_approach: str  # 沟通风格倾向（务实或创意）
    situation_based_style: bool  # 不同场合下是否希望风格有所差异
    response_frequency: str  # 数字形象的沟通频率（尽可能多回复、只在重要时刻回复）

    # 隐私与数据安全偏好模块
    data_review_preference: bool  # 是否愿意定期审查和管理数据使用情况
    data_use_notification: bool  # 是否希望每次使用数据时收到通知
    anonymous_data_contribution: bool  # 是否愿意提供匿名数据以帮助改善产品
    data_retention_policy: bool  # 是否希望对数据的存储时限有具体设定

# 保存用户信息到本地
def save_user_info(user_info: UserInfo, file_path='user_info.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(user_info.dict(), f, ensure_ascii=False, indent=4)

# 读取本地存储的用户信息
def load_user_info(file_path='user_info.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("用户信息文件不存在，请先保存用户信息。")
        return None

# 定义API接口
@app.post("/save-user-info")
async def save_user_info_api(user_info: UserInfo):
    try:
        save_user_info(user_info)
        return {"message": "用户信息保存成功"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"保存用户信息时出错: {str(e)}")

# 启动应用的入口点
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)