from machine import I2C, Pin
from urtc import DS1307
import utime
from ssd1306 import SSD1306_I2C

i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
rtc = DS1307(i2c)

year = int(input("Year : "))
month = int(input("month (Jan --> 1 , Dec --> 12): "))
date = int(input("date : "))
day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
hour = int(input("hour (24 Hour format): "))
minute = int(input("minute : "))
second = int(input("second : "))

now = (year,month,date,day,hour,minute,second,0)
rtc.datetime(now)

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    utime.sleep(0.0001)
    print(rtc.datetime())
    
    s = str(rtc.datetime()[6])
    m = str(rtc.datetime()[5])
    h = str(rtc.datetime()[4])
    
    i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    oled.text("{}:{}:{}".format(h, m, s), 0, 0)
    oled.show()
    
    

