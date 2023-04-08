import event, halo, time
import time
# initialize variables
score = 0
cog = 0
items_list = []
halo.speech_recognition.set_recognition_address(url = "{NAVIGATEURL}")
halo.speech_recognition.set_access_token(token = "{ACCESSTOKEN}")

@event.start
def on_start():
    global score, cog, items_list
    score = 0
    cog = 0
    halo.wifi.start(ssid = "Galaxy A12BD74", password = "rxcr4527", mode = halo.wifi.WLAN_MODE_STA)
    while not halo.wifi.is_connected():
      # DO SOMETHING
      pass

    halo.led.show_all(1, 208, 39, 50)
    time.sleep(1)
    halo.led.off_all()

@event.touchpad0_active
def on_0_active():
    global score, cog, items_list
    cog = 0
    halo.led.show_ring('white white white white white white white white green white white white')
    halo.speech_recognition.begin(8, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('pen')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('pencil')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('bag')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('ruler')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('sharpener')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('eraser')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('compass')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('table')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('chair')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('fan')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('cupboard')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('book')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('paper')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('whiteboard')) > -1:
      cog = cog + 1

    if str(halo.speech_recognition.get_result_code()).find(str('marker')) > -1:
      cog = cog + 1

    halo.led.off_all()
    if cog > 5:
      halo.led.show_all(1, 208, 39, 50)
      time.sleep(1)
      halo.led.off_all()

    else:
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(1)
      halo.led.off_all()

@event.button_pressed
def on_button_pressed():
    global score, cog, items_list
    halo.speech_recognition.begin(2, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('red')) > -1:
      score = score + 1
      halo.led.show_all(1, 208, 39, 50)
      time.sleep(1)
      halo.led.off_all()

    else:
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(1)
      halo.led.off_all()

    time.sleep(1)
    halo.speech_recognition.begin(2, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('school')) > -1:
      score = score + 1
      halo.led.show_all(1, 208, 39, 50)
      time.sleep(1)
      halo.led.off_all()

    else:
      score = score + 1
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(1)
      halo.led.off_all()

    time.sleep(1)
    halo.speech_recognition.begin(2, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('singapore')) > -1:
      score = score + 1
      halo.led.show_all(1, 208, 39, 50)
      time.sleep(1)
      halo.led.off_all()

    else:
      score = score + 1
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(1)
      halo.led.off_all()

    time.sleep(1)
    halo.speech_recognition.begin(2, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('horses')) > -1:
      score = score + 1
      halo.led.show_all(1, 208, 39, 50)
      time.sleep(1)
      halo.led.off_all()

    else:
      score = score + 1
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(1)
      halo.led.off_all()

    time.sleep(1)
    halo.speech_recognition.begin(3, 'english')
    if str(halo.speech_recognition.get_result_code()).find(str('apple')) > -1:
      if str(halo.speech_recognition.get_result_code()).find(str('blue')) > -1:
        if str(halo.speech_recognition.get_result_code()).find(str('book')) > -1:
          score = score + 1
          halo.led.show_all(1, 208, 39, 50)
          time.sleep(1)
          halo.led.off_all()

    time.sleep(2)
    if score < 3:
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(2)
      halo.led.off_all()

    else:
      halo.led.show_all(124, 208, 0, 50)
      time.sleep(2)
      halo.led.off_all()

