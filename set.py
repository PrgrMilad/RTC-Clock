from machine import Pin, SoftSPI, SoftI2C
from pcf8563 import PCF8563

T_WATCH_I2C0_SCL = 5
T_WATCH_I2C0_SDA = 16



Now = [2024, 7, 24, 11, 6, 40, 2]
month_str = ["January", "February", "March", "April", "May", "June", "July",
             "Au    gust", "September", "October", "November", "December"]
month_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
day_of_week_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week_short = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
t_watch_i2c0 = SoftI2C(scl=Pin(T_WATCH_I2C0_SCL), sda=Pin(T_WATCH_I2C0_SDA))
pcf8563 = PCF8563(t_watch_i2c0)

pcf8563.set_datetime(Now)