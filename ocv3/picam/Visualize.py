import os, cv2, numpy

colornum = 12
colors = [(128,128,128),(128,0,0),(192,192,128),(255,69,0),(128,64,128),(60,40,222),(128,128,0),(192,128,128),(64,64,128),(64,0,128),(64,64,0),(0,128,192),(0,0,0)];

def Visualize(img, results, fps):
	img_cp = img.copy()
	detectedNum = len(results)
	cv2.putText(img_cp, "%.2ffps" % fps, (70, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
	if detectedNum > 0:
            for i in range(detectedNum):
                
                clr = colors[results[i].objType % colornum]
                txt = results[i].name

                left = results[i].left
                top = results[i].top
                right = results[i].right
                bottom = results[i].bottom

                cv2.rectangle(img_cp, (left,top), (right,bottom), clr, thickness=3)
                cv2.rectangle(img_cp, (left,top-20),(right,top),(255,255,255),-1)
                cv2.putText(img_cp,txt,(left+5,top-7),cv2.FONT_HERSHEY_SIMPLEX,0.5,clr,1)

	(ret, jpeg) = cv2.imencode('.jpg', img_cp)
	return jpeg.tobytes()

