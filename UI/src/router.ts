import { createRouter, createMemoryHistory } from 'vue-router';
import PersonSelf from './components/social/PersonSelf.vue';
import SelfMap from './components/social/SelfMap.vue';
import SocialMessage from './components/social/SocialMessage.vue';
const Statisic = () => import('@/components/social/Statistic.vue');
const MindMap = () => import('@/components/map/MindMap.vue');
const TaroCard = () => import('@/components/taro/TaroCard.vue');
const routes = [
  {
    path: '/',
    name: 'Home',
    component: PersonSelf
  },
  {
    path: '/mind-map',
    name: 'MindMap',
    component: MindMap
  },
  {
    path: '/taro-card',
    name: 'TaroCard',
    component: TaroCard
  },
  {
    path: '/statistic',
    name: 'Statisic',
    component: Statisic
  },
  {
    path: '/social',
    name: 'social',
    component: SocialMessage
  },
  {
    path: '/person-map',
    name: 'PersonMap',
    component: SelfMap
  }
];

const router = createRouter({
  history: createMemoryHistory(),
  routes
});

export default router;
