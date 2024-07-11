import os
import time
import ADS1x15
import math
from gpiozero import PWMLED


ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))


ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

k = 0.2

azul = PWMLED(26)
rojo = PWMLED(19)

while True :
    val_termistor = ADS.readADC(1)
    val_pote = ADS.readADC(3)
    volt_termistor = val_ter * f

    temp_pote = 30 * val_pote / 32767.5
    res_termistor = (volt_termistor * 10000) / (3.3 - volt_termistor)
    temp_termistor = (298 * 3900) / (298 * math.log(res_termistor / 10000) + 3900) - 273.15

    print(temp_termistor)
    print(temp_pote)

    dif = temp_termistor - temp_pote

    if dif > 0:
        if dif >= 5:
            dif = 5
        azul.value = dif * k
        rojo.off()
    elif dif < 0:
        if dif <= -5:
            dif = -5
        rojo.value = dif * k * -1
        azul.off()


    time.sleep(1)
