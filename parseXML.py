import xml.etree.ElementTree as ET
import os

def parseFile(pathToXML):
    root = ET.parse(pathToXML).getroot()
    images = root.findall('image')

    for img in images:
        width = float(img.get('width'))
        height = float(img.get('height'))

        folder, file = img.get('name').replace('.jpg', '.txt').rsplit('/', 1)
        if not os.path.exists('./' + folder):
            os.makedirs(folder)
        file = open('./' + folder + '/' + file, "w+")

        boxes = img.findall('box')
        for box in boxes:
            result = ''
            box_label = 0 if box.get('label') == 'customer' else 1

            x_center = (float(box.get('xtl')) + float(box.get('xbr'))) / 2
            x0 = x_center / width

            y_center = (float(box.get('ytl')) + float(box.get('ybr'))) / 2
            y0 = y_center / height

            rec_width = (float(box.get('xbr')) - float(box.get('xtl')))
            w = rec_width / width

            rec_height = (float(box.get('ybr')) - float(box.get('ytl')))
            h = rec_height / height

            result += str(box_label) + ' ' + str(x0) + ' ' + str(y0) + ' ' + str(w) + ' ' + str(h) + '\n'
            print(result)
            file.writelines(result)


