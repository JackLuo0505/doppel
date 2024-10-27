<template>
  <div class="mindmap-container">
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <div class="loading-text">正在生成人物肖像...</div>
    </div>
    <n-flex justify="center">
      <n-gradient-text :size="24">以下为你的人物肖像</n-gradient-text>
      <n-button v-if="showMindmap" @click="navigateToStatistic">前往匹配</n-button>
    </n-flex>
    <mindmap v-if="showMindmap" :modelValue="mindmapData" key="mindmap" :drag="true"></mindmap>
    <!-- <chat-input v-model:chat-message="chatMessage" :send-message="getAIResponse" /> -->
    <!-- <n-button v-if="showMindmap" @click="navigateToStatistic">前往匹配</n-button> -->
  </div>
</template>

<script setup lang="ts">
import mindmap from 'vue3-mindmap';
import { openai } from '@/utils';
import { system_prompt } from './SelfMapPrompt';
import 'vue3-mindmap/dist/style.css';
import { useFormDataStore } from '@/store';
import { useRouter } from 'vue-router';

// const chatMessage = ref<string>('');
const showMindmap = ref(false);
const isLoading = ref(false);
const router = useRouter();
const navigateToStatistic = () => {
  router.push('/statistic');
};
type MindMapNode = {
  name: string;
  children?: MindMapNode[];
  left?: boolean;
};

const mindmapData = ref<MindMapNode[]>([]);

watchEffect(() => {
  if (mindmapData.value && mindmapData.value.length > 0) {
    showMindmap.value = true;
  } else {
    showMindmap.value = false;
  }
});
const useForm = useFormDataStore();
const getAIResponse = async () => {
  showMindmap.value = false;
  mindmapData.value = [];
  isLoading.value = true;

  const user_prompt = useForm.getFormattedData();
  console.log('用户输入:', user_prompt);
  try {
    const stream = await openai.chat.completions.create({
      model: 'deepseek-chat',
      messages: [
        { role: 'system', content: system_prompt },
        { role: 'user', content: user_prompt }
      ],
      response_format: {
        type: 'json_object'
      },
      stream: true
    });

    let responseText = '';

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        responseText += chunk.choices[0].delta.content;
      }
    }
    console.log('AI回复:', responseText);
    const parsedData = JSON.parse(responseText) as MindMapNode;
    mindmapData.value = [parsedData];
  } catch (error) {
    console.error('获取AI传输流失败:', error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {});
watchEffect(() => {
  getAIResponse();
});
</script>

<style scoped>
.mindmap-container {
  position: relative;
  height: 100vh; /* 使整个组件占满视窗 */
}

/* 确保mindmap组件有足够的显示空间 */
:deep(.vue3-mindmap) {
  width: 100%;
  height: 600px;
  margin: 20px 0;
}

.loading-overlay {
  position: fixed; /* 改成 fixed 使其覆盖整个屏幕 */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100vh; /* 高度改为视窗高度 */
  background-color: rgba(255, 255, 255, 0.9);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-text {
  margin-top: 20px;
  color: #666;
  font-size: 16px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
