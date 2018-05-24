from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
locationPy = "C:/Users/10490/Desktop/ai/trans"
locationList = [locationPy + str(i) + ".pcm" for i in range (0,4)]
stringConbine = []
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
for piece in locationList:
	stringt = client.asr(get_file_content(piece), 'pcm', 16000, {'dev_pid': 1536,})
	stringConbine = stringConbine + stringt['result']

finalResult=''.join(stringConbine)
f = open('test.txt', 'w',encoding='utf-8')  
f.write(finalResult)  