from flask import Flask,render_template
import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
pin = 23

@app.route('/')
def index():
    try:
        localtime = datetime.datetime.now()
        strTime = localtime.strftime("%Y. %m. %d")
        sensor = Adafruit_DHT.DHT11
        GPIO.setup(24,GPIO.IN)
        GPIO.setup(18,GPIO.OUT)
            
        value = GPIO.input(24)
        print("%s"%value)
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
            
        if value==True:
            GPIO.output(18,True)
            print ('현재 온도는 {0:0.1f}*C , 습도는 {1:0.1f}% 입니다!'.format(temperature, humidity))
            #dht=format(temperature, humidity)
            if humidity is not None and temperature is not None:
                dht="[Now Temperature:'" +"{0:0.1f}*C".format(temperature)+"', Now Humidity:'"+"{0:0.1f}%".format(humidity)+"']"
            else:
                dht="Failed to get reading. Try again!"
        else:
            GPIO.output(18,False)
            dht="If you want to know Tempature and Humidity, PRESS THE BUTTON ONE MORE! "
        
    except:
        #print("hi")
        dht ="Read error. Try again!"
        
    DHT = {'time':strTime, 'DHT':dht}
    
    return render_template('index2.html',**DHT)
GPIO.cleanup()        
##GPIO.setup(18, GPIO.OUT)GPIO.cleanup()
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
