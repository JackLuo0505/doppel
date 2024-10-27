<template>
  <n-card title="介绍一下你自己(以马斯克为例)" embedded>
    <n-form>
      <!-- 基本信息 -->
      <n-form-item label="您的年龄是？">
        <n-input-number v-model:value="formData.age" placeholder="请输入您的年龄" />
      </n-form-item>

      <n-form-item label="您的职业和工作领域是？">
        <n-input v-model:value="formData.occupation" placeholder="请输入您的职业和工作领域" />
      </n-form-item>

      <!-- 个性特征模块 -->
      <n-form-item label="请描述您的性格特点">
        <n-input v-model:value="formData.personality" placeholder="请输入您的性格特点" />
      </n-form-item>

      <n-form-item label="您认为自己在社交中属于以下哪种类型？">
        <n-radio-group v-model:value="formData.socialType">
          <n-radio value="内向">内向</n-radio>
          <n-radio value="外向">外向</n-radio>
          <n-radio value="两者皆有">两者皆有</n-radio>
        </n-radio-group>
      </n-form-item>

      <n-form-item label="您在沟通时是否倾向于主动还是被动？">
        <n-radio-group v-model:value="formData.communicationApproach">
          <n-radio value="主动">主动</n-radio>
          <n-radio value="被动">被动</n-radio>
        </n-radio-group>
      </n-form-item>

      <n-form-item label="您的沟通风格是偏理性、感性、还是幽默？">
        <n-radio-group v-model:value="formData.communicationStyle">
          <n-radio value="理性">理性</n-radio>
          <n-radio value="感性">感性</n-radio>
          <n-radio value="幽默">幽默</n-radio>
        </n-radio-group>
      </n-form-item>

      <!-- 兴趣爱好模块 -->
      <n-form-item label="您的主要兴趣爱好是什么？">
        <n-checkbox-group v-model:value="formData.hobbies">
          <n-checkbox value="阅读">阅读</n-checkbox>
          <n-checkbox value="运动">运动</n-checkbox>
          <n-checkbox value="物理">物理</n-checkbox>
          <n-checkbox value="音乐">音乐</n-checkbox>
          <n-checkbox value="编程">编程</n-checkbox>
          <n-checkbox value="探索">探索</n-checkbox>
        </n-checkbox-group>
      </n-form-item>

      <n-form-item label="您最喜欢的活动或消遣方式是什么？">
        <n-input v-model:value="formData.favoriteActivity" placeholder="请输入您的喜好" />
      </n-form-item>

      <!-- 沟通偏好模块 -->
      <n-form-item label="您的日常沟通语言偏好是？">
        <n-radio-group v-model:value="formData.communicationTone">
          <n-radio value="正式">正式</n-radio>
          <n-radio value="随意">随意</n-radio>
          <n-radio value="幽默">幽默</n-radio>
          <n-radio value="专业">专业</n-radio>
        </n-radio-group>
      </n-form-item>

      <n-form-item label="您更喜欢主动分享还是倾听他人的观点？">
        <n-radio-group v-model:value="formData.sharingPreference">
          <n-radio value="主动分享">主动分享</n-radio>
          <n-radio value="倾听他人">倾听他人</n-radio>
        </n-radio-group>
      </n-form-item>

      <!-- 情绪管理与表达模块 -->
      <n-form-item label="您认为自己的表达风格？">
        <n-radio-group v-model:value="formData.emotionalExpression">
          <n-radio value="表达风格相对严肃">情绪外露</n-radio>
          <n-radio value="表达风格相对活泼">表达内敛</n-radio>
        </n-radio-group>
      </n-form-item>

      <n-form-item label="您在与人沟通时如何表达愉悦？">
        <n-input
          v-model:value="formData.happyExpression"
          placeholder="例如：笑脸表情、直接表达、幽默语言等" />
      </n-form-item>
      <n-form-item>
        <n-button type="primary" @click="handleSubmit">生成数字肖像</n-button>
      </n-form-item>
    </n-form>
  </n-card>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useFormDataStore } from '@/store';
const formDataStore = useFormDataStore();
const formData = ref({
  age: 24,
  occupation: '企业家',
  personality: '外向',
  socialType: '外向',
  communicationApproach: '主动',
  communicationStyle: '理性',
  socialPreference: '热爱交流社交',
  hobbies: ['编程', '探索', '物理'],
  favoriteActivity: '科技, 太空探索',
  communicationTone: '正式',
  sharingPreference: '主动分享',
  emotionalExpression: '表达风格相对严肃',
  happyExpression: '直接表达',
  other: '一个二十岁的企业家,热爱创新,热衷科技'
});

const router = useRouter();
const handleSubmit = () => {
  console.log('点击了提交按钮');
  console.log('formData:', formData.value);
  // Store the form data in Pinia
  formDataStore.setFormData(formData.value);

  // Navigate to the next route without passing data via params or query
  router.push({ name: 'PersonMap' });
};
</script>
