<template>
    <div class="Aging_container">
        <div class="Aging_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/tiandy_logo.png" alt="">
            </div>
            <!-- 登录表单区域 -->
            <el-form label-width="100px" class="aging_form">
                <!-- IP地址 -->
                <el-form-item label="IP地址">
                    <el-input prefix-icon="el-icon-location"></el-input>
                </el-form-item>
                <!-- 端口 -->
                <el-form-item label="端口">
                    <el-input prefix-icon="el-icon-monitor"></el-input>
                </el-form-item>
                <!-- 账户 -->
                <el-form-item label="账户">
                    <el-input prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item label="密码">
                    <el-input prefix-icon="el-icon-key"></el-input>
                </el-form-item>
                <!-- 按钮 -->
                <el-form-item class="btns">
                    <el-button type="primary" @click="onSubmit">查询</el-button>
                    <el-button>重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>
.Aging_container {
    background-color: #2B4B6B;
    height: 100%;
}

.Aging_box {
    width: 500px;
    height: 400px;
    background-color: #FFFFFF;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    .avatar_box {
        height: 40px;
        width: 150px;
        padding: 15px;
        box-shadow: 0 0 50px yellowgreen;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -150%);
        img {
            width: 100%;
            height: 120%;
        }
    }
}

.aging_form {
    position: absolute;
    bottom: 0;
    widows: 100%;
    height: 90%;
    padding: 0 50px;
    box-sizing:border-box
}

.btns {
    display: flex;
    justify-content: flex-start;
}
</style>
