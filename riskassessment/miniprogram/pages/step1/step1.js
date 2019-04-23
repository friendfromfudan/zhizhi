// pages/step1/step1.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    sum_socre:0,
    score1:0,
    score2:0,
    score3:0,
    items1: [
      { name: 'no1', value: '<35', score:'0.81'},
      { name: 'no2', value: '35-39', score: '0.54' },
      { name: 'no3', value: '40-44', score: '0.23' },
      { name: 'no4', value: '45-49', score: '0' },
      { name: 'no5', value: '≥50', score: '0.16' },
    ] ,
    items2: [
      { name: 'n06', value: '0', score: '0' },
      { name: 'no7', value: '1-3', score: '0.38' },
      { name: 'no8', value: '≥4', score: '1.2' },
    ] ,
    items3:[
      { name: 'n09', value: '未知', score: '0.61' },
      { name: 'no10', value: '≤', score: '0' },
      { name: 'no11', value: '>2', score: '0.42' },


    ]

  },
  radioChange1: function (e) {
    
    switch (e.detail.value){
      case "no1": 
        let sum;
        sum = this.data.score1 + this.data.score2 + this.data.score3;
        this.setData({
          score1:0.81,
          sum_socre:sum,
        });
        break;
      case "no2":
        this.setData({
          score1: 0.54
        });
        break;
      case "no3":
        this.setData({
          score1: 0.23
        });
        break;
      case "no4":
        this.setData({
          score1: 0
        });
        break;
      case "no5":
        this.setData({
          score1: 0.16
        }); 
        break;

      default:
        console.log("default");


    }


  },
  radioChange2: function (e) {
    
  },
  radioChange3: function (e) {
    
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