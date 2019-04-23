// pages/user/user.js

const regeneratorRuntime = require('../common/regenerator-runtime.js')

const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userInfo: {},
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log('a');
    this.getOpenid();
    console.log('c');
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
      })
      app.globalData.hasUser = true
      wx.navigateTo({ url: '../index/index' })
      console.log('登录成功')

      this.addUser(app.globalData.userInfo)
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
         
        })
        app.globalData.hasUser=true
        this.addUser(res.userInfo)
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo

          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
          this.addUser(app.globalData.userInfo)
        }
      })
    }
    
    
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
   

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  getOpenid() {
    console.log('b');
    let that = this;
    wx.cloud.callFunction({
      name: 'login',
      success:function(res) {
        app.globalData.openid=res.result.openId;
        console.log(app.globalData.openid) // 3
      },
      fail: console.error

      // complete: res => {
      //   console.log('云函数获取到的openid: ', res.result.openid)
      //   var openid = res.result.openid;
      //   that.setData({
      //     openid: openid
      //   })
      // }
    })
  },

   getUserInfo(e) {
    if (e.detail.userInfo) {
      app.globalData.userInfo = e.detail.userInfo

      this.setData({
        userInfo: e.detail.userInfo,
        hasUserInfo: true
      })

      this.addUser(app.globalData.userInfo)
      wx.navigateTo({ url: '../index/index' })

      // wx.switchTab({ url: '/pages/index/index' })
    }
  },

  // 如果数据库没有此用户，则添加
  async addUser(user) {
    if (app.globalData.hasUser) {
      return
    }


  


    // 在此插入储存用户代码
    // 获取数据库实例
    const db = wx.cloud.database({})


    // db.collection('user').doc('XKMy8nffS3SWdc7v').get({
    //   success(res) {
    //     // res.data 包含该记录的数据
    //     console.log(res.data)
    //   }
    // })

    console.log(app.globalData.hasUser)

    db.collection('user').where({
      nickName: user.nickName,
    })
      .get({
        success(res) {
          console.log(res.data)
        }
      }) 

    // 插入用户信息
    let result = await db.collection('user').add({
      data: {
        nickName: user.nickName,
      }
    })

    app.globalData.nickName = user.nickName
    app.globalData.id = result._id
  }


})