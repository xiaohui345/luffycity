<template>
  <nav class="navbar navbar-default">
    <div class="container-fluid">
      <div class="navbar-header">
        <img src="https://hcdn1.luffycity.com/static/frontend/activity/head-logo_1564141048.3435316.svg" alt="">
      </div>
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <!--用数字来进行判断的话，解决了重复定义判断的麻烦，这种思路还行-->
          <!--<li :class="{active:show==1}" @click="linkshow"><a>导航链接</a></li>-->
          <!--<li :class="{active:show==2}" @click="musicshow"><router-link to="/music">音乐播放器</router-link></li>-->
          <!--<li :class="{active:show==3}" @click="luboshow"><router-link to="/lubo">林允儿图片</router-link></li>-->
          <!--<li :class="{active:show==4}" @click="markshow"><router-link to="/mark">markeddowm</router-link></li>-->
          <!--<li :class="{active:show==5}" @click="tabaoshow"><a>淘宝</a></li>-->
          <!--<li :class="{active:show==6}" @click="lufengshow"><a>路飞</a></li>-->
          <li v-for="(item,index) in routes" :class="{active:index===currentIndex}" @click="activeHander(index)">
            <router-link :to="item.url">{{item.title}}</router-link>
          </li>
          <li><a href="https://www.cnblogs.com/zenghui-python/">我的博客</a></li>
        </ul>


        <ul class="nav navbar-nav navbar-right ">
          <li v-if="this.$store.state.nickname">
            <!--有昵称就表示已经登录了-->
             <a>{{this.$store.state.nickname}}</a>
          </li>
          <li v-else>
             <!--否则就没有登录-->
            <router-link to="/login"><span @click="backurlHander">登录</span></router-link>
          </li>
          <li v-if="this.$store.state.nickname">
            <a @click="loginout">注销</a>
          </li>
           <li v-else>
             <!--否则就没有登录-->
             <router-link to="/register"><span @click="backurlHander">注册</span></router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: "Vheader",
    data() {
      return {
        routes: [
          {url: "/", title: "导航链接"},
          {url: "/course", title: '课程列表'},
          {url: "/micro", title: '深科技'},
        ],
        currentIndex: null,
        show: null
      }
    },
    methods: {
      activeHander(index) {
        this.currentIndex = index
      },
      loginout(){
        this.$store.commit('DeleteUser')
      },
      backurlHander(){
        this.$store.state.backUrl = this.$router.currentRoute.fullPath;
        console.log(this.$store.state.backUrl)
      },
    },
    created() {
      //用this.$route 来访问路由
      console.log(this.$route);
      for (var i = 0; i < this.routes.length; i++) {
        if (this.routes[i].url === this.$route.path) {
          this.currentIndex = i;
          //停止
          return;
        }
      }
    }
  }
</script>

<style scoped>
  * {
    padding: 0;
    margin: 0;
  }

  body {
    font-size: 14px;
    color: #4a4a4a;
  }

  ul {
    list-style: none;
  }

  a {
    text-decoration: none;
  }

</style>
