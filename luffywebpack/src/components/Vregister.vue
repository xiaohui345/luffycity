<template>
  <div>
    <h2>注册页面</h2>
    <div>
      <label>昵称:&emsp;
        <input type="text" placeholder="输入昵称" v-model="nickname">
      </label>
    </div>
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
      <button class="btn btn-info" @click="regBTN">注册</button>
    </div>


  </div>
</template>

<script>
  export default {
    name: "Vregister",
    data() {
      return {
        username: '',
        password: '',
        nickname: '',
      }
    },
    methods: {
      regBTN() {

        //    点击注册的时候把数据发送给后端
        var that = this;
        this.$axios.request({
          url: that.$store.state.apiList.register,
          method: 'post',
          data: {
            nickname: that.nickname,
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
            } else {
              //有点小毛病，就是当你在某个网站点击登录的时候，当前的url应该也带上。这里没有带上
              //通过点击登录或注册的时候保存到当前的路由，然后登录后进行跳转来解决了。
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
  }
</script>

<style scoped>

</style>
