<template>
  <div id="app">
    <Vheader></Vheader>
    <router-view/>
  </div>
</template>

<script>
import Vheader from './components/Vheader'
import 'bootstrap/dist/css/bootstrap.min.css'
export default {
  name: 'App',
  components:{
    Vheader
  }
}
</script>

<style>

</style>
