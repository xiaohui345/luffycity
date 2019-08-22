<template>
  <div>
    <h2>深科技</h2>
    <ul style="padding:5px 0">
      <li v-for="(item,index) in articlelist" style="list-style: none">
        <router-link :to="{name:'article',params:{id:item.id}}">
          <h3>{{item.title}}</h3>
          <img :src=item.head_img alt="" style="width: 300px;height: 200px">
        </router-link>
        <p style="padding-top: 10px">来源于:{{item.source}}</p>
        <p>摘要:{{item.brief}}</p>
        <!--<p>正文:{{item.content}}</p>-->
        <i class="fa fa-commenting-o" aria-hidden="true"></i>
        <span class="padcls">评论数:{{item.comment_num}}</span>
        <i class="fa fa-thumbs-up" aria-hidden="true"></i>
        <span class="padcls">点赞数:{{item.agree_num}}</span>
        <i class="fa fa-star-o" aria-hidden="true"></i>
        <span class="padcls">收藏数:{{item.collect_num}}</span>
      </li>
    </ul>
  </div>

</template>

<script>

  export default {
    name: "Vmicro",
    data() {
      return {
        articlelist: [],
      }
    },
    methods: {
      initMicrocouser() {
        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/micro/",
          method: "get",
          //这里必要带token值进行后端的登录校验，成功后才能把数据返回
          // params 发过去的是get请求的条件
          //  params:{
          //    token:that.$store.state.token
          //  }
        }).then(function (arg) {
          console.log(arg.data);
          that.articlelist = arg.data.data;
        }).catch(function (arg) {
          console.log(arg.data)
        })

      }

    },
    mounted() {
      this.initMicrocouser()
    },
  }
</script>

<style scoped>
  .padcls {
    padding-right: 5px
  }
</style>
