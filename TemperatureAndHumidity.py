import grovepi #GrovePi cihazı için gerekli olan kütüphane tanımlandı.
import time
dht_sensor_port=4 #Sıcaklık ve Nem sensörü GrovePi cihazı üzerinde D4 portuna takılı.
dht_sensor_type=0 #Sıcaklık ve Nem sensörü DHT11 olduğu için type'ı 0, DHT22 olsaydı type'ı 1 olacaktı.
while True:
                [ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type) #Sensörden değerler okunuyor, sırasıyla temp ve hum değişkenlerine atılıyor.
                print 'Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) #temp ve hum değerleri ekrana yazdırılıyor.
                time.sleep(1)

        
   
