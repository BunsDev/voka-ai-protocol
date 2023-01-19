<template>
  <div class="sunwings_nft_footer" v-mode="1">
      <el-collapse model-value="1">
      <el-collapse-item title="How to mint/buy NFT?" name="1">
        <div>
          Please check the <el-button link type="success" @click="jump2tutorial">Tutorial</el-button>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script setup lang="ts">
import { ref, defineComponent } from 'vue';
import { ElMessageBox } from 'element-plus'

const tutorial_url = "http://ptworker.com/en/2023/01/14/%e5%a6%82%e4%bd%95%e8%b4%ad%e4%b9%b0nft-%ef%bc%88%e4%b8%80%ef%bc%89%ef%bc%9a%e8%b6%85%e7%ba%a7%e6%96%b0%e6%89%8b%e5%85%a5%e9%97%a8/";

const jump2tutorial = () => {
    window.location.href = tutorial_url;
}

const activeNames = ref(['1'])

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/deep/ .el-collapse-item__wrap {
  background-color: #edf0e5;
}

/deep/ .el-collapse-item__header {
  background-color: #edf0e5;
}
</style>
