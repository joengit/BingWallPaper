import json
import os
import urllib.request
import requests

url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"


try:
    json_data = requests.get(url).text
    image_data = json.loads(json_data)

    image_url_1920x1080 = 'http://www.bing.com' + \
        image_data['images'][0]['url']  # lower quality
    image_url_1920x1200 = 'http://www.bing.com/hpwp/' + \
        image_data['images'][0]['hsh']  # better quality with watermark
    image_url_UHD = image_url_1920x1080.replace("1920x1080", "UHD")
    image_name = image_data['images'][0]['enddate']

    dir_path = './'

    file_path_1920x1080 = dir_path + "1920x1080/" + image_name + '.jpg'
    file_path_1920x1200 = dir_path + "1920x1200/" + image_name + '.jpg'
    file_path_UHD = dir_path + "UHD/" + image_name + '.jpg'
    json_path = dir_path + "json/" + image_name + ".json"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(dir_path + "1920x1080/"):
        os.makedirs(dir_path + "1920x1080/")
    if not os.path.exists(dir_path + "1920x1200/"):
        os.makedirs(dir_path + "1920x1200/")
    if not os.path.exists(dir_path + "UHD/"):
        os.makedirs(dir_path + "UHD/")
    if not os.path.exists(dir_path + "json/"):
        os.makedirs(dir_path + "json/")

    if os.path.exists(file_path_1920x1080) is False:
        urllib.request.urlretrieve(
            image_url_1920x1080, filename=file_path_1920x1080)
    if os.path.exists(file_path_1920x1200) is False:
        urllib.request.urlretrieve(
            image_url_1920x1200, filename=file_path_1920x1200)
    if os.path.exists(file_path_UHD) is False:
        urllib.request.urlretrieve(image_url_UHD, filename=file_path_UHD)
    if os.path.exists(json_path) is False:
        with open(json_path, "wb+") as file:
            file.write(json_data.encode())

except:
    print("Error!")
