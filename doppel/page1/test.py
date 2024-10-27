from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from zhipuai import ZhipuAI
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)
from user_storage import load_user_info

# 初始化FastAPI应用
app = FastAPI()

client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF") # 请填写您自己的APIKey

def generate_scenario():
    user_info = load_user_info()
    try:
        response = client.chat.completions.create(
            model="glm-4-plus",  # 请填写您要调用的模型名称
            messages=[
                {"role": "system", "content": "作为一名设计师与作家，请协助我创造符合我形象与目的的社交场景描述"},
                {"role": "user", "content": f"""我叫{user_info['username']}，今年{user_info['age']}岁，职业是{user_info['occupation']}。
                        在社交中，我偏向于{user_info['social_type']}，沟通倾向{user_info['communication_tendency']}，沟通风格是{user_info['communication_style']}，
                        决策方式则是{user_info['decision_making_style']}。我的兴趣爱好包括{user_info['interests']}，
                        经常关注{user_info['preferred_topics']}类型的信息，最喜欢的活动是{user_info['favorite_activity']}，
                        {'经常' if user_info['social_activity_frequency'] else '不太'}参加社交活动。
                        在沟通上，我偏好使用{user_info['language_preference']}的语言风格，更喜欢{user_info['response_preference']}的回复方式，
                        {'会' if user_info['use_of_emojis'] else '不会'}使用表情符号，并在面对矛盾时倾向于{user_info['conflict_response']}，
                        分享倾向于{user_info['sharing_preference']}。情绪方面，我较{user_info['mood_exposure']}，在负面情绪时倾向于{user_info['negative_mood_management']}，
                        容易因{user_info['emotion_trigger_topics']}话题而情绪波动，愉悦时会用{user_info['joy_expression']}表达。
                        我的理想数字形象应具备{user_info['ideal_character_traits']}特征，沟通风格倾向于{user_info['communication_approach']}，
                        {'在不同场合下希望风格有所差异' if user_info['situation_based_style'] else '不希望风格改变'}。
                        此外，我希望数字形象的回复频率为{user_info['response_frequency']}。关于数据隐私，我{'希望' if user_info['data_review_preference'] else '不希望'}定期审查数据使用，
                        {'希望' if user_info['data_use_notification'] else '不需要'}每次使用数据时通知，{'愿意' if user_info['anonymous_data_contribution'] else '不愿意'}提供匿名数据，
                        {'希望' if user_info['data_retention_policy'] else '不要求'}对数据的存储时限有具体设定。请创造一个适合我社交目的的场景文字描述。"""},
            ],
        )

        # 获取生成的场景描述
        scenario_description = response.choices[0].message

        response = client.images.generations(
            model="cogview-3-plus", #填写需要调用的模型编码
            prompt=f"请生成符合这个场景描述的场景图：{scenario_description}",
        )

        scenario_url = response.data[0].url

        output = {
            "scenario_description": scenario_description,
            "scenario_url": scenario_url
        }

        # 返回
        return output
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating scenario: {str(e)}")

if __name__ == "__main__":
    print(generate_scenario())