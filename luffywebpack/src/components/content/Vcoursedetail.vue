<template>

  <ul>
    <li v-for="(item,index) in coursedetailData" style="list-style: none">
      <img :src=item.img alt="">
      <h2>{{item.name}}课程的介绍:</h2>
        <p>{{item.content}}</p>
      <p>课程讲师:</p>
      <ul>
        <li v-for="(itte3,index) in item.teachers" style="list-style: none">
          <p>老师:{{itte3.name}}</p>
          <p>职位:{{itte3.title}}</p>
          <!--<router-link :to="{name:'Vcoursedetail',params:{id:itte3.id}}">{{itte3.title}}</router-link>-->
        </li>
      </ul>
      <p>学习课程的原因:{{item.why_study}}</p>
      <p>将学到哪些内容:{{item.what_to_study_brief}}</p>
      <p>此项目如何有助于我的职业生涯:{{item.career_improvement}}</p>
      <p style="border-bottom: 1px solid slategray">课程先修要求:{{item.prerequisite}}</p>
      <!--<h3>课程章节表:</h3>-->
      <!--<ul>-->
        <!--<li v-for="(itte2,index) in item.sections">-->
          <!--<span>{{itte2.title}}</span>-->
        <!--</li>-->
      <!--</ul>-->
      <p>学习周期:</p>
      <!--相当循环每一个盒子-->
        <div v-for="(price,index) in item.price">
          <div style="width: 300px;float:left">
            <p>{{price.valid_period}}</p>
            <p>{{price.price}}元</p>
          </div>
        </div>
      <div class="clearfix" style="border-bottom: 1px solid slategray"></div>
      <p>课程章节:</p>
      <ul style="padding:5px 0">
        <li v-for="(coursecter,index) in item.coursechapter" style="list-style: none;border-bottom: 1px solid slategray">
          <p>第{{coursecter.chapter}}节</p>
            <p>章节名称:{{coursecter.title}}</p>
            <p>章节介绍:{{coursecter.summarys}}</p>
        </li>
      </ul>
      <p>推荐相关的课程:</p>
      <ul>
        <li v-for="(itte3,index) in item.recommend_courses">
          <a @click="changeDetail(itte3.id)">{{itte3.title}}</a>
          <!--<router-link :to="{name:'Vcoursedetail',params:{id:itte3.id}}">{{itte3.title}}</router-link>-->
        </li>
      </ul>
    </li>
  </ul>

</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Vcoursedetail",
    data() {
      return {
        coursedetail: [],
      }
    },
    methods: {
      initCoursedetail(id) {

        var that = this;
        this.$axios.request({
          url: "http://127.0.0.1:8008/api/v2/course/" + id + '/',
          method: "get",
        }).then(function (ret) {
          //里面的this变换了
          if (ret.data.code === 1000) {
            console.log(ret.data);
            that.coursedetail = ret.data.data;
          } else {
            alter(ret.data.error)
          }
          // console.log(ret.data)
        }).catch(function (ret) {
          // console.log(ret.error)
        })
        // $.ajax({
        //   url: "http://127.0.0.1:8000/api/v2/coursedetailview/" + id,
        //   type: "get",
        //   dataType: "jsonp",    //伪造的ajax ， 跨域请求，但是本质上还是基于script 上面的原理；
        //   jsonp: "callbacks",
        //   success: function (arg) {
        //     var data = JSON.parse(arg);  //反序列化
        //     console.log("data", data);
        //     that.coursedetail = data.data
        //   }
        // })

      },
      //不能在同一组件之间跳转。
      // getDetail(id) {
      //   this.$router.push({
      //     path: `/coursedetail/${id}`,
      //   });
      // },

      //
      //同一个url上的跳转(切换)，只是后面的正则匹配的数字不同，可以通过点击事件，让来这个组件在执行一次，
      // 然后通过重定向this.$router.push({name:"",params:{id:""}}),来改变url上的正则匹配的数字。
      changeDetail(id){
        this.initCoursedetail(id);
        //重定向
        this.$router.push({name:"Vcoursedetail",params:{id:id}})
      },
    },
    computed: {
      coursedetailData() {
        return this.coursedetail
      }
    },
    mounted() {
      //第一次是网页上的
      var id = this.$route.params.id;
      this.initCoursedetail(id);
    }
  }
</script>

<style scoped>

</style>
