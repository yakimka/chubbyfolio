import Vue from 'vue';
import Router from 'vue-router';
import config from './config';

Vue.use(Router);

const SiteName = config.VUE_APP_SITE_NAME;
const DefaultNameForTitle = SiteName !== undefined ? ` | ${SiteName}` : '';

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      meta: {
        title: 'Главная страница' + DefaultNameForTitle
      },
      component: require('@/views/Home.vue').default // load sync home
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      meta: {
        title: 'Портфолио' + DefaultNameForTitle,
        layout: 'portfolio'
      },
      component: () => import('@/views/Portfolio.vue')
    },
    {
      path: '/photoset/:id',
      name: 'photoset',
      meta: {
        title: 'Портфолио' + DefaultNameForTitle,
        layout: 'portfolio'
      },
      component: () => import('@/views/Photoset.vue')
    },
    {
      path: '/contact-me',
      name: 'contact',
      meta: {
        title: 'Контакты' + DefaultNameForTitle
      },
      component: () => import('@/views/ContactMe.vue')
    },
    {
      path: '/about-me',
      name: 'about',
      meta: {
        title: 'Обо мне' + DefaultNameForTitle
      },
      component: () => import('@/views/About.vue')
    },
    {
      path: '/404',
      name: '404',
      meta: {
        title: '404',
        layout: 'blank'
      },
      component: require('@/views/404.vue').default // load sync home
    },
    {
      path: '*',
      redirect: '/404'
    }
  ]
});
