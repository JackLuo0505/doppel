
from pydantic import BaseModel
from zhipuai import ZhipuAI
import os

# 初始化FastAPI应用

client = ZhipuAI(api_key="9b5eb901b1e92e9a749bfbda59def0d5.bv37HUooK5YLNNKF") # 请填写您自己的APIKey

class Questionnaire(BaseModel):
    name: str
    age: int
    preferences: str
    personality: str
    purpose: str

def generate_scenario(questionnaire: Questionnaire):
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
        messages=[
            {"role": "system", "content": "作为一名设计师与作家，请协助我创造符合我形象与目的的社交场景描述"},
            {"role": "user", "content": f"我叫{questionnaire.name},{questionnaire.age}岁，我的性格是{questionnaire.personality}, 我喜欢{questionnaire.preferences}，我社交的目的是{questionnaire.preferences}，请创造一个适合我社交目的的场景文字描述。"},
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


# 测试函数
def main():
    # 创建测试数据
    test_questionnaire = Questionnaire(
        name="Alice",
        age=25,
        preferences="阅读, 旅游, 听音乐",
        personality="外向和开朗",
        purpose="寻找志同道合的旅游伙伴"
    )

    # 调用生成场景函数并打印结果
    result = generate_scenario(test_questionnaire)
    print("场景描述:", result["scenario_description"])
    print("场景图片URL:", result["scenario_url"])
 
if __name__ == "__main__":
    main()