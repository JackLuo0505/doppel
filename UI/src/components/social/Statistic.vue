<template>
  <div class="container">
    <!-- Title -->
    <n-gradient-text type="success" :size="48" class="title"> 社交魔法屋 </n-gradient-text>

    <!-- Statistic Information -->
    <n-statistic class="statistic" tabular-nums>
      <template #label>
        发现了
        <span style="font-size: larger">
          <n-number-animation
            ref="numberAnimationInstRef"
            :from="100000"
            :to="prop.MatchedUser"
            :duration="4500"
            class="number-animation" />
        </span>
        个用户和您可能匹配
      </template>
      <template #value>
        遇到了<span class="highlight">{{ prop.MatchedUser }}</span
        >个匹配的灵魂
      </template>
    </n-statistic>

    <!-- Bottom Text -->
    <n-space vertical class="message">
      <transition name="fade" mode="out-in">
        <div v-if="currentMessage" :key="messageIndex">{{ currentMessage }}</div>
      </transition>
    </n-space>

    <!-- Other Components -->
  </div>
  <TaroUser v-model:loading="loading" />
</template>

<script setup lang="ts">
import { NStatistic, NNumberAnimation, NGradientText, NSpace } from 'naive-ui';

const prop = withDefaults(
  defineProps<{
    MatchedUser?: number;
  }>(),
  {
    MatchedUser: 9
  }
);

const tempMessages = [
  '正在筛选年龄相近',
  '正在筛选性格匹配',
  '正在筛选热爱探索',
  '正在筛选兴趣相投',
  '正在筛选聊天话题',
  '正在筛选沟通风格',
  '正在筛选情绪表达',
  '筛选完成!'
];

// Define current message and index
const currentMessage = ref<string>('');
let messageIndex = 0;

const loading = ref<boolean>(true); // 按钮loading状态

// Display next message
const displayNextMessage = () => {
  if (messageIndex < tempMessages.length) {
    currentMessage.value = tempMessages[messageIndex];
    messageIndex++;
    setTimeout(displayNextMessage, 4000 / tempMessages.length);
  } else {
    loading.value = false; // 倒计时结束后关闭loading状态
  }
};

onMounted(() => {
  displayNextMessage();
});
</script>

<style scoped>
/* Container Styles */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  /* background: linear-gradient(135deg, #f0f9ff 0%, #cbebff 100%); */
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Title Styles */
.title {
  font-weight: bolder;
  margin-bottom: 24px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
}
.title .n-icon {
  margin-right: 12px;
}
.number-animation {
  font-size: 40px; /* 增加动画数字字体大小 */
  color: #ff6f61;
}

/* Statistic Styles */
.statistic {
  font-size: 20px;
  color: #333;
  margin-bottom: 24px;
  text-align: center;
}
.highlight {
  color: #ff6f61;
  font-weight: bold;
}
.number-animation {
  font-size: 36px;
  color: #ff6f61;
}

/* Message Styles */
.message {
  font-size: 16px;
  color: #555;
  text-align: center;
  line-height: 1.8;
  margin-top: 30px;
  padding: 20px;
  /* background-color: rgba(255, 255, 255, 0.8); */
  border-radius: 12px;
}

/* Fade Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
