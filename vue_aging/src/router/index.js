import Vue from 'vue'
import VueRouter from 'vue-router'
import Aging from '../components/Aging.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/aging'
  },
  {
    path: '/aging',
    name: 'Aging',
    component: Aging
  }
]

const router = new VueRouter({
  routes
})

export default router
