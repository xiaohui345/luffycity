<template>
  <div>
    <h2>文章详情</h2>
    <ul style="padding:5px">
      <li style="list-style: none">
        <img :src=head_img alt="" style="width: 300px;height: 200px">
        <h2>{{title}}</h2>
        <p>来源于:{{source}}</p>
        <p>正文:{{content}}</p>
        <i class="fa fa-commenting-o" aria-hidden="true"></i>
        <span class="comment ">评论数:{{comment_num}}</span>
        <a><i class="fa fa-thumbs-up" aria-hidden="true" @click="ChangecommentHander"></i></a>
        <span class="comment">点赞数:{{agree_num}}</span>
        <a><i class="fa fa-star-o" aria-hidden="true" @click="ChangecollectHander"></i></a>
        <span class="comment ">收藏数:{{collect_num}}</span>
      </li>
    </ul>
    <p>评论区:</p>
    <div v-for="(comment_obj,index) in commentHaner" style="padding:5px 0;border-bottom: 1px solid slategray;">
      <div>
        <p>评论人:{{comment_obj.username}}</p>
        <p>评论时间:{{comment_obj.date|formatDate}}</p>
        <div v-if="comment_obj.p_id">
          <!--有父评论，就显示父评论-->
          <div class="alert alert-success" role="alert">
            <p>@<span>{{ comment_obj.p_comment.username}}:</span></p>
            <p>{{ comment_obj.p_comment.comment }}</p>
          </div>
        </div>
        <p>评论内容:{{comment_obj.comment}}</p>
        <a><i class="fa fa-thumbs-up" aria-hidden="true"></i></a>
        <span class="comment">点赞数:{{comment_obj.agree_number}}</span>
        <a><i class="fa fa-thumbs-down" aria-hidden="true"></i></a>
        <span class="comment">踩数:{{comment_obj.disagree_number}}</span>
        <a><span class="comment" @click="recallHander(comment_obj.id,comment_obj.username)">回复</span></a></div>

    </div>
    <p>评论:</p>
    <div class="col-md-4">
      <textarea name="" id="" cols="20" rows="3" class="form-control" v-model="comentcontent"></textarea>
    </div>

    <button class="btn btn-success" @click="commentHander()">提交评论</button>

  </div>

</template>

<script>
  import {formatDate} from "../../date";
  import $ from 'jquery'

  export default {
    name: "Varticle",
    data() {
      return {
        head_img: '',
        title: '',
        source: '',
        content: '',
        isclick: false,
        comment_num: 0,
        agree_num: 0,
        collect_num: 0,
        comentcontent: '',
        comment: [],
        isup: true,
        //  是true 则会点赞，如果是false则会踩
      }
    },
    methods: {
      initarticledetail(article_id) {
        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/micro/" + article_id + "/",
          method: "get",
          //这里必要带token值进行后端的登录校验，成功后才能把数据返回
          // params 发过去的是get请求的条件
          //  params:{
          //    token:that.$store.state.token
          //  }
        }).then(function (arg) {
          // console.log(arg.data);
          that.head_img = arg.data.data.head_img;
          that.title = arg.data.data.title;
          that.source = arg.data.data.source;
          that.content = arg.data.data.content;
          that.comment_num = arg.data.data.comment_num;
          that.agree_num = arg.data.data.agree_num;
          that.collect_num = arg.data.data.collect_num;
          that.comment = arg.data.arcticle_comment;
        }).catch(function (arg) {
          // console.log(arg.data)
        })

      },

      ChangecommentHander() {
        //    点击 点赞数+1
        //  每个人只能点赞一次，在后端进行判断
        var article_id = this.$route.params.id;
        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/micro/" + article_id + "/" + 'updown/',
          method: 'post',
          data: {
            token: that.$store.state.token,
            article_id: article_id,
            isup: that.isup,
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (arg) {
          //  提交成功后
          if (arg.data.code === 1000) {
            if (arg.data.data.status) {
              //表示点赞成功
              //在网页上要展示加1
              that.agree_num++;
            } else {
              //已经点赞过了
              alert(arg.data.data.msg)
            }
          } else {
            // console(arg.data.error)
          }
        }).catch(function (arg) {
        })

      },
      ChangecollectHander() {
        //   收藏 收藏数+1
        var article_id = this.$route.params.id;
        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/micro/" + article_id + "/" + "collection/",
          method: 'post',
          data: {
            token: that.$store.state.token,
            article_id: article_id,
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (arg) {
          if (arg.data.code === 1000) {
            console.log(arg.data);
            if (arg.data.collections) {
              //    收藏成功
              that.collect_num++;
              alert(arg.data.msg)

            } else {
              //  每个人只能点一次收藏，再点就取消收藏了。
              //    取消收藏
              that.collect_num--;
              alert(arg.data.msg)
            }
          } else {
            //收藏失败
          }
        }).catch(function () {

        });

      },
      commentHander() {
        //提交评论
        var p_node = this.$store.state.p_id;
        var article_id = this.$route.params.id;
        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/micro/" + article_id + "/",
          method: 'post',
          data: {
            token: that.$store.state.token,
            article_id: article_id,
            comentcontent: that.comentcontent,
            p_node: p_node
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (arg) {
          //  提交成功后
          if (arg.data.code === 1000) {
            alert(arg.data.msg);
            console.log(arg.data);
            that.comment_num++;
            that.comentcontent = '';
            that.comment.push(arg.data.comment)
          } else {
            alert(arg.data.error)
          }
        }).catch(function (arg) {
        })
      },
      recallHander(p_id, username) {
        this.comentcontent = '@' + username + ' \n ';
        this.$store.state.p_id = p_id
      }

    },
    mounted() {
      var article_id = this.$route.params.id;
      this.initarticledetail(article_id)
    },
    computed: {
      commentHaner() {
        return this.comment
      }
    },
    filters: {
      formatDate(time) {
        var date = new Date(time);
        return formatDate(date, 'yyyy-MM-dd hh:mm');
      }
    }
  }

</script>

<style scoped>
  .comment {
    padding-right: 20px
  }
</style>
