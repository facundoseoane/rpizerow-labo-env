import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO para los LEDs RGB y el buzzer
LED_RED_PIN = 19
LED_GREEN_PIN = 13  # Corregido
LED_BLUE_PIN = 26    # Corregido
BUZZER_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Funciones para controlar los LEDs RGB y el buzzer
def set_led_color(color):
    GPIO.output(LED_RED_PIN, GPIO.LOW)
    GPIO.output(LED_GREEN_PIN, GPIO.LOW)
    GPIO.output(LED_BLUE_PIN, GPIO.LOW)
    if color == "red":
        GPIO.output(LED_RED_PIN, GPIO.HIGH)
    elif color == "green":
        GPIO.output(LED_GREEN_PIN, GPIO.HIGH)
    elif color == "blue":
        GPIO.output(LED_BLUE_PIN, GPIO.HIGH)

def buzz_on():
    print("Buzzer encendido")
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

def buzz_off():
    print("Buzzer apagado")
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Bucle principal para leer los comandos
while True:
    command = input("prompt: ").split()
    print("Comando ingresado:", command)
    if command[0] == "buzz":
        if command[1] == "on":
            buzz_on()
        elif command[1] == "off":
            buzz_off()
    elif command[0] == "rgb":
        color = input("Ingrese el color (red/green/blue): ")
        print("Color ingresado:", color)
        set_led_color(color)
