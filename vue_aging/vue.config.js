module.exports = {
  // lintOnSave: false
  devServer: {
    open: false,
    proxy: {
      '/proxy': {
        target: 'http://192.168.28.80:5000', // 这里填写后台真是接口
        ws: true,
        changeOrigin: true, // 允许跨域
        pathRewrite: {
          '^/proxy': ''
        }
      }
    }
  }
}