// pages/step1/step1.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    sum_socre:0,
    score1:0,
    statu1:0,
    score2:0,
    statu2:0,
    score3:0,
    statu3:0,
    items1: [
      { name: 'no1', value: '<35', score:'0.81'},
      { name: 'no2', value: '35-39', score: '0.54' },
      { name: 'no3', value: '40-44', score: '0.23' },
      { name: 'no4', value: '45-49', score: '0' },
      { name: 'no5', value: '≥50', score: '0.16' },
    ] ,
    items2: [
      { name: 'no6', value: '0', score: '0' },
      { name: 'no7', value: '1-3', score: '0.38' },
      { name: 'no8', value: '≥4', score: '1.2' },
    ] ,
    items3:[
      { name: 'no9', value: '未知', score: '0.61' },
      { name: 'no10', value: '≤', score: '0' },
      { name: 'no11', value: '>2', score: '0.42' },


    ]

  },
  radioChange1: function (e) {
      switch (e.detail.value) {
        case "no1":
          this.setData({
            score1: 81,

          });
          break;
        case "no2":
          this.setData({
            score1: 54
          });
          break;
        case "no3":
          this.setData({
            score1: 23
          });
          break;
        case "no4":
          this.setData({
            score1: 0
          });
          break;
        case "no5":
          this.setData({
            score1: 16
          });
          break;

        default:
          console.log("default");
      }
      let sum = (this.data.score1 + this.data.score2 + this.data.score3)/100;
      console.log(sum);
      this.setData({
        sum_socre: sum,
        statu1: 1,
      })   
    if ((this.data.statu1 + this.data.statu2 + this.data.statu3) == 3) {
      wx.navigateTo({
        url: '/pages/step2/step2',
      })
    } 
  },
  radioChange2: function (e) {

    console.log(e);
    switch (e.detail.value) {
      case "no6":
        this.setData({
          score2: 0,
        });
        break;
      case "no7":
        this.setData({
          score2: 38
        });
        break;
      case "no8":
        this.setData({
          score2: 120
        });
        break;
      default:
        console.log("default2");
    }
    console.log(this.data.score2);
    let sum = (this.data.score1+this.data.score2+this.data.score3)/100;
    this.setData({
      sum_socre: sum,
      statu2:1,
    })
  },
  radioChange3: function (e) {

    console.log(e);
    switch (e.detail.value) {
      case "no9":
        this.setData({
          score3: 61,
        });
        break;
      case "no10":
        this.setData({
          score2: 0,
        });
        break;
      case "no11":
        this.setData({
          score2: 42
        });
        break;
      default:
        console.log("default3");
    }
    console.log(this.data.score3);
    let sum = (this.data.score1 + this.data.score2 + this.data.score3)/100;
    this.setData({
      sum_socre: sum,
      statu3: 1,
    })
    
  },



  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  }
})