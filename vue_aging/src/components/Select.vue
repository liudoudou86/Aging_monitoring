<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>老化查询结果</el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 卡片视图区域 -->
        <el-card>
            <span>{{ agingjson }}</span>
        </el-card>
    </div>
</template>

<script>
export default {
    data () {
        return {
            agingjson: {}
        }
    },
    mounted: function () {
        this.agingjson = JSON.parse(sessionStorage.getItem('agingdata'))
        // console.log(this.agingjson)
    }
}
</script>

<style lang="less" scoped>
</style>
