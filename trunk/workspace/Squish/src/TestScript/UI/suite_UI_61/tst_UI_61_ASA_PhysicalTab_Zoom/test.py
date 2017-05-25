##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.ComponentBox import ComponentBoxConst
from API.functions import check

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    create()
    checkZoom()
    
def create():
    a0.create()
    
def checkZoom():
    a0.select()
    
    image = a0.physical.imageObject
    height = image.height
    width = image.width
    a0.physical.zoomIn()
    compareValueRange(a0.physical.imageObject, height*2, width*2, 2)
    
    a0.physical.zoomOriginal()
    compareValueRange(a0.physical.imageObject, height, width, 0)
    
    a0.physical.zoomOut()
    compareValueRange(a0.physical.imageObject, height/1.5, width/1.5, 2)
    
def compareValueRange(obj, p_height, p_width, p_variance):
    if obj.height >= p_height - p_variance and obj.height <= p_height + p_variance:
        test.passes('Expected ' + str(p_height) + '\t Got ' + str(obj.height))
    else:
        test.fail('Expected ' + str(p_height) + '\t Got ' + str(obj.height))
    if obj.width >= p_width - p_variance and obj.width <= p_width + p_variance:
        test.passes('Expected ' + str(p_width) + '\t Got ' + str(obj.width))
    else:
        test.fail('Expected ' + str(p_width) + '\t Got ' + str(obj.width))
    