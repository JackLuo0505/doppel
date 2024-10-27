<template>
  <div :class="['chat-bubble', position]" v-html="renderedMarkdown"></div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import markdownIt from 'markdown-it';

// 定义props,left 或 right 用于控制气泡位置
const props = defineProps({
  content: {
    type: String,
    required: true
  },
  position: {
    type: String,
    default: 'left'
  }
});

// 使用 markdown-it 解析 markdown 文本
const md = markdownIt();
const renderedMarkdown = computed(() => md.render(props.content));
</script>

<style scoped>
.chat-bubble {
  max-width: 40%;
  padding: 10px;
  margin: 10px;
  border-radius: 10px;
  word-wrap: break-word;
}

/* 左侧气泡样式 */
.left {
  text-align: left;
  margin-right: auto;
}

/* 右侧气泡样式 */
.right {
  text-align: right;
  margin-left: auto;
}
</style>
