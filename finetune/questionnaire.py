from pydantic import BaseModel
from zhipuai import ZhipuAI
import os

# 初始化FastAPI应用

client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF")  # 请填写您自己的APIKey

# 定义完整的问卷数据模型
class Questionnaire(BaseModel):
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

def generate_scenario(questionnaire: Questionnaire):
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
        messages=[
            {"role": "system", "content": "作为一名设计师与作家，请协助我创造符合我形象与目的的社交场景描述"},
            {"role": "user", "content": f"我的用户名是{questionnaire.username}，今年{questionnaire.age}岁，职业是{questionnaire.occupation}。"
                                         f"在社交中，我偏向于{questionnaire.social_type}，沟通倾向{questionnaire.communication_tendency}，沟通风格是{questionnaire.communication_style}，"
                                         f"决策方式则是{questionnaire.decision_making_style}。我的兴趣爱好包括{questionnaire.interests}，"
                                         f"经常关注{questionnaire.preferred_topics}类型的信息，最喜欢的活动是{questionnaire.favorite_activity}，"
                                         f"{'经常' if questionnaire.social_activity_frequency else '不太'}参加社交活动。"
                                         f"在沟通上，我偏好使用{questionnaire.language_preference}的语言风格，更喜欢{questionnaire.response_preference}的回复方式，"
                                         f"{'会' if questionnaire.use_of_emojis else '不会'}使用表情符号，并在面对矛盾时倾向于{questionnaire.conflict_response}，"
                                         f"分享倾向于{questionnaire.sharing_preference}。情绪方面，我较{questionnaire.mood_exposure}，在负面情绪时倾向于{questionnaire.negative_mood_management}，"
                                         f"容易因{questionnaire.emotion_trigger_topics}话题而情绪波动，愉悦时会用{questionnaire.joy_expression}表达。"
                                         f"我的理想数字形象应具备{questionnaire.ideal_character_traits}特征，沟通风格倾向于{questionnaire.communication_approach}，"
                                         f"{'在不同场合下希望风格有所差异' if questionnaire.situation_based_style else '不希望风格改变'}。"
                                         f"此外，我希望数字形象的回复频率为{questionnaire.response_frequency}。关于数据隐私，我{'希望' if questionnaire.data_review_preference else '不希望'}定期审查数据使用，"
                                         f"{'希望' if questionnaire.data_use_notification else '不需要'}每次使用数据时通知，{'愿意' if questionnaire.anonymous_data_contribution else '不愿意'}提供匿名数据，"
                                         f"{'希望' if questionnaire.data_retention_policy else '不要求'}对数据的存储时限有具体设定。请创造一个适合我社交目的的场景文字描述。"},
        ],
    )

    # 获取生成的场景描述
    scenario_description = response.choices[0].message

    response = client.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=f"请生成符合这个场景描述的场景图：{scenario_description}",
    )

    scenario_url = response.data[0].url

    output = {
        "scenario_description": scenario_description,
        "scenario_url": scenario_url
    }

    # 返回
    return output

# 测试函数
def main():
    # 创建测试数据
    test_questionnaire = Questionnaire(
        age=25,
        occupation="软件工程师",
        username="Alice",
        gender="女",
        social_type="外向",
        communication_tendency="主动",
        communication_style="幽默",
        decision_making_style="快速决定",
        interests="阅读, 旅游, 听音乐",
        preferred_topics="科技, 娱乐",
        favorite_activity="旅行",
        social_activity_frequency=True,
        language_preference="正式",
        response_preference="简洁",
        use_of_emojis=True,
        conflict_response="冷静处理",
        sharing_preference="倾听",
        mood_exposure="内敛",
        negative_mood_management="自我调节",
        emotion_trigger_topics="工作, 朋友",
        joy_expression="笑脸表情",
        ideal_character_traits="乐观, 热情",
        communication_approach="创意",
        situation_based_style=True,
        response_frequency="尽可能多回复",
        data_review_preference=True,
        data_use_notification=True,
        anonymous_data_contribution=True,
        data_retention_policy=True
    )

    # 调用生成场景函数并打印结果
    result = generate_scenario(test_questionnaire)
    print("场景描述:", result["scenario_description"])
    print("场景图片URL:", result["scenario_url"])

if __name__ == "__main__":
    main()
