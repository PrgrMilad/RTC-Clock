from machine import Pin, SoftSPI, SoftI2C
import max7219
from pcf8563 import PCF8563
import utime
T_WATCH_I2C0_SCL = 5
T_WATCH_I2C0_SDA = 16


DIN_PIN = 15
CS_PIN = 2
CLK_PIN = 0
pm=0


Now = [2024, 7, 24, 17, 9, 20, 2]
month_str = ["January", "February", "March", "April", "May", "June", "July",
             "Au    gust", "September", "October", "November", "December"]
month_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
day_of_week_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week_short = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
t_watch_i2c0 = SoftI2C(scl=Pin(T_WATCH_I2C0_SCL), sda=Pin(T_WATCH_I2C0_SDA))
pcf8563 = PCF8563(t_watch_i2c0)
# pcf8563.set_datetime(Now)

spi = SoftSPI(baudrate=10000000, polarity=0, phase=0, sck=Pin(CLK_PIN), mosi=Pin(DIN_PIN), miso=Pin(4))

num_matrices = 1

display = max7219.Matrix8x8(spi, Pin(CS_PIN), num_matrices)
display.brightness(2)

def set_led(x, y, state):
    display.pixel(x, y, state)
    display.show()

print("runed")

def print_current_time(x):
    currentTime = pcf8563.datetime()
    return int(currentTime[x])
def minute():

    if print_current_time(5)<3 and print_current_time(5)>=0 :
        set_led(7,0,1)
    elif print_current_time(5)<8 and print_current_time(5)>=3:
        set_led(7,1,1)
    elif print_current_time(5)<13 and print_current_time(5)>=8:
        set_led(7,2,1)
    elif print_current_time(5)<18 and print_current_time(5)>=13:
        set_led(7,3,1)
    elif print_current_time(5)<23 and print_current_time(5)>=18:
        set_led(7,4,1)
    elif print_current_time(5)<28 and print_current_time(5)>=23:
        set_led(7,5,1)
    elif print_current_time(5)<33 and print_current_time(5)>=28:
        set_led(7,6,1)
    elif print_current_time(5)<38 and print_current_time(5)>=33 :
        set_led(7,7,1)
    elif print_current_time(5)<43 and print_current_time(5)>=38 :
        set_led(6,7,1)
    elif print_current_time(5)<48 and print_current_time(5)>=43:
        set_led(5,7,1)
    elif print_current_time(5)<53 and print_current_time(5)>=48:
        set_led(4,7,1)
    elif print_current_time(5)<58 and print_current_time(5)>=53:
        set_led(3,7,1)
    elif print_current_time(5)<60 and print_current_time(5)>=58:
        set_led(2,7,1)
    if print_current_time(5)<60 and print_current_time(6)==59:
        set_led(2,7,0)
        set_led(3,7,0)
        set_led(4,7,0)
        set_led(5,7,0)
        set_led(6,7,0)
        set_led(7,7,0)
        set_led(7,6,0)
        set_led(7,5,0)
        set_led(7,4,0)
        set_led(7,3,0)
        set_led(7,2,0)
        set_led(7,1,0)
        set_led(7,0,0)

def hourr():
    if print_current_time(6) ==0:
        set_led(2,0,0)
        set_led(3,0,0)
        set_led(4,0,0)
        set_led(5,0,0)
        set_led(1,0,0)
        set_led(0,0,0)
        set_led(0,6,0)
        set_led(0,5,0)
        set_led(0,4,0)
        set_led(0,3,0)
        set_led(0,2,0)
        set_led(0,1,0)

    if print_current_time(4)>12:
        hour = print_current_time(4)-12
        set_led(0,7,1)
        pm = 1
    else:
        hour = print_current_time(4)
    if hour==1:
        set_led(5,0,1)
    elif hour==2:
        set_led(4,0,1)
    elif hour==3:
        set_led(3,0,1)
    elif hour==4:
        set_led(2,0,1)
    elif hour==5:
        set_led(1,0,1)
    elif hour==6:
        set_led(0,0,1)
    else:
        set_led(0,hour-6,1)
    if print_current_time(5) == 59 and print_current_time(6) == 59 and hour==12 and pm==1:
        for i in range(8):
            for j in range(8):
                set_led(i, j, 0)
    elif print_current_time(5) == 59 and print_current_time(6) == 59 and hour==12 and pm!=1:
        pass

while True:
    hourr()
    minute()
    currentTime = pcf8563.datetime()
    print(currentTime)
    set_led(3,3,1)
    set_led(4,4,1)
    set_led(3,4,1)
    set_led(4,3,1)
    utime.sleep(0.07)
    set_led(3,3,0)
    set_led(4,4,0)
    set_led(3,4,0)
    set_led(4,3,0)
    utime.sleep(0.93)
