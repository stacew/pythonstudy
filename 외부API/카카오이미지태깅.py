import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os


API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate'
MYAPP_KEY = os.environ['KAKAO_REST_API_KEY']

def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)

        print('응답 받은 값 >>', resp)
        resp.raise_for_status()


        print('비전 kakao 서버와 연결 OK..')
        print(resp.content)


        result = resp.json()['result']
        if len(result['label_kr']) > 0:
            if type(result['label_kr'][0]) != str:
                result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr'])))
        else:
            print("이미지로부터 태그를 생성하지 못했습니다.")

    except Exception as e:
        print(str(e))
        sys.exit(0)

# if __name__ == "__main__":
def main(site):
    parser = argparse.ArgumentParser(description='Classify Tags')
    parser.add_argument('image_url', type=str, nargs='?',
        default=site,
        help='image url to classify')

    args = parser.parse_args()

    generate_tag(args.image_url)

img_list = ['http://blogfiles.naver.net/MjAxODAyMTRfMjU5/MDAxNTE4NTc4MDUxMDgx.koRmcIvs1YXsG05ZTlMMdKaCxkmN2ERCz_QExgjO8A4g.BAYu5TTIp7Ri9fPYB3-lPIBlXCiGuv-R_IC8pWO9Et0g.JPEG.dok1503/36.jpg',
            'http://blogfiles.naver.net/20091028_278/ytbae50_1256731440450kCMN4_jpg/4_ytbae50.jpg',
            'http://blogfiles.naver.net/20140619_63/kilsoo42_1403153956711usVqm_JPEG/%C7%B3%B0%E615.jpg',
            'http://blogfiles.naver.net/data43/2009/4/21/170/%C7%B3%B0%E6-18_wooyun8.jpg',
            'http://blogfiles.naver.net/data6/2004/11/1/238/carli25-mijeong8013.jpg']

for x in img_list:
    main(x)