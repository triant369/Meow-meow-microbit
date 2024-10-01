def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 0)
    for index in range(4):
        pins.servo_write_pin(AnalogPin.P2, 50)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P2, 90)
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_melody_ended():
    pins.digital_write_pin(DigitalPin.P1, 1)
music.on_event(MusicEvent.MELODY_ENDED, on_melody_ended)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P2, 0)
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_melody_note_played():
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(200)
music.on_event(MusicEvent.MELODY_NOTE_PLAYED, on_melody_note_played)

pins.digital_write_pin(DigitalPin.P1, 1)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
