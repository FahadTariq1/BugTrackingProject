import { createRouter, createWebHistory } from 'vue-router';

import SignIn from '../views/Signin.vue';
import ChoiceUsertype from '@/views/ChoiceUsertype.vue';
import Allprojects from '@/views/Allprojects.vue';
import Login from '@/views/Login.vue';
import AllBugs from '@/views/AllBugs.vue';

const routes = [
  {
    path: '/',
    name: 'ChoiceUsertype',
    component: ChoiceUsertype,
  },
  {
    path: '/SignIn',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/allprojects',
    name: 'Allprojects',
    component: Allprojects,
  },
  {
    path: '/allbugs/:project_id',
    name: 'AllBugs',
    component: AllBugs,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Global navigation guard
router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/Login', '/signin'];
  const authRequired = !publicPages.includes(to.path);
  const token = localStorage.getItem('authToken');

  if (authRequired && !token) {
    return next('/Login');
  }

  next(); // Proceed to the requested page
});

export default router;
