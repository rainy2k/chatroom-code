import os
from gtts import gTTS

# 将文本转换为语音
tts = gTTS('Hello, World!')
tts.save('hello.mp3')

# 播放语音
os.system('afplay hello.mp3')
