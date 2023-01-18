<template>
  <div ref="root">
    <el-container>
      <el-header height="80px">
          <header-view></header-view>
      </el-header>
      <el-main>
        <router-view class="main"></router-view>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import store from "./store";
import HeaderView from "@/components/header/HeaderVue.vue";
import { WindowSize, computeWindowSizeByWidth } from '@/functions/WindowSizeFunctions/WindowSizeTypes';

const root = ref<HTMLElement | null>(null);

onMounted(() => {
  window.addEventListener("resize", WindowResizeHandler);
  store.commit({
        type: 'resizeWindow',
        size: computeWindowSizeByWidth(Number(root.value?.clientWidth)),
        windowWidth:Number(root.value?.clientWidth)
    });
})

function WindowResizeHandler(e: any) {
  store.commit({
        type: 'resizeWindow',
        size: computeWindowSizeByWidth(e?.target?.innerWidth),
        windowWidth:Number(root.value?.clientWidth)
    });
}
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
