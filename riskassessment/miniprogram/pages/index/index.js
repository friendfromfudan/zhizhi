//index.js
const app = getApp()

Page({

  jmp (e){
    console.log('跳了')
    wx.navigateTo({
      url: '/pages/step1/step1',
    })
  },

   
})
