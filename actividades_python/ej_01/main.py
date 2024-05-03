from gpiozero import LED, Button
# traigo las clases LED y Button del modulo gpiozero
from signal import pause
# traigo la funcion pause  del modulo signal
led = LED(26)
# se declara el gpio 26 como correspondiente al led
button = Button(18)
# se declara el gpio 18 como correspondiente al button
button.when_pressed = led.on
# en este paso declaro que si se presiona el boton el led se encendera 
button.when_released = led.off
# aqui se dclara que cuando no este presionado el boton , el led se mantendra apagado
pause() 
# mantiene el programa en un bucle hasta que le doy una señal de salida
