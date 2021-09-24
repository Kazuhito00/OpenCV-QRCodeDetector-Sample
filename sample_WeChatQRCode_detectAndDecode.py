#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import time
import argparse

import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    args = parser.parse_args()

    return args


def main():
    # 引数解析 #################################################################
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    # カメラ準備 ###############################################################
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # Detector準備 #############################################################
    qrcode_detector = cv.wechat_qrcode_WeChatQRCode()

    elapsed_time = 0

    while True:
        start_time = time.time()

        # カメラキャプチャ #####################################################
        ret, image = cap.read()
        if not ret:
            break
        debug_image = copy.deepcopy(image)

        # 検出実施 #############################################################
        result = qrcode_detector.detectAndDecode(image)

        # 描画 ################################################################
        debug_image = draw_tags(debug_image, result, elapsed_time)

        elapsed_time = time.time() - start_time

        # キー処理(ESC：終了) #################################################
        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        # 画面反映 #############################################################
        cv.imshow('AprilTag Detect Demo', debug_image)

    cap.release()
    cv.destroyAllWindows()


def draw_tags(
    image,
    qrcode_result,
    elapsed_time,
):
    if len(qrcode_result[0]) > 0:
        qrcode_text = qrcode_result[0][0]
        qrcode_corners = qrcode_result[1]
        print(qrcode_corners)

        # テキスト
        cv.putText(image, str(qrcode_text), (10, 55), cv.FONT_HERSHEY_SIMPLEX,
                   0.75, (0, 255, 0), 2, cv.LINE_AA)

    # 処理時間
    cv.putText(image,
               "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
               cv.LINE_AA)

    return image


if __name__ == '__main__':
    main()
