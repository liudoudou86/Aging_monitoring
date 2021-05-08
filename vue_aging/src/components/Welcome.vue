<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 卡片视图区域 -->
        <el-card>
            <div>
                <h1>欢迎来到老化数据查询平台</h1>
            </div>
            <div>
                <span>1、点击【老化查询结果】查看老化数据</span>
            </div>
            <div>
                <span>2、该平台通过输入服务器相关信息查询老化需求的数据</span>
            </div>
            <div>
                <span>3、如果觉得数据存在问题可通过点击刷新进行反复查询</span>
            </div>
        </el-card>
    </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>
</style>
