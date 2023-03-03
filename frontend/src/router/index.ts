import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import AccountView from '@/views/AccountView.vue'
import { isAuthenticated } from '@/supabase'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: async (to, from) => {
        if (await isAuthenticated()) {
          return { name: 'account'}
        } else {
          return true
        }
      }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      beforeEnter: async (to, from) => {
        if (await isAuthenticated()) {
          return { name: 'account' }
        } else {
          return true
        }
      }
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
      beforeEnter: async (to, from) => {
        if (await isAuthenticated()) {
          return true
        } else {
          return {name: 'login'}
        }
      }
    }
  ]
})

export default router
