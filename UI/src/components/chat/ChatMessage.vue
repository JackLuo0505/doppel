<template>
  <div class="chat-container flex flex-col p-5 max-w-[80%] m-auto">
    <div v-for="(message, index) in messages" :key="index" class="mt-3">
      <ChatBubble :content="message.content" :position="message.position" />
    </div>

    <chat-input :send-message="sendMessage" v-model:chat-message="chatMessage" />
  </div>
</template>

<script setup lang="ts">
import ChatBubble from '@/components/chat/ChatBubble.vue';
import { useMessageStore } from '@/store';

const messageStore = useMessageStore();

const messages = messageStore.messages;

const chatMessage = ref<string>('');
const message = useMessage();
import { openai } from '@/utils';
// 发送消息逻辑
const sendMessage = async () => {
  if (!chatMessage.value) {
    message.error('消息不能为空');
    return;
  }

  // 将用户消息添加到右侧消息列表
  messageStore.addMessage({ content: chatMessage.value, position: 'right' });

  // 清空输入框
  chatMessage.value = '';

  // 调用 AI 回复逻辑
  await replyMessage();
};

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
        { role: 'system', content: '你是一个AI,回答我的问题!' },
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
  }
};
</script>
