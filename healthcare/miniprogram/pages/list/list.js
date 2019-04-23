const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
    bigImg:'/images/3.jpg'
  },
  
  onLoad(){
    // let that = this
    const db = wx.cloud.database({});
    db.collection('check').where({_openid: app.globalData.openid,}).get({
        success:res=> {
          // res.data 是包含以上定义的两条记录的数组
          console.log(res.data);
          this.setData({
            list: res.data,
            //res代表success函数的事件对，data是固定的，list是数组
          });
          console.log(list);

        }
      });
    db.collection('photo').where({
      _openid: app.globalData.openid,
    })
      .get({
        success:res=> {
          this.setData({
            bigImg:res.data[0].bigImg,
          });
          // res.data 是包含以上定义的两条记录的数组
          console.log(res.data)
        }
      })

    


  },
  changeBigImg() {
    let that = this;
    let openid = app.globalData.openid;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        wx.showLoading({
          title: '上传中',
        });
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        let filePath = res.tempFilePaths[0];
        const name = Math.random() * 1000000;
        console.log(name)
        console.log(filePath)
        const cloudPath = name + filePath.match(/\.[^.]+?$/)[0]
        console.log(cloudPath);
        wx.cloud.uploadFile({
          cloudPath,//云存储图片名字
          filePath,//临时路径
          success: res => {
            console.log('[上传图片] 成功：', res)
            that.setData({
              bigImg: res.fileID,//云存储图片路径,可以把这个路径存到集合，要用的时候再取出来
            });
            let fileID = res.fileID;
            //把图片存到users集合表
            const db = wx.cloud.database();



            db.collection('photo').where({
              _openid: app.globalData.openid,
            })
              .get({
                success: res => {
                  console.log('图片已经有了')
                  console.log(res.data)
                  console.log('图片id')
                  console.log(res.data[0]._id)
                 
                  
                  console.log('这时候应该更新图片地址')
                
                  db.collection('photo').doc(res.data[0]._id).update({
                    // data 传入需要局部更新的数据
                    data: {
                      bigImg: fileID
                    },
                    success: res => {
                      console.log('lalal')}
                  })

                
                },

                fail:res=>{


                  db.collection("photo").add({
                    data: {
                      bigImg: fileID
                    },
                    success: function () {
                      wx.showToast({
                        title: '图片存储成功',
                        'icon': 'none',
                        duration: 3000
                      })
                    },
                    fail: function () {
                      wx.showToast({
                        title: '图片存储失败',
                        'icon': 'none',
                        duration: 3000
                      })
                    }
                  })

                }



              })



            
            
            ;
          },
          fail: e => {
            console.error('[上传图片] 失败：', e)
          },
          complete: () => {
            wx.hideLoading()
          }
        });
      }
    })
  }
  ,
  toCheck: function (event){
    console.log('adfads');
    const db = wx.cloud.database({});

    db.collection('check').add({
      // data 字段表示需新增的 JSON 数据
      data: {
        data: new Date()
      },
      success(res) {
        // res 是一个对象，其中有 _id 字段标记刚创建的记录的 id
        console.log(res)
      }
    })

  }
  ,
  SetShadow(e) {
    this.setData({
      shadow: e.detail.value
    })
  },
  SetBorderSize(e) {
    this.setData({
      bordersize: e.detail.value
    })
  },
});
