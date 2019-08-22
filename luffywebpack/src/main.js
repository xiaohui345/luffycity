// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import store from './store/store'
import 'font-awesome/css/font-awesome.css'

Vue.config.productionTip = false;

//在vue的全局变量中设置了$axios = axios
// 以后在每个组件中使用时： this.$axios

Vue.prototype.$axios = axios;




//路由拦截器：没有登录过的用户不能访问需要登录的页面，即登录验证
router.beforeEach(function (to,from,next) {
  //to 是要去的Url，from 是从哪里来，next是 进行执行 是否访问 to要去的url
  if(to.meta.requireAuth){
    //需要进行登录的验证，要去的url只有登陆成功后才能访问,即token验证
    if(store.state.token){
      //通过 to的url 访问
      next()
    }else {
      //重定向
      next({name:"login",query:{backUrl: to.fullPath}})
    }

  }else {
    next()
  }
  
});




/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
