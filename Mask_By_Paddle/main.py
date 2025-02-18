import paddlehub as hub
import cv2

mask_detector = hub.Module(name="pyramidbox_lite_server_mask")

def mask_detecion(img):
  input_dict = {"data": [img]}
  result = mask_detector.face_detection(data=input_dict)
  count = len(result[0]['data'])
  if count < 1:
    #print('There is no face detected!')
    pass
  else:
    for i in range(0,count):
      #print(result[0]['data'][i])
      label = result[0]['data'][i].get('label')
      score = float(result[0]['data'][i].get('confidence'))
      x1 = int(result[0]['data'][i].get('left'))
      y1 = int(result[0]['data'][i].get('top'))
      x2 = int(result[0]['data'][i].get('right'))
      y2 = int(result[0]['data'][i].get('bottom'))
      cv2.rectangle(img,(x1,y1),(x2,y2),(255,200,0),2)
      if label == 'NO MASK':
        cv2.putText(img,label,(x1,y1),0,0.8,(0,0,255),2)
      else:
        cv2.putText(img,label,(x1,y1),0,0.8,(0,255,0),2)
  cv2.imshow('mask_detection',img)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  return result


if __name__ == '__main__':
  a=cv2.imread('mask_detection.mp4')
  print(type(a))

  cap = cv2.VideoCapture('mask_detection.mp4') #视频文件检测
  print(type(cap))
  cap = cv2.VideoCapture(0) #摄像头检测
  if(cap.isOpened()): #视频打开成功
    print("open success")
    while(True):
      ret,frame = cap.read()#读取一帧
      #print(type(frame))
      #print(frame.shape)
      result = mask_detecion(frame)
      #cv2.imshow('mask_detection',result)
      if cv2.waitKey(1)&0xFF ==27: #按下Esc键退出
        break
  else:
    print ('open video/camera failed!')
  cap.release()
  cv2.destroyAllWindows()


'''
  images=cv2.imread('train_2.jpg')
  result = mask_detecion(images)
  print(result)
'''
