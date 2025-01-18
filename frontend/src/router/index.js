import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/views/LoginPage.vue'
import AddMembersPage from '@/views/AddMembersPage.vue'
import AdminPage from '@/views/AdminPage.vue'
import ArticlePage from '@/views/ArticlePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/addmembers',
      name: 'addmembers',
      component: AddMembersPage
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminPage
    },
    {
      path: '/article', 
      name: 'article',
      component: ArticlePage 
    }
  ]
})

export default router