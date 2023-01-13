import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NFTView from '../views/NFT.vue'

const routes: Array<RouteRecordRaw> = [
  {
    name: 'nft',
    path: '/',
    components: {
        default: NFTView,
    },
  },
  {
    name: 'about',
    path: '/about',
    components: {
        default: HomeView,
    },
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
