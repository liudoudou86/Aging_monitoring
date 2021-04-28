import Vue from 'vue'
import VueRouter from 'vue-router'
import Aging from '../components/Aging.vue'
import Home from '../components/Home.vue'

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
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  }
]

const router = new VueRouter({
  routes
})

export default router
