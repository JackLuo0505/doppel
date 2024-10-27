<script setup lang="ts">
import { ref } from 'vue';
import { NButton, NModal } from 'naive-ui';
import Card from './UserCard.vue';
import { GetTaroCardByid1, TaroCard } from '@/utils';
import { useRouter } from 'vue-router';
import { useChatContextStore } from '@/store';
const loading = defineModel('loading', {
  type: Boolean,
  default: true
});
const ShowCard = ref<boolean>(false);
const showModal = ref<boolean>(false);
const selectedCards = ref<TaroCard[]>([]);
const chatContext = useChatContextStore();
const handleCardsSelected = (selected: number[]) => {
  selectedCards.value = GetTaroCardByid1(selected);
  console.log(selectedCards.value);
  setTimeout(() => {
    showModal.value = true;
  }, 1000);
};
const router = useRouter();
const navigateToChat = () => {
  console.log('navigateToChat');
  chatContext.setChatArea(Images[currentIndex.value].name);
  chatContext.setChatUser(selectedCards.value[0].name);
  chatContext.setChatCharacter(selectedCards.value[0].mean);

  router.push('/social');
};
const message = useMessage();
const Images = [
  {
    src: 'https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel1.jpeg',
    name: '在校园里轻松漫步'
  },
  {
    src: 'https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel2.jpeg',
    name: '在城市里city walk'
  },
  {
    src: 'https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel3.jpeg',
    name: '去武功山攀爬高峰'
  },
  {
    src: 'https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel4.jpeg',
    name: '去海边看日出'
  }
];
const onIndexUpdate = (newIndex: number) => {
  currentIndex.value = newIndex;
  console.log('当前索引:', newIndex); // 实时输出当前索引值
};
const currentIndex = ref<number>(0);

const fit = ref<number>(0);

watch(
  () => selectedCards.value,
  () => {
    if (selectedCards.value[0].name === '马斯克') {
      fit.value = 100;
      message.success('恭喜你发现了彩蛋,选中了独一无二的自己', { duration: 5000 });
      message.success('自己和自己的匹配度当然是100%', { duration: 5000 });
    } else {
      fit.value = 92.35;
    }
  }
);
</script>

<template>
  <div class="container">
    <n-button
      :loading="loading"
      type="primary"
      @click="
        () => {
          ShowCard = true;
        }
      ">
      看看有谁和你聊上了吧!
    </n-button>

    <Card @cardsSelected="handleCardsSelected" v-show="ShowCard" />
  </div>

  <n-modal
    v-if="showModal"
    v-model:show="showModal"
    preset="card"
    :title="`你选择了${selectedCards[0].name}`"
    size="huge"
    class="answer-model">
    <n-statistic tabular-nums>
      <template #prefix> 根据系统测算,您的和{{ selectedCards[0].name }}的匹配度是 </template>

      <n-number-animation ref="numberAnimationInstRef" :from="0.0" :to="fit" :precision="2" />
      <template #suffix> %</template>
    </n-statistic>
    <n-carousel
      effect="card"
      prev-slide-style="transform: translateX(-150%) translateZ(-800px);"
      next-slide-style="transform: translateX(50%) translateZ(-800px);"
      style="height: 240px"
      :show-dots="false"
      :current-index="currentIndex"
      @update:current-index="onIndexUpdate">
      <n-carousel-item v-for="(image, index) in Images" :key="index" :style="{ width: '60%' }">
        <img class="carousel-img" :src="image.src" />
      </n-carousel-item>
    </n-carousel>
    <n-flex justify="center">
      <n-button @click="navigateToChat">你们决定{{ Images[currentIndex].name }} </n-button>
    </n-flex>
  </n-modal>
</template>

<style scoped>
.container {
  margin: 1rem auto;
  max-width: 100%;
  align-items: center;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>

<style>
.answer-model {
  max-width: 60% !important;
}

@media (max-width: 768px) {
  .answer-model {
    max-width: 90% !important;
  }
}
</style>
