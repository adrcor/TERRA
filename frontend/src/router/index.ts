import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import AccountView from '@/views/AccountView.vue'
import { isAuthenticated } from '@/supabase'
import PracticeView from '@/views/PracticeView.vue'
import PrivacyView from '@/views/PrivacyView.vue'
import TermsView from '@/views/TermsView.vue'
import AboutView from '@/views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    // always scroll to top
    return { top: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter: async (to, from) => {
        isAuthenticated()
      }
    },
    {
      path: '/practice',
      name: 'practice',
      component: PracticeView,
      beforeEnter: async (to, from) => {
        if (await isAuthenticated()) {
          return true
        } else {
          return {name: 'login'}
        }
      }
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
    },
    {
      path: '/privacy-policy',
      name: 'privacy',
      component: PrivacyView
    },
    {
      path: '/terms-and-conditions',
      name: 'terms',
      component: TermsView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
  ]
})

export default router
