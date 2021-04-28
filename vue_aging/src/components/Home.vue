<template>  
    <el-container class="home-container">
        <!-- 头部区域 -->
        <el-header>
            <div>
                <img src="../assets/tiandy_logo.png" alt="">
                <span>老化数据查询平台</span>
            </div>
            <el-button type="primary" @click="logout">返回</el-button>
        </el-header>
        <!-- 整体页面主体 -->
        <el-container>
            <!-- 侧边栏 -->
            <el-aside width="200px">
                <!-- 侧边栏区域 -->
                <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                    <!-- 一级菜单 -->
                    <el-submenu index="1">
                        <!-- 一级菜单模板区域 -->
                        <template slot="title">
                            <!-- 图表 -->
                            <i class="el-icon-location"></i>
                            <!-- 文本内容 -->
                            <span>七天老化查询</span>
                        </template>
                        <el-submenu index="1-1">
                            <template slot="title">政法行业测试部</template>
                            <el-menu-item index="1-1-1">监察委</el-menu-item>
                            <el-menu-item index="1-1-2">检法</el-menu-item>
                            <el-menu-item index="1-1-3">监管</el-menu-item>
                        </el-submenu>
                        <el-submenu index="1-2">
                            <template slot="title">通用行业测试部</template>
                            <el-menu-item index="1-2-1">交通</el-menu-item>
                        </el-submenu>
                    </el-submenu>
                    <el-menu-item index="2">
                        <i class="el-icon-menu"></i>
                        <span slot="title">长期老化查询</span>
                    </el-menu-item>
                    <el-menu-item index="3">
                        <i class="el-icon-document"></i>
                        <span slot="title">老化查询结果</span>
                    </el-menu-item>
                    <el-menu-item index="4">
                        <i class="el-icon-setting"></i>
                        <span slot="title">老化说明</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-container>
                <!-- 右侧内容主体 -->
                <el-main>Main</el-main>
            </el-container>
        </el-container>
    </el-container>
</template>

<script>
export default {
    methods: {
        logout () {
            this.$router.push('/aging')
        }
    }
}
</script>

<style lang="less" scoped>
.home-container {
    height: 100%;
}

.el-header {
    background-color: #32363A;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    color: #FFFFFF;
    font-size: 25px;
    > div {
        display: flex;
        align-items: center;
        span {
            margin-left: 15px;
        }
    }
}

.el-aside {
    background-color: #545C64;
}

.el-main {
    background-color: #EAEDF1;
}
</style>
