from DHT22 import DHT22
from machine import I2C, Pin
from urtc import DS1307
from ssd1306 import SSD1306_I2C
import utime

i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
dht22 = DHT22(Pin(22,Pin.IN,Pin.PULL_UP))
rtc = DS1307(i2c)

#uncomment to set time
"""year = int(input("Year : "))
month = int(input("month (Jan --> 1 , Dec --> 12): "))
date = int(input("date : "))
day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
hour = int(input("hour (24 Hour format): "))
minute = int(input("minute : "))
second = int(input("second : "))

now = (year,month,date,day,hour,minute,second,0)
rtc.datetime(now)"""

#Clock
i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    print(rtc.datetime())
    
    s = str(rtc.datetime()[6])
    m = str(rtc.datetime()[5])
    h = str(rtc.datetime()[4])
    d = str(rtc.datetime()[2])
    mnt = str(rtc.datetime()[1])
    T, H = dht22.read()
    oled.fill(0)
    oled.text("{}:{}:{}".format(h, m, s), 0, 1)
    oled.text("{}/{}".format(d, mnt), 0, 11)
    oled.text('H: ' +"{:0.0f}".format(H)+ "%", 0, 21)
    oled.text('T: ' +"{:0.1f}".format(T)+ "C", 0, 31)
    oled.show()
    
