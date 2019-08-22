<template>
  <div>
    <h2>登录页面</h2>
    <div>
      <label>用户名:
        <input type="text" placeholder="输入用户名" v-model="username">
      </label>
    </div>
    <label>密码:&emsp;
      <!--&emsp;是一个中文的空格-->
      <input type="password" placeholder="输入密码" v-model="password">
    </label>
    <div>
      <button class="btn btn-info" @click="loginBTN">登录</button>
    </div>


  </div>

</template>

<script>
  export default {
    name: "Vlogin",
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods: {
      loginBTN() {

        //    点击登录的时候把数据发送给后端，进行校验
        var that = this;
        this.$axios.request({
          url: that.$store.state.apiList.login,
          method: 'post',
          data: {
            username: that.username,
            password: that.password,
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (arg) {
          if (arg.data.code === 1000) {
            that.$store.commit('changeUser', arg.data.data);
            //重定向
            //拿到返回登录之前的url
            var tourl = that.$route.query.backUrl;
            console.log(tourl);
            if (tourl) {
              that.$router.push({
                path: tourl,
              });
            }
            else {
              //有点小毛病，就是当你在某个网站点击登录的时候，当前的url应该也带上。这里没有带上
              //通过点击登录的时候保存到当前的路由，然后登录后进行跳转来解决了。
              //还有浏览器返回时url变了，但是网页没有变.
              that.$router.push({
                path: that.$store.state.backUrl,
              });
            }

          } else {
            alert(arg.data.erorr)
          }
        }).catch(function (arg) {
        })
      }
    },
    computed: {},
    mounted() {

    },
    create() {

    }

  }
</script>

<style scoped>

</style>
