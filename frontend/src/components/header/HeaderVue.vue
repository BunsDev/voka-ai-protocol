<template>
    <div class="header">
        <el-row align="middle" type="flex">
            <el-col :span="8">
                <div class="left">
                    <img src="@/assets/logov2.png" height="36" />
                </div>
            </el-col>

            <el-col :span="2">
            </el-col>

            <el-col :span="14">
                <div class="right">
                    <div class="menu" v-if="_windowWidth >= 700">
                        <a class="top-menu-item" href="http://www.sunwings.top/index.html">Home</a>
                        <a class="top-menu-item" href="">NFT</a>
                        <a class="top-menu-item" href="http://www.sunwings.top/news.html">News</a>
                        <a class="top-menu-item" href="http://www.sunwings.top/contact.html">Contract</a>
                    </div>
                    <div class="menu-dropdown" v-else>
                        <el-dropdown>
                            <img src="@/assets/menu-icon.png" style="width: 20px;"/>
                            <template #dropdown>
                                <el-dropdown-menu>
                                    <el-dropdown-item>
                                        <a class="dropdown-menu-item" href="http://www.sunwings.top/index.html">Home</a>
                                    </el-dropdown-item>
                                    <el-dropdown-item>
                                        <a class="dropdown-menu-item" href="">NFT</a>
                                    </el-dropdown-item>
                                    <el-dropdown-item>
                                        <a class="dropdown-menu-item" href="http://www.sunwings.top/news.html">News</a>
                                    </el-dropdown-item>
                                    <el-dropdown-item>
                                        <a class="dropdown-menu-item" href="http://www.sunwings.top/contact.html">Contract</a>
                                    </el-dropdown-item>
                                </el-dropdown-menu>
                            </template>
                        </el-dropdown>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useStore } from 'vuex';
import { WindowSize } from '@/functions/WindowSizeFunctions/WindowSizeTypes';
let { state } = useStore();

const _windowWidth = computed(() => {
    return state.windowWidth;
})
</script>

<style scoped lang="scss">
.header {
    height: 100%;
    padding-right: 25px;
    padding-left: 25px;
    margin-right: auto;
    margin-left: auto;
    background: #accd9e;

    .el-row {
        height: 100%;
    }

    .left {
        display: flex;
    }

    .right {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        .menu {
            .top-menu-item {
                font-size: 14px;
                font-family: Arial, Helvetica, sans-serif;
                padding: 15px;
                color: #ffffff;
                &:link {
                    text-decoration: none;
                }
                &:visited {
                    text-decoration: none;
                }
                &:hover {
                    text-decoration: none;
                }
                &:active {
                    text-decoration: none;
                }
            }
        }
    }
}
.dropdown-menu-item {
    font-size: 14px;
    font-family: Arial, Helvetica, sans-serif;
    padding: 5px;
    color: #accd9e;
    &:link {
        text-decoration: none;
    }
    &:visited {
        text-decoration: none;
    }
    &:hover {
        text-decoration: none;
    }
    &:active {
        text-decoration: none;
    }
}
</style>
