import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  mode: 'history',

  routes: [
    {
      path: '/',
      name: 'home',
      component: require('@/pages/Home.vue').default // load sync home
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      meta: {layout: 'portfolio'},
      component: () => import('@/pages/Portfolio.vue')
    },
    {
      path: '/photoset/:id',
      name: 'photoset',
      meta: {layout: 'portfolio'},
      component: () => import('@/pages/Photoset.vue')
    },
    {
      path: '/contact-me',
      name: 'contact',
      component: () => import('@/pages/ContactMe.vue')
    },
    {
      path: '/about-me',
      name: 'about',
      component: () => import('@/pages/About.vue')
    },
    {
      path: '/404',
      name: '404',
      meta: {layout: 'blank'},
      component: require('@/pages/404.vue').default // load sync home
    },
    {
      path: '*',
      redirect: '/404'
    }
  ]
});
