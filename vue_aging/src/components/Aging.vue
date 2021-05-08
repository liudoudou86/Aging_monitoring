<template>
    <div class="Aging_container">
        <div class="Aging_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/tiandy_logo.png" alt="">
            </div>
            <!-- 登录表单区域 -->
            <el-form ref="agingFormRef" :model="agingForm" :rules="agingFormRules" label-width="100px" class="aging_form">
                <!-- IP地址 -->
                <el-form-item label="IP地址" prop="IP_ADDRESS">
                    <el-input v-model="agingForm.IP_ADDRESS" prefix-icon="el-icon-location"></el-input>
                </el-form-item>
                <!-- 端口 -->
                <el-form-item label="端口" prop="PORT">
                    <el-input v-model="agingForm.PORT" prefix-icon="el-icon-monitor"></el-input>
                </el-form-item>
                <!-- 账户 -->
                <el-form-item label="账户" prop="USER">
                    <el-input v-model="agingForm.USER" prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item label="密码" prop="PASSWORD">
                    <el-input v-model="agingForm.PASSWORD" prefix-icon="el-icon-key" type="password"></el-input>
                </el-form-item>
                <!-- 按钮 -->
                <el-form-item class="btns">
                    <el-button type="primary" @click="submitAgingForm('agingFormRef')">查询</el-button>
                    <el-button type="info" @click="resetAgingForm('agingFormRef')">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      // 这是表单的数据绑定
      agingForm: {
        IP_ADDRESS: '',
        PORT: '',
        USER: '',
        PASSWORD: ''
      },
      // 这是表单的验证规则
      agingFormRules: {
        IP_ADDRESS: [
          { required: true, message: '请输入IP地址', trigger: 'blur' },
          { min: 4, max: 15, message: '长度在4到12个字符', trigger: 'blur' }
        ],
        PORT: [
          { required: true, message: '请输入端口号', trigger: 'blur' },
          { min: 2, max: 5, message: '长度在2到5个字符', trigger: 'blur' }
        ],
        USER: [
          { required: true, message: '请输入账户', trigger: 'blur' },
          { min: 4, max: 20, message: '长度在4到20个字符', trigger: 'blur' }
        ],
        PASSWORD: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '长度在6到20个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 这是重置表单数据的按钮
    resetAgingForm (agingFormRef) {
    // console.log(this)
    // 此为resetFields方法对未定义的判断
      if (this.$refs[agingFormRef] !== undefined) {
        this.$refs[agingFormRef].resetFields()
      }
    },
    submitAgingForm (agingFormRef) {
      const api = '/aging?IP_ADDRESS=' + this.agingForm.IP_ADDRESS + '&PORT=' + this.agingForm.PORT + '&USER=' + this.agingForm.USER + '&PASSWORD=' + this.agingForm.PASSWORD
      sessionStorage.setItem('apiaddress', JSON.stringify(api)) // 将接口存入sessionStorage中
      this.$http.get(api).then(
        (result) => {
          this.$message.success('请求成功') // 此处箭头函数的作用是为了更清晰的指向Message
          this.$router.push({ path: '/home' })
          sessionStorage.setItem('agingdata', JSON.stringify(result.data)) // 将接口返回值存入sessionStorage中
          // console.log(result.data)
        }
      ).catch(
        () => {
          this.$message.error('请求失败')
        }
      )
    }
  }
}
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
