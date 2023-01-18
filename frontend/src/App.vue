<template>
<el-container>
      <el-header height="80px">
          <header-view></header-view>
      </el-header>
      <el-main>
        <router-view class="main"></router-view>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
</template>

<script setup lang="ts">
import HeaderView from "@/components/header/HeaderVue.vue";
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0px !important;;
  margin: 0px !important;;
}

.el-header {
  padding: 0px !important;
  margin: 0px !important;
}

html, body {
  margin: 0px !important;
  padding: 0px !important;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
