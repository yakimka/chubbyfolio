import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const SiteName = process.env.VUE_APP_SITE_NAME;
const DefaultNameForTitle = SiteName !== undefined ? ` | ${SiteName}` : '';

export default new Router({
  mode: 'history',

  routes: [
    {
      path: '/',
      name: 'home',
      meta: {
        title: 'Главная страница' + DefaultNameForTitle
      },
      component: require('@/pages/Home.vue').default // load sync home
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      meta: {
        title: 'Портфолио' + DefaultNameForTitle,
        layout: 'portfolio'
      },
      component: () => import('@/pages/Portfolio.vue')
    },
    {
      path: '/photoset/:id',
      name: 'photoset',
      meta: {
        title: 'Портфолио' + DefaultNameForTitle,
        layout: 'portfolio'},
      component: () => import('@/pages/Photoset.vue')
    },
    {
      path: '/contact-me',
      name: 'contact',
      meta: {
        title: 'Контакты' + DefaultNameForTitle
      },
      component: () => import('@/pages/ContactMe.vue')
    },
    {
      path: '/about-me',
      name: 'about',
      meta: {
        title: 'Обо мне' + DefaultNameForTitle
      },
      component: () => import('@/pages/About.vue')
    },
    {
      path: '/404',
      name: '404',
      meta: {
        title: '404',
        layout: 'blank'},
      component: require('@/pages/404.vue').default // load sync home
    },
    {
      path: '*',
      redirect: '/404'
    }
  ]
});