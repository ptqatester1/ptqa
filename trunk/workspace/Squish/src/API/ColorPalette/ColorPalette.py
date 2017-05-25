##Chris Allen

from API.Utility.Util import Util
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.ColorPalette.ColorPaletteConst import ColorPaletteConst

def err(msg = ''): raise NotImplementedError(msg)

class FillColor:
	'''With how PT is set up clicking specific colors can't be scripted'''
	def __init__(self):
		self.util = Util()
	
	def red(self, redVal):
		self.util.setText(ColorPaletteConst.selectColor.RED_VALUE, redVal)
	
	def green(self, greenVal):
		self.util.setText(ColorPaletteConst.selectColor.GREEN_VALUE, greenVal)
	
	def blue(self, blueVal):
		self.util.setText(ColorPaletteConst.selectColor.BLUE_VALUE, blueVal)
	
	def hue(self, hueVal):
		self.util.setText(ColorPaletteConst.selectColor.HUE_VALUE, hueVal)
	
	def sat(self, satVal):
		self.util.setText(ColorPaletteConst.selectColor.SAT_VALUE, satVal)
	
	def val(self, val):
		self.util.setText(ColorPaletteConst.selectColor.VAL_VALUE, val)
	
	def addCustomColorsButton(self):
		self.util.clickButton(ColorPaletteConst.selectColor.ADD_TO_CUSTOM_COLOR)
	
	def okButton(self):
		self.util.clickButton(ColorPaletteConst.selectColor.OK_BUTTON)
	
	def cancelButton(self):
		self.util.clickButton(ColorPaletteConst.selectColor.CANCEL_BUTTON)
	
	def setRgb(self, redVal, greenVal, blueVal):
		self.red(redVal)
		self.green(greenVal)
		self.blue(blueVal)
	
	def setHsv(self, hueVal, satVal, val):
		self.hue(hueVal)
		self.sat(satVal)
		self.val(val)
	
	def addCustomColor(self, r, g, b):
		self.red(r)
		self.green(g)
		self.blue(b)
		self.addCustomColorsButton()

class ColorPalette:
	def __init__(self):
		self.util = Util()
		self.fillColor = FillColor()
	def goToColorPalette(self):
		MainToolbar().paletteButton()
		None
	
	def freeFormButton(self):
		self.util.clickButton(ColorPaletteConst.POLYGON)
	
	def lineButton(self):
		self.util.clickButton(ColorPaletteConst.LINE)
	
	def ellipseButton(self):
		self.util.clickButton(ColorPaletteConst.ELLIPSE)
	
	def rectangleButton(self):
		self.util.clickButton(ColorPaletteConst.RECTANGLE)
	
	def outline(self, checked = None):
		checkbox = findObject(ColorPaletteConst.OUTLINE)
		if checked == None:
			self.util.click(checkbox)
		elif checked == True:
			if not checkbox.checked:
				self.util.click(checkbox)
		elif checked == False:
			if checkbox.checked:
				self.util.click(checkbox)
		else:
			raise ValueError('checked must be None, True, or False')
	
	def noFillRadio(self):
		self.util.clickButton(ColorPaletteConst.NO_FILL)
	
	def fillColorRadio(self):
		self.util.clickButton(ColorPaletteConst.FILL_COLOR)
	
	def selectOutlineColorButton(self):
		self.util.clickButton(ColorPaletteConst.SELECT_OUTLINE_COLOR)
	
	def selectFillColorButton(self):
		self.util.clickButton(ColorPaletteConst.SELECT_FILL_COLOR)
	
	def setFillColor(self, r, g, b):
		self.fillColorRadio()
		self.selectFillColorButton()
		self.fillColor.setRgb(r, g,	b)
		self.fillColor.okButton()
		