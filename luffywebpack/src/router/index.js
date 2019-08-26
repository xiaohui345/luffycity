import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Vmain from '@/components/Vmain'
import Vcourse from '@/components/content/Vcourse'
import Vcoursedetail from '@/components/content/Vcoursedetail'
import Vmicro from '@/components/content/Vmicro'
import Varticle from '@/components/content/Varticle'
import Vlogin from '@/components/Vlogin'
import Vregister from '@/components/Vregister'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Vmain',
      component: Vmain,


    },
    {
      path: '/course',
      name: 'Vcourse',
      component: Vcourse,
    },
    {
      path: '/coursedetail/:id',
      name: 'Vcoursedetail',
      component: Vcoursedetail,
      //需要登录后才能访问的路由。
      // meta: {
      //   requireAuth: true
      // }
    },
    {
      path: '/login/',
      name: 'login',
      component: Vlogin
    },
    {
      path: '/register/',
      name: 'register',
      component: Vregister
    },
    {
      path: '/micro/',
      name: 'micro',
      component: Vmicro,
      // meta: {
      //   requireAuth: true
      // },
    },
      {
      path: '/article/:id',
      name: 'article',
      component: Varticle,
      meta: {
        requireAuth: true
      },
    }
  ],
  mode: 'history'
})
