import Vue from 'vue'
import VueRouter from 'vue-router'
import Aging from '../components/Aging.vue'
import Home from '../components/Home.vue'
import Welcome from '../components/Welcome.vue'
import Select from '../components/Select.vue'

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
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome',component: Welcome },
      { path: '/select',component: Select }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
