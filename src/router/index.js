import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// });

export default new Router({
  mode: 'history',

  routes: [
    {
      path: '/',
      name: 'home',
      meta: {layout: 'landing'},
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
      path: '/about-me',
      name: 'about',
      meta: {layout: 'no-sidebar'},
      component: () => import('@/pages/About.vue')
    },
    {
      path: '*',
      name: '404*',
      component: require('@/pages/404.vue').default // load sync home
    }
  ]
});
