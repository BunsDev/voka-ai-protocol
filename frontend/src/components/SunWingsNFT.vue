<template>
  <div class="metamask">
    <el-row justify="space-between" v-for="r in NFT_Row" :key="r">
      <el-col v-for="c in NFT_Col" :key="c" :span="Math.floor(24 / NFT_Col)" :offset="c > 1 ? 0 : 0">
        <el-card :body-style="{ padding: '0px' }" shadow="hover" style="margin: 10px;">
          <NFTCard :groupId="NFT_Col*(r-1)+c" :imgUrl="idolinfo[NFT_Col * (r - 1) + c - 1].image" :nftName="idolinfo[NFT_Col * (r - 1) + c - 1].name"></NFTCard>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import NFTCard from '@/components/cards/NFTCard.vue'; // @ is an alias to /src
import { useStore } from 'vuex';
import { WindowSize } from '@/functions/WindowSizeFunctions/WindowSizeTypes';
let { state } = useStore();
const NFT_Row = ref(2);
const NFT_Col = ref(4);

onMounted(() => {
  switch(_windowSize.value) {
    case WindowSize.TOOSMALL: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.TINY: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.SMALL: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.MIDDLE: {
      NFT_Row.value = 4;
      NFT_Col.value = 2;
      break;
    }
    case WindowSize.LARGE: {
      NFT_Row.value = 2;
      NFT_Col.value = 4;
      break;
    }
    default: {
      NFT_Row.value = 2;
      NFT_Col.value = 4;
      break;
    }
  }

})

const _windowSize = computed(() => {
    return state.windowSizeType;
})

watch(_windowSize, (newVal, oldVal) => {
  switch(newVal) {
    case WindowSize.TOOSMALL: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.TINY: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.SMALL: {
      NFT_Row.value = 8;
      NFT_Col.value = 1;
      break;
    }
    case WindowSize.MIDDLE: {
      NFT_Row.value = 4;
      NFT_Col.value = 2;
      break;
    }
    case WindowSize.LARGE: {
      NFT_Row.value = 2;
      NFT_Col.value = 4;
      break;
    }
    default: {
      NFT_Row.value = 2;
      NFT_Col.value = 4;
      break;
    }
  }
})

const idolinfo = [
  {
    "name": "李丹尼尔 Danny",
    "image": require('@/assets/idols/Danny.jpg')
  },
  {
    "name": "昊天 Toey",
    "image": require('@/assets/idols/Toey.jpg')
  },
  {
    "name": "陈家瑨 Chris",
    "image": require('@/assets/idols/Chris.jpg')
  },
  {
    "name": "余俊杰 Prame",
    "image": require('@/assets/idols/Prame.jpg')
  },
  {
    "name": "岳凯峰 Hue",
    "image": require('@/assets/idols/Hue.jpg')
  },
  {
    "name": "黄书豪 Mark",
    "image": require('@/assets/idols/Mark.jpg')
  },
  {
    "name": "苏思南 Park",
    "image": require('@/assets/idols/Park.jpg')
  },
  {
    "name": "王柏佑 Payu",
    "image": require('@/assets/idols/Payu.jpg')
  },
]

</script>

<style scoped lang="scss">
.metamask {
  .el-row {
    margin-bottom: 20px;
  }
}
</style>
