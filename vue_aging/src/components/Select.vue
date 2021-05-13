<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>老化查询结果</el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 卡片视图区域 -->
        <el-card>
            <!-- 列表区域 -->
            <el-table :data="agingjson" border stripe>
                <el-table-column label="可用内存(M)" prop="AVAILABLE_MEMORY" width="100" align="center"></el-table-column>
                <el-table-column label="剩余CPU" prop="CPU" width="80" align="center"></el-table-column>
                <el-table-column label="TCP连接数" prop="TCP_CONNECT" width="95" align="center"></el-table-column>
                <el-table-column label="根目录空间大小(M)" prop="SPACE_SIZE_GEN" width="140" align="center"></el-table-column>
                <el-table-column label="TDFS目录空间大小(M)" prop="SPACE_SIZE_TDFS" width="160" align="center"></el-table-column>
                <el-table-column label="僵尸进程数" prop="ZOMBIE" width="90" align="center"></el-table-column>
                <el-table-column label="Java_tomcat进程" align="center">
                    <el-table-column label="Tomcat进程号" prop="TOMCAT_PID" width="120" align="center"></el-table-column>
                    <el-table-column label="虚拟内存(M)" prop="TOMCAT_VIRT" width="100" align="center"></el-table-column>
                    <el-table-column label="物理内存(M)" prop="TOMCAT_RES" width="100" align="center"></el-table-column>
                    <el-table-column label="CPU" prop="TOMCAT_CPU" width="60" align="center"></el-table-column>
                </el-table-column>
                <el-table-column label="X1进程" align="center">
                    <el-table-column label="X1进程号" prop="X1_PID" width="120" align="center"></el-table-column>
                    <el-table-column label="虚拟内存(M)" prop="X1_VIRT" width="100" align="center"></el-table-column>
                    <el-table-column label="物理内存(M)" prop="X1_RES" width="100" align="center"></el-table-column>
                    <el-table-column label="CPU" prop="X1_CPU" width="60" align="center"></el-table-column>
                </el-table-column>
                <el-table-column label="Mysql进程" align="center">
                    <el-table-column label="Mysql进程号" prop="MYSQL_PID" width="120" align="center"></el-table-column>
                    <el-table-column label="虚拟内存(M)" prop="MYSQL_VIRT" width="100" align="center"></el-table-column>
                    <el-table-column label="物理内存(M)" prop="MYSQL_RES" width="100" align="center"></el-table-column>
                    <el-table-column label="CPU" prop="MYSQL_CPU" width="60" align="center"></el-table-column>
                </el-table-column>
                <el-table-column label="Java_cassandra进程" align="center">
                    <el-table-column label="Cassandra进程号" prop="CASSANDRA_PID" width="130" align="center"></el-table-column>
                    <el-table-column label="虚拟内存(M)" prop="CASSANDRA_VIRT" width="100" align="center"></el-table-column>
                    <el-table-column label="物理内存(M)" prop="CASSANDRA_RES" width="100" align="center"></el-table-column>
                    <el-table-column label="CPU" prop="CASSANDRA_CPU" width="60" align="center"></el-table-column>
                </el-table-column>
                <el-table-column label="Oracle进程" align="center">
                    <el-table-column label="Oracle进程号" prop="Oracle_PID" width="120" align="center"></el-table-column>
                    <el-table-column label="虚拟内存(M)" prop="Oracle_VIRT" width="100" align="center"></el-table-column>
                    <el-table-column label="物理内存(M)" prop="Oracle_RES" width="100" align="center"></el-table-column>
                    <el-table-column label="CPU" prop="Oracle_CPU" width="60" align="center"></el-table-column>
                </el-table-column>
            </el-table>
        </el-card>
    </div>
</template>

<script>
export default {
  data () {
    return {
      // 如果接口返回值无法映射到页面，请检查后端接口格式应该为数组[]
      agingjson: []
    }
  },
  mounted: function () {
    this.getData()
  },
  methods: {
    getData () {
      this.agingjson = JSON.parse(sessionStorage.getItem('agingdata'))
      console.log(this.agingjson)
    }
  }
}
</script>

<style lang="less" scoped>
.el-table {
    font-size: 13px;
}
</style>
