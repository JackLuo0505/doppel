export const system_prompt = `
提示词:生成一个嵌套的 JSON 数据结构,表示思维导图的层级关系。根节点应包含 name 属性,代表节点名称。每个节点可以包含以下属性:

name:节点的名称。
children:一个包含子节点的数组,表示节点的子层级。每个子节点也应遵循相同的结构,包含 name 和 children 属性。
left(可选）:布尔值属性。如果节点应左对齐,请设置 "left": true。
下面是一个示例 JSON 数据结构:
{
  "name": "如何学习web前端",
  "children": [
    {
      "name": "预备知识",
      "children": [
        { "name": "HTML & CSS" },
        { "name": "JavaScript" }
      ]
    },
    {
      "name": "进阶",
      "children": [
        { "name": "学习vue" }
      ]
    },
    {
      "name": "进阶",
      "left": true
    }
  ]
}

`;
