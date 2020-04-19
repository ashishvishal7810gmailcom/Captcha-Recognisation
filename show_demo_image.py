import cv2
import numpy as np
import pickle
model = pickle.load(open('new_emnist_model.sav', 'rb'))
finalans=[]

def predict_(image):
    image = image.reshape((1, image. shape[0], image.shape[1], 1))
    y_pred = model.predict(image)
    #print(y_pred)
    ynew = y_pred.argmax(axis=-1)
    #print(ynew)
    finalans.append(ynew)
    print(ynew)

def extract_segments(img, pad=20, area=100, threshold=150, ker=1):
    # thresholding the image
    ret, thresh1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    #thresh1 = 255 - thresh1
    #img = 255 - img
    cv2.imshow('thresh',thresh1)
    cv2.waitKey(0)
    # connected component labelling
    output = cv2.connectedComponentsWithStats(thresh1, 4)
    #print(output)
    final = []
    temp2 = output[2]
    temp2 = temp2[temp2[:, 4] > area]
    temp1 = np.sort(temp2[:, 0])
    kernel = np.ones([ker, ker])

    for i in range(1, temp2.shape[0]):
        cord = np.squeeze(temp2[temp2[:, 0] == temp1[i]])

        num = np.pad(thresh1[cord[1]:cord[1] + cord[3], cord[0]:cord[0] + cord[2]],pad)
        num=cv2.resize(num,(28,28))
        num = num.astype('float32')
        cv2.imshow('imae',num)
        cv2.waitKey(0)
        num=num/255
        final.append(num)
        predict_(num)

def image_show(img):
    def nothing(x):
        pass

    finalans.clear()
    barsWindow = 'Bars'
    hl = 'H Low'
    hh = 'H High'
    sl = 'S Low'
    sh = 'S High'
    vl = 'V Low'
    vh = 'V High'
    threshold='Threshold'
    w='width'
    h='height'
    e='erode fre'
    d='dialete fre'
    b='Back ground'
    cv2.namedWindow(barsWindow, flags=cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow(barsWindow, 400, 600);
    # create the sliders
    cv2.createTrackbar(threshold, barsWindow, 0, 255, nothing)
    cv2.createTrackbar(e, barsWindow, 0, 10, nothing)
    cv2.createTrackbar(d, barsWindow, 0, 10, nothing)
    cv2.createTrackbar(w, barsWindow, 0, 1500, nothing)
    cv2.createTrackbar(h, barsWindow, 0, 1500, nothing)
    cv2.createTrackbar(hl, barsWindow, 0, 360, nothing)
    cv2.createTrackbar(hh, barsWindow, 0, 255, nothing)
    cv2.createTrackbar(sl, barsWindow, 0, 255, nothing)
    cv2.createTrackbar(sh, barsWindow, 0, 360, nothing)
    cv2.createTrackbar(vl, barsWindow, 0, 255, nothing)
    cv2.createTrackbar(vh, barsWindow, 0, 255, nothing)
    cv2.createTrackbar(b, barsWindow, 0, 1, nothing)

    # code to change range of color
    #def tune_image(img):
        # set initial values for sliders
    cv2.setTrackbarPos(threshold, barsWindow, 100)
    cv2.setTrackbarPos(e, barsWindow, 3)
    cv2.setTrackbarPos(d, barsWindow, 2)
    cv2.setTrackbarPos(w, barsWindow,800)
    cv2.setTrackbarPos(h, barsWindow, 300)
    cv2.setTrackbarPos(hl, barsWindow, 0)
    cv2.setTrackbarPos(hh, barsWindow, 360)
    cv2.setTrackbarPos(sl, barsWindow, 0)
    cv2.setTrackbarPos(sh, barsWindow, 180)
    cv2.setTrackbarPos(vl, barsWindow, 0)
    cv2.setTrackbarPos(vh, barsWindow, 180)
    cv2.setTrackbarPos(b, barsWindow, 0)
    while (True):

        # read trackbar positions for all
        thresh = cv2.getTrackbarPos(threshold, barsWindow)
        ite = cv2.getTrackbarPos(e, barsWindow)
        itd = cv2.getTrackbarPos(d, barsWindow)
        width = cv2.getTrackbarPos(w, barsWindow)
        height = cv2.getTrackbarPos(h, barsWindow)
        hul = cv2.getTrackbarPos(hl, barsWindow)
        huh = cv2.getTrackbarPos(hh, barsWindow)
        sal = cv2.getTrackbarPos(sl, barsWindow)
        sah = cv2.getTrackbarPos(sh, barsWindow)
        val = cv2.getTrackbarPos(vl, barsWindow)
        vah = cv2.getTrackbarPos(vh, barsWindow)
        back_gounnd = cv2.getTrackbarPos(b, barsWindow)

        frame = cv2.resize(img, (width,height))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # make array for final values
        HSVLOW = np.array([hul, sal, val])
        HSVHIGH = np.array([huh, sah, vah])

        # apply the range on a mask
        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        maskedFrame=mask
        #maskedFrame = cv2.bitwise_and(frame, frame, mask=mask)
        fin_img = cv2.erode(maskedFrame, (3, 3), iterations=ite)
        #cv2.imshow('erode_img', fin_img)
        fin_img = cv2.dilate(fin_img, (3, 3), iterations=itd)
        # display the camera and masked images
        if(back_gounnd):
            fin_img=255-fin_img
        cv2.imshow('dialete img',fin_img)
        # cv2.waitKey(10)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            extract_segments(fin_img,20,thresh)
            sc = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r', 't']
            st = ""
            s = []
            for x in finalans:
                if (x <= 9):
                    c = 48 + x
                    st = st + chr(c)
                    s.append(chr(c))
                elif (x <= 35):
                    c = 65 + x - 10
                    st = st + chr(c)
                    s.append(chr(c))
                else:
                    ind = int(x) - 36
                    st = st + sc[ind]
                    s.append(sc[ind])
            cv2.destroyAllWindows()
            return st