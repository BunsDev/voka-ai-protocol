<template>
  <div class="home">
    <MetaMask></MetaMask>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MetaMask from '@/components/MetaMask.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    MetaMask,
  },
});
</script>
