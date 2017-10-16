import os
import io
import sys
import re
import time
import requests
import PyPDF2

from wand.image import Image

# import modules.mncf_helper as mncf_helper
# from utils import utils
# from people_names import people_names
# from bs4 import BeautifulSoup
#
# from PIL import Image
#
# import pyocr
# import pyocr.builders

# try:
#     import Image
# except ImportError:
#     from PIL import Image, ImageEnhance, ImageFilter
# import pytesseract

# from __future__ import print_function
# from wand.image import Image

# import modules.psql.candidates as candidates_model
my_filename = './scripts/betsy.pdf'
# my_filename = './scripts/betsy-page-005_copy.jpg'

def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def main(args):

    all_pages = Image(filename=my_filename)        # PDF will have several pages.
    # single_image = all_pages.sequence[0]    # Just work on first page
    with Image(filename=my_filename) as i:
        i.format = 'JPEG'
        i.background_color = Color('white') # Set white background.
        i.alpha_channel = 'remove'          # Remove transparency and replace with bg.


    # jpeg_bytes = io.BytesIO()
    # with Image(filename=my_filename) as img:
    #     print('pages = ', len(img.sequence))
    #     img.save(jpeg_bytes, "jpeg")

        # with img.convert('JPEG') as converted:
        #     converted.save(filename='page.jpg')

            # image_pdf.convert('JPEG')


    # result = ocr_space_file(my_filename, False, '87e1161bdf88957')
    # text = result['ParsedResults'][0]['ParsedText']
    # print (text)


    # with Image(filename=my_filename) as img:
    #      img.save(filename="temp.jpg")


if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
