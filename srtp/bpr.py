# -*- coding: utf-8 -*-
import serial
import time
import threading
SLEEP_Cmd = [0xff, 0xcd, 0x03, 0xae, 0xab]
WAKEUP_Cmd = [0xff, 0xcd, 0x03, 0xad, 0xaa]
START_Cmd = [0xff, 0xcd, 0x03, 0xa3, 0xa0]
STOP_Cmd = [0xff, 0xcd, 0x03, 0xa6, 0xa3]

START_STATE = 0
STOP_STATE = 1
SLEEP_STATE = 2
WAKEUP_STATE = 3

STATUS_NORMAL_INFO = "設備已經連接!"
STATUS_ERROR_INFO_0 = "報告: 測量不到有效的脈搏!"
STATUS_ERROR_INFO_1 = "報告: 氣袋沒有綁好!"
STATUS_ERROR_INFO_2 = "報告: 測量結果數值有誤!"
STATUS_ERROR_INFO_3 = "報告: 進入超壓保護!"
STATUS_ERROR_INFO_4 = "報告: 幹預過多!"


class bpsensor:

    def __init__(self, port):
        self.ser = serial.Serial(
            port=None,              # number of device, numbering starts at
            # zero. if everything fails, the user
            # can specify a device string, note
            # that this isn't portable anymore
            # if no port is specified an unconfigured
            # an closed serial port object is created
            baudrate=115200,          # baud rate
            bytesize=8,     # number of databits
            parity=serial.PARITY_NONE,     # enable parity checking
            stopbits=serial.STOPBITS_ONE,  # number of stopbits
            timeout=3,           # set a timeout value, None for waiting forever
            xonxoff=0,              # enable software flow control
            rtscts=0,               # enable RTS/CTS flow control
            interCharTimeout=None   # Inter-character timeout, None to disable
        )
        self.ser.port = port
        self.RecBuff = [0 for i in range(10)]
        self.RecIndex = 0
        self.data_len = 0
        self.strInfo = ""
        self.status = 1
        self.done = False

    def __del__(self):
        self.close()

    def getdata(self, ch):
        self.strInfo = ""
        bRefreshDisp = False
        self.done = False
        val = 0
        self.RecBuff[self.RecIndex] = ch

        if self.RecIndex == 0:
            if self.RecBuff[0] != 0xff:
                self.RecIndex = 0
                return -1

        elif self.RecIndex == 1:
            if self.RecBuff[1] != 0xcd:

                self.RecIndex = 0
                return -1

        elif self.RecIndex == 2:
            self.data_len = self.RecBuff[2] - 1
            if self.data_len > 7 or self.data_len < 2:

                self.RecIndex = 0
                return -2

        else:
            self.data_len -= 1
            if self.data_len == 0:

                # 数据接收完成
                # 校验
                verify = self.RecBuff[2]
                for i in range(self.RecBuff[2] - 2):

                    verify += self.RecBuff[4 + i]

                if ((verify & 0xff) != self.RecBuff[3]):
                    self.RecIndex = 0
                    return -3

                # 提取有用数据,判断命令字

                if self.RecBuff[4] == 0x5b:  # 传感器休眠
                    self.strInfo = "已休眠"
                    self.status = SLEEP_STATE
                    self.RecIndex = 0
                    return 0
                elif self.RecBuff[4] == 0x5a:  # 唤醒
                    self.strInfo = "已唤醒"
                    self.status = WAKEUP_STATE
                    self.RecIndex = 0
                    return 0
                elif self.RecBuff[4] == 0x54:  # 测量阶段
                    self.bDeviceAck = True

                    if ((self.RecBuff[5] and 0x10) == 1):

                        self.strInfo = "有心跳"
                    else:

                        self.strInfo = "无心跳"

                    # 气压值
                    bRefreshDisp = True
                    self.val = self.RecBuff[5] & 0x0f
                    self.val = (val << 8) | self.RecBuff[6]
                elif self.RecBuff[4] == 0x55:  # 血压值
                    if ((self.RecBuff[5] and 0x80) == 1):

                        # 心律不齐
                        self.strInfo = "心律不齐!"
                        self.m_wMP = 1
                    else:

                        # 心率正常
                        self.strInfo = "心率正常!"
                        self.m_wMP = 0

                    self.RecBuff[5] &= 0x7f  # 把最高位 心率位去掉

                    #收缩压
                    val = (self.RecBuff[5] << 8) | self.RecBuff[6]
                    # strInfo.Format("%d",val)
                    self.m_wSP = val

                    #舒张压压
                    val = (self.RecBuff[7] << 8) | self.RecBuff[8]
                    # strInfo.Format("%d",val);
                    self.m_wDP = val

                    # 心率
                    # strInfo.Format("%d",RecBuff[9]);
                    self.m_wPR = self.RecBuff[9]
                    self.done = True
                    return self.m_wSP, self.m_wDP, self.m_wPR

                elif self.RecBuff[4] == 0x56:

                    if(self.RecBuff[5] == 0):
                        self.strInfo = STATUS_ERROR_INFO_0

                    elif self.RecBuff[5] == 1:
                        self.strInfo = STATUS_ERROR_INFO_1

                    elif self.RecBuff[5] == 2:
                        self.strInfo = STATUS_ERROR_INFO_2

                    elif self.RecBuff[5] == 3:
                        self.strInfo = STATUS_ERROR_INFO_3

                    elif self.RecBuff[5] == 4:
                        self.strInfo = STATUS_ERROR_INFO_4

                    else:
                        self.strInfo = "報告: 未知錯誤!"

                        return -4
                else:
                    return -5
                bRefreshDisp = True

        self.RecIndex += 1

        if (bRefreshDisp):

            bRefreshDisp = False

            self.RecIndex = 0

        return 0

    def sleep(self):
        if self.ser.isOpen():
            self.ser.write(SLEEP_Cmd)

    def wakeup(self):
        if(self.ser.isOpen() and self.status != WAKEUP_STATE):
            self.ser.write(WAKEUP_Cmd)
            self.status = WAKEUP_STATE

    def start(self):
        if(self.ser.isOpen() and self.status != START_STATE):
            self.ser.write(START_Cmd)
            time.sleep(0.5)
            self.ser.write(START_Cmd)
            i = 0
            time.sleep(2)
            while self.done is False:
                temp = self.ser.read()
                if temp != 0 and temp != b'':
                    temp = ord(temp)
                    self.getdata(temp)
                else:
                    i += 1
                if i > 3:
                    break

            if(self.done):
                print(self.m_wSP, self.m_wDP, self.m_wPR)
                # self.done=False
            else:
                print(self.strInfo)

    def open(self):
        if not self.ser.isOpen():
            self.ser.open()

    def close(self):
        if self.ser.isOpen():
            self.ser.close()


if __name__ == "__main__":
    a = bpsensor('/dev/ttyUSB0')
    a.open()
    a.start()
