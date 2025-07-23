import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/LoginView.vue'
import Dashboard from '../views/DashboardView.vue'

const routes = [
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/', redirect: '/login' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
