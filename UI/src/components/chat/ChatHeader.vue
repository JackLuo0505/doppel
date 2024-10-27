<template>
  <n-layout-header>
    <n-flex justify="space-between" align="center" style="padding: 0.3rem 1rem">
      <n-dropdown :options="dropOptions" trigger="click">
        <n-button tertiary type="success"> 选择模式 </n-button>
      </n-dropdown>

      <n-space align="center">
        <n-icon>
          <ChatbubbleOutline />
        </n-icon>
        <n-p> 临时聊天 </n-p>
      </n-space>
      <n-avatar round size="large" src="/musk.jpg" />
    </n-flex>
  </n-layout-header>
</template>

<script lang="ts" setup>
import { ChatbubbleOutline } from '@vicons/ionicons5';
const dropOptions = [
  {
    label: '群聊模式',
    key: 'many'
  },
  {
    label: '单聊模式',
    key: 'single'
  }
];
</script>
