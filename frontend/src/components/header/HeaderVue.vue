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
                    <a class="top-menu-item" href="http://www.sunwings.top/index.html">Home</a>
                    <a class="top-menu-item" href="">NFT</a>
                    <a class="top-menu-item" href="http://www.sunwings.top/news.html">News</a>
                    <a class="top-menu-item" href="http://www.sunwings.top/contact.html">Contract</a>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang="ts">
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
        .top-menu-item {
            font-size: 14px;
            font-family: Arial, Helvetica, sans-serif;
            padding: 15px;
            color: #ffffff;
        }
        a:link {
            text-decoration: none;
        }
        
        a:visited {
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: none;
        }
        
        a:active {
            text-decoration: none;
        }
    }
}
</style>
