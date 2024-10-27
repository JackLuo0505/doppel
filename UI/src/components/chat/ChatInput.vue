<template>
  <n-layout-footer
    style="
      z-index: 10;
      position: fixed;
      bottom: 4rem;
      left: 55%;
      transform: translateX(-50%);
      max-width: 100vw;
      display: flex;
    ">
    <n-space align="center" justify="center" style="width: 100%; display: flex">
      <n-input v-model:value="chatMessage" placeholder="请输入消息" style="flex: 1; margin-right: 8px" />
      <n-button type="success" strong @click="prop.sendMessage">发送</n-button>
    </n-space>
  </n-layout-footer>
</template>

<script setup lang="ts">
const chatMessage = defineModel<string>('chatMessage', { type: String, default: '' });
const prop = defineProps<{
  sendMessage: () => void;
}>();
</script>
