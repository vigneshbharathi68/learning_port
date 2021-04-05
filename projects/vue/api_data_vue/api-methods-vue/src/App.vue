<template>
<center>
  <img alt="Vue logo" src="./assets/logo.png">
</center>
  <HelloWorld />
  <FetchApiAxios />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import FetchApiAxios from './components/FetchApiAxios.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    FetchApiAxios
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
