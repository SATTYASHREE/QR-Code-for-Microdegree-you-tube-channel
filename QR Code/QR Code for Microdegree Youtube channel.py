#QR Code for Microdegree you tube channel

import pyqrcode
import png
channel_link= "https://youtu.be/01qSumyUrpU"
url = pyqrcode.create(channel_link)
url.svg("myqr.svg", scale =8)
url.png("myqr.png", scale= 6)
