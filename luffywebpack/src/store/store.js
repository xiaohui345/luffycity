import vuex from 'vuex'
import Vue from 'vue'
import Vuecookies from 'vue-cookies'


Vue.use(vuex);
Vue.use(Vuecookies);

//构建一个vuex的store实例对象
export default new vuex.Store({
  state:{
    //页面刷新的时候就去cookies里面去取数据了
    nickname:Vuecookies.get("nickname"),
    token:Vuecookies.get("token"),
    apiList:{
    //  面向资源 ：api
      login :'http://127.0.0.1:8008/api/v2/login/',
      micro:"http://127.0.0.1:8008/api/v2/micro/",
      course:"http://127.0.0.1:8008/api/v2/course/",
      register:"http://127.0.0.1:8008/api/v2/register/",
    },
    backUrl:'',
    p_id:'',

  },
  mutations:{
    changeUser(state,data){
      //这里存的数据是暂时的，一刷新后就消失了，因此必须把数据保存到cookies里面去。
      state.nickname = data.nickname;
      state.token = data.token;
      Vuecookies.set("nickname",data.nickname,"20min");
      Vuecookies.set("token",data.token,"20min")
    },
    DeleteUser(state){
    //这里存的数据是暂时的，一刷新后就消失了，因此必须把数据保存到cookies里面去。
    state.nickname = '';
    state.token = '';
    Vuecookies.remove("nickname");
    Vuecookies.remove("token")
  }
  },
  actions:{

  }
});
