
import time
import HandTrackingMOdule as htm
from djitellopy import tello


def initialize_the_drone():
    root = tello.Tello()
    root.connect()
    root.streamon()
    print("BATTERY:", root.get_battery())
    return root

def droneCommand(root):
    # print(len(overlayList))
    # pTime = 0
    detector = htm.handDetector(detectionCon=1)
    tipIds = [4, 8, 12, 16, 20] # thump, index, middle, ring, pink

    droneTakeOff = False
    dronePermission = True

    while True:
        img = root.get_frame_read().frame
        img = detector.findHands(img)

        # Get all the hand landmarks
        lmList = detector.findPosition(img, draw=False) # https://mediapipe.readthedocs.io/en/latest/solutions/hands.html

        if len(lmList) != 0:
            # print(lmList[tipIds[0]])
            # print(lmList[tipIds[0]][1], lmList[tipIds[0] - 1][1])
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(0)
            else:
                fingers.append(1)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    # print(lmList, lmList[tipIds[id]], "<", lmList[tipIds[id] - 2])
                    fingers.append(1)
                else:
                    fingers.append(0)

            if dronePermission:
                if not droneTakeOff:
                    print(fingers)
                    if fingers == [0, 0, 0, 0, 0]:
                        print("drone takeoff, please wait.")
                        droneTakeOff = True
                        root.takeoff()
                        root.send_rc_control(0, 0, 0, 0)

                elif droneTakeOff:
                    if fingers == [0, 0, 0, 0, 0]:
                        print("Drone landing, please wait.")
                        droneTakeOff = False
                        root.land()
                        root.end()

                    elif fingers == [1, 1, 1, 1, 1]:
                        print("Spinning!")
                        root.send_rc_control(0, 0, 0, 100)
                        time.sleep(4)
                        root.send_rc_control(0, 0, 0, 0)
                        print("Done!")

                    elif fingers == [0, 1, 0, 0, 0]:
                        # print("Pinpointing your index")
                        # print("Locking your index:", lmList[tipIds[1]])
                        if lmList[tipIds[1]][1] < 200:
                            print("Turn Left")
                            root.send_rc_control(100, 0, 0, 0)

                        if lmList[tipIds[1]][1] > 450:
                            print("Turn Right")
                            root.send_rc_control(-100, 0, 0, 0)

                        if lmList[tipIds[1]][2] > 200:
                            print("Go down")
                            root.send_rc_control(0, 0, -100, 0)

                        if lmList[tipIds[1]][2] < 90:
                            print("Go up")
                            root.send_rc_control(0, 0, 100, 0)









            # return fingers
            # totalFingers = fingers.count(1)
            # print(totalFingers)



        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # # print(f"1 / ({cTime} - {pTime}) = {fps}")
        #
        # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
        #             3, (255, 0, 0), 3)
        #
        # cv2.imshow("Image", img)
        # cv2.waitKey(1)

root = initialize_the_drone()
droneCommand(root)