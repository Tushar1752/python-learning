#drinking water reminder program
import os
import time
Repeat = 10 
while True:
  command="osascript -e \'say \"Hely Tushar pani pilo\"\'; osascript -e\ 'display alert \"hello world\"\'"
  os.system(command)
  time.sleep(Repeat)