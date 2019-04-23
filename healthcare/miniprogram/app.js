//app.js
App({
  onLaunch: function () {

    wx.cloud.init({
      env: 'myclothes-a998d3',
      traceUser: true
    })

    wx.getSystemInfo({
      success: e => {
        this.globalData.StatusBar = e.statusBarHeight;
        let custom = wx.getMenuButtonBoundingClientRect();
        this.globalData.Custom = custom;
        this.globalData.CustomBar = custom.bottom + custom.top - e.statusBarHeight;
        console.log(e.model);
        console.log(e.pixelRatio);
        console.log(e.windowWidth);
        console.log(e.windowHeight);
        console.log(e.language);
        console.log(e.version);
        console.log(e.platform);
      }
    })

    wx.getSetting({
      success: e => {
        if (e.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: e => {
              this.globalData.userInfo = e.userInfo
    

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(e);
               

              }
            }
          })
        } else {
          // 跳转登录页面让用户登录
          // wx.navigateTo({ url: '../index/index' })
        }
      }
    })
  },
  
  
  
  globalData: {
    openid: '',
    hasUser: false, // 数据库中是否有用户
    hasUserInfo: false, // 小程序的userInfo是否有获取
    userInfo: null,
    checkeult: null,
    code: null,
    openId: null,
    flag: 0,
    nickName: '',
    allData: {
      albums: []
    },
    id: null,
    ColorList: [{
      title: '嫣红',
      name: 'red',
      color: '#e54d42'
    },
    {
      title: '桔橙',
      name: 'orange',
      color: '#f37b1d'
    },
    {
      title: '明黄',
      name: 'yellow',
      color: '#fbbd08'
    },
    {
      title: '橄榄',
      name: 'olive',
      color: '#8dc63f'
    },
    {
      title: '森绿',
      name: 'green',
      color: '#39b54a'
    },
    {
      title: '天青',
      name: 'cyan',
      color: '#1cbbb4'
    },
    {
      title: '海蓝',
      name: 'blue',
      color: '#0081ff'
    },
    {
      title: '姹紫',
      name: 'purple',
      color: '#6739b6'
    },
    {
      title: '木槿',
      name: 'mauve',
      color: '#9c26b0'
    },
    {
      title: '桃粉',
      name: 'pink',
      color: '#e03997'
    },
    {
      title: '棕褐',
      name: 'brown',
      color: '#a5673f'
    },
    {
      title: '玄灰',
      name: 'grey',
      color: '#8799a3'
    },
    {
      title: '草灰',
      name: 'gray',
      color: '#aaaaaa'
    },
    {
      title: '墨黑',
      name: 'black',
      color: '#333333'
    },
    {
      title: '雅白',
      name: 'white',
      color: '#ffffff'
    },
    ]
  }, 

  
})