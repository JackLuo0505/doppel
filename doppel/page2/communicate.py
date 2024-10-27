from zhipuai import ZhipuAI
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)
from user_storage import load_user_info
import json

# 初始化ZhipuAI客户端
client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF")  # 请替换为您的APIKey

# 加载对话角色信息
def load_role_info(file_path='roles.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("角色信息文件不存在。")
        return None

# 保存对话记录
def save_conversation_log(conversations, file_path='all_conversations.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"conversations": conversations}, f, ensure_ascii=False, indent=4)

def multi_dialogue():
    user_info = load_user_info()
    role_infos = load_role_info()

    if not user_info or not role_infos:
        print("用户信息或角色信息未找到。")
        return

    all_conversations = []

    for role in role_infos:
        role_name = role['role_name']
        role_description = role['description']

        conversation = [
            {"role": "user", "content": f"您好，{role_name}！"},
            {"role": role_name, "content": f"您好，{user_info['name']}，很高兴见到您！"}
        ]

        try:
            response = client.chat.completions.create(
                model="charglm-3",
                meta={
                    "user_info": (
                        f"我叫{user_info.username}，今年{user_info.age}岁，职业是{user_info.occupation}。"
                                         f"在社交中，我偏向于{user_info.social_type}，沟通倾向{user_info.communication_tendency}，沟通风格是{user_info.communication_style}，"
                                         f"决策方式则是{user_info.decision_making_style}。我的兴趣爱好包括{user_info.interests}，"
                                         f"经常关注{user_info.preferred_topics}类型的信息，最喜欢的活动是{user_info.favorite_activity}，"
                                         f"{'经常' if user_info.social_activity_frequency else '不太'}参加社交活动。"
                                         f"在沟通上，我偏好使用{user_info.language_preference}的语言风格，更喜欢{user_info.response_preference}的回复方式，"
                                         f"{'会' if user_info.use_of_emojis else '不会'}使用表情符号，并在面对矛盾时倾向于{user_info.conflict_response}，"
                                         f"分享倾向于{user_info.sharing_preference}。情绪方面，我较{user_info.mood_exposure}，在负面情绪时倾向于{user_info.negative_mood_management}，"
                                         f"容易因{user_info.emotion_trigger_topics}话题而情绪波动，愉悦时会用{user_info.joy_expression}表达。"
                                         f"我的理想数字形象应具备{user_info.ideal_character_traits}特征，沟通风格倾向于{user_info.communication_approach}，"
                                         f"{'在不同场合下希望风格有所差异' if user_info.situation_based_style else '不希望风格改变'}。"
                                         f"此外，我希望数字形象的回复频率为{user_info.response_frequency}。关于数据隐私，我{'希望' if user_info.data_review_preference else '不希望'}定期审查数据使用，"
                                         f"{'希望' if user_info.data_use_notification else '不需要'}每次使用数据时通知，{'愿意' if user_info.anonymous_data_contribution else '不愿意'}提供匿名数据，"
                                         f"{'希望' if user_info.data_retention_policy else '不要求'}对数据的存储时限有具体设定。请创造一个适合我社交目的的场景文字描述。"
                    ),
                    "bot_info": role_description,
                    "bot_name": role_name,
                    "user_name": user_info['name']
                },
                messages=conversation
            )

            # 添加生成的消息到对话中
            conversation.append({"role": role_name, "content": response.choices[0].message})

            # 将此对话记录保存到总对话列表中
            all_conversations.append({
                "role": role_name,
                "conversation": conversation
            })

        except Exception as e:
            print(f"与{role_name}对话时出错: {str(e)}")
            continue

    # 保存所有对话记录
    save_conversation_log(all_conversations)
    print(f"所有对话已生成并保存，总共与 {len(all_conversations)} 个角色进行了对话。")

if __name__ == "__main__":
    multi_dialogue()
