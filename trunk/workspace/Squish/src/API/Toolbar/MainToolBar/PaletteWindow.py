##Chris Allen

from API.Toolbar.MainToolBar.PaletteWindowConst import PaletteWindowConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.ColorPalette.ColorPalette import ColorPalette
from API.Utility.Util import Util

class PaletteWindow:
    def __init__(self):
        self.util = Util()
        self.colorPalette = ColorPalette()
    
    def drawShapeWithDefaultColor(self, p_shape, p_fill, from_x, from_y, to_x, to_y):
        self.colorPalette.goToColorPalette()
        if p_fill == True:
            self.colorPalette.fillColorRadio()
        elif p_fill == False:
            self.colorPalette.noFillRadio()
        else:
            raise ValueError('p_fill should be True or False')
        if p_shape.lower() == 'line':
            self.colorPalette.lineButton()
        elif p_shape.lower() == 'polygon' or p_shape.lower() == 'freeform':
            self.colorPalette.freeFormButton()
        elif p_shape.lower() == 'rectangle':
            self.colorPalette.rectangleButton()
        elif p_shape.lower() == 'ellipse':
            self.colorPalette.ellipseButton()
        else:
            raise ValueError('p_shape should be rectangle, line, ellipse, or (polygon, freeform)')
        self.util.dragItemBy(self.util.currentWorkspace, from_x, from_y, to_x, to_y)
        CommonToolsBar().selectToolButton()