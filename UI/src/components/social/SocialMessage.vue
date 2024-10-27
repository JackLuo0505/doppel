<template>
  <div class="chat-container flex flex-col p-5 max-w-[80%] m-auto">
    <div v-for="(message, index) in messages" :key="index" class="mt-3">
      <ChatBubble :content="message.content" :position="message.position" />
    </div>

    <!-- <chat-input :send-message="sendMessage" v-model:chat-message="chatMessage" /> -->
  </div>
</template>

<script setup lang="ts">
import ChatBubble from '@/components/chat/ChatBubble.vue';
import { useMessageStore } from '@/store';
let index: number = 0;

const messageStore = useMessageStore();

const messages = messageStore.messages;

const message = useMessage();
import { openai } from '@/utils';
import { getSystemPrompt } from './chatPrompt';
const nextMessage = ref<boolean>(true);
const replyMessage = async () => {
  if (messageStore.messages.length === 0) {
    message.error('无有效消息');
    return;
  }

  // 添加一条初始的空白 AI 回复消息
  const aiMessageIndex = messageStore.messages.length;
  messageStore.addMessage({ content: 'AI 正在输入...', position: 'left' });

  try {
    const stream = await openai.chat.completions.create({
      model: 'deepseek-chat',
      messages: [
        { role: 'system', content: getSystemPrompt() },
        { role: 'user', content: messageStore.messages[aiMessageIndex - 1].content }
      ],
      stream: true
    });

    let aiResponse = '';

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        aiResponse += chunk.choices[0].delta.content;
        messageStore.updateMessageContent(aiMessageIndex, aiResponse);
      }
    }
  } catch (error) {
    message.error('AI回复失败');
    console.error('AI 请求出错:', error);
  } finally {
    setTimeout(() => {
      nextMessage.value = true;
    }, 500);
  }
};

const candidateMessage: string[] = [
  '最近有个新出的VR体验,听说特别逼真。想一起去感受下未来的科技世界吗?',
  '听说电影院新上了4D科幻大片,沉浸感超强。有没有兴趣今晚一起去体验一下？',
  '看到有家咖啡馆推出了AI点单系统,不知道好不好用,要不要晚上一起去试试,感受一下智能服务?'
];
const sendMessage = async () => {
  if (!nextMessage.value) {
    return;
  }
  const length = candidateMessage.length;
  if (index >= length) {
    return;
  }
  messageStore.addMessage({ content: candidateMessage[index], position: 'right' });
  index++;
  nextMessage.value = false;

  await replyMessage();
};
// 发送消息逻辑
onMounted(() => {
  sendMessage();
});
watchEffect(() => {
  if (nextMessage.value) {
    sendMessage();
  }
});
</script>
