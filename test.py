# -*- coding: utf-8 -*-
"""Oxford_Pet_Localization+Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HV5CFFetaKmH99VycgYJMsfK9-dek2yh
"""

"""Test"""

img=Image.open('IMG_4259.JPG')
img=img.resize((224,224))
img=np.array(img)
img=img/255.

img=np.reshape(img,(1,224,224,3))
pred=model_res.predict(img)
print(pred)

## localization test
prediction=model_res.predict(img)
pred_x=prediction[0,0]
pred_y=prediction[0,1]
pred_w=prediction[0,2]
pred_h=prediction[0,3]
pred_xmin=pred_x - pred_w/2.
pred_ymin=pred_y - pred_h/2.
pred_rect_x=int(pred_xmin*IMG_SIZE)
pred_rect_y=int(pred_ymin*IMG_SIZE)
pred_rect_w=int(pred_w*IMG_SIZE)
pred_rect_h=int(pred_h*IMG_SIZE)

pred_rect=Rectangle((pred_rect_x,pred_rect_y),pred_rect_w,pred_rect_h,
                    fill=False,color='red')
plt.axes().add_patch(pred_rect)
plt.imshow(img[0])
plt.show()

## localization+classification test
pred2=loc_cls_model.predict(img)
pred_x2=pred2[0,2]
pred_y2=pred2[0,3]
pred_w2=pred2[0,4]
pred_h2=pred2[0,5]
pred_xmin2=pred_x2 - pred_w2/2.
pred_ymin2=pred_y2 - pred_h2/2.
pred_rect_x2=int(pred_xmin2*IMG_SIZE)
pred_rect_y2=int(pred_ymin2*IMG_SIZE)
pred_rect_w2=int(pred_w2*IMG_SIZE)
pred_rect_h2=int(pred_h2*IMG_SIZE)

pred_rect2=Rectangle((pred_rect_x2,pred_rect_y2),pred_rect_w2,pred_rect_h2,
                    fill=False,color='red')
plt.axes().add_patch(pred_rect2)
plt.imshow(img[0])
plt.show()
