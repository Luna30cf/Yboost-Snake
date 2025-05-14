from machine import Pin, PWM
import time

BUZZER_PIN = 1
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)

def play_tone(frequency, duration):
    """Joue une tonalité spécifique."""
    if frequency == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(frequency)
        buzzer.duty_u16(1500)

    time.sleep_ms(duration)
    buzzer.duty_u16(0) 

def play_victory_sound():
    """Joue un son de victoire."""
    melody = [1000, 1250, 1500, 1750, 2000] 
    duration = 200

    for note in melody:
        play_tone(note, duration)
    play_tone(0, 200) 

def play_game_over_sound():
    """Joue un son de game over."""
    melody = [1500, 1250, 1000, 750, 500]
    duration = 250

    for note in melody:
        play_tone(note, duration)
    play_tone(0, 500) 

# Test immédiat des sons
play_victory_sound()
time.sleep(1)
play_game_over_sound()
