<template>
  <!--<ul>-->
  <!--<li v-for="(item,index) in courseData" style="list-style: none" >-->
  <!--&lt;!&ndash;<span @click="getDetail(item.id,item.title)">{{item.title}}</span>&ndash;&gt;-->
  <!--<router-link :to="{name:'Vcoursedetail',params:{id:item.id}}">-->
  <!--<img :src=item.course_img alt="">-->
  <!--<h3>{{item.title}}</h3>-->
  <!--</router-link>-->
  <!--<p>课程等级:{{item.level}}</p>-->
  <!--</li>-->
  <!--</ul>-->
  <div>
    <div v-for="(item,index) in courseData">
      <!--每次循环就是一个长400px的盒子-->
      <div style="width: 500px;float:left">
        <router-link :to="{name:'Vcoursedetail',params:{id:item.id}}">
          <img :src=item.course_img alt="" style="width: 300px; height: 200px">
          <h3>{{item.name}}</h3>
        </router-link>
        <p>课程类型:{{item.course_type}}</p>
        <p>课程课时:{{item.period}}周</p>
        <p>课程等级:{{item.level}}</p>
        <p>课程介绍:{{item.brief}}</p>
      </div>
    </div>
  </div>

</template>

<script>

  export default {
    name: "Vcourse",
    data() {
      return {
        courselist: []
      }
    },
    methods: {
      initCourse() {
        var that = this;
        this.$axios.request({
          url: that.$store.state.apiList.course,
          method: "get",
        }).then(function (ret) {
          //里面的this变换了
          console.log(ret.data);
          that.courselist = ret.data.data;
        }).catch(function (ret) {
          // console.log(ret.error)
        })
      },
      getDetail(id, title) {
        this.$router.push({
          path: `/coursedetail/${id}`,
        });
        this.$store.state.title = title
      },
    },
    computed: {
      courseData() {
        return this.courselist
      }
    },
    //  DOM加载完以后，自动执行
    mounted() {
      this.initCourse()
    },


  }
</script>

<style scoped>

</style>
