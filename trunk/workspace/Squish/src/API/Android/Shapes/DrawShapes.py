from API.Android.Shapes.DrawShapesConst import DrawShapesConst
from API.Android.Utility.Util import Util
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu, ShapeSubMenuConst
from API.Android.Workspace.WorkspaceConst import WorkspaceConst
from squish import *
import test
import object

class DrawOptions:
	def __init__(self):
		self.util = Util()
		
	def selectShapeType(self, p_shapeType):
		self.util.tap(DrawShapesConst.SHAPE_TYPES)

		if p_shapeType == 'Rectangle':
			self.util.tap(DrawShapesConst.RECTANGLE)

		elif p_shapeType == 'Ellipse':
			self.util.tap(DrawShapesConst.ELLIPSE)

		elif p_shapeType == 'Line':
			self.util.tap(DrawShapesConst.LINE)


	def setFill(self, p_fillEnabled, p_fillColor = None):
		if findObject(DrawShapesConst.FILLENABLED).selected == p_fillEnabled:
			pass
		else:
			self.util.tap(DrawShapesConst.FILLENABLED)

		if p_fillColor == 'Red':
			self.util.tap(DrawShapesConst.SHAPEFILLCOLORS)
			self.util.tap(DrawShapesConst.FILL_COLOR_RED)

		elif p_fillColor == 'Green':
			self.util.tap(DrawShapesConst.SHAPEFILLCOLORS)
			self.util.tap(DrawShapesConst.FILL_COLOR_GREEN)

		elif p_fillColor == 'Blue':
			self.util.tap(DrawShapesConst.SHAPEFILLCOLORS)
			self.util.tap(DrawShapesConst.FILL_COLOR_BLUE)

		elif p_fillColor == 'Black':
			self.util.tap(DrawShapesConst.SHAPEFILLCOLORS)
			self.util.tap(DrawShapesConst.FILL_COLOR_BLACK)

		elif p_fillColor == 'White':
			self.util.tap(DrawShapesConst.SHAPEFILLCOLORS)
			self.util.tap(DrawShapesConst.FILL_COLOR_WHITE)


	def setOutline(self, p_outlineEnabled, p_outlineColor = None):
		if findObject(DrawShapesConst.OUTLINEENABLED).selected == p_outlineEnabled:
			pass
		else:
			self.uitl.tap(DrawShapesConst.OUTLINEENABLED)


		if p_outlineColor == 'Red':
			self.util.tap(DrawShapesConst.SHAPEOUTLINECOLORS)
			self.util.tap(DrawShapesConst.OUTLINE_COLOR_RED)

		elif p_outlineColor == 'Green':
			self.util.tap(DrawShapesConst.SHAPEOUTLINECOLORS)
			self.util.tap(DrawShapesConst.OUTLINE_COLOR_GREEN)

		elif p_outlineColor == 'Blue':
			self.util.tap(DrawShapesConst.SHAPEOUTLINECOLORS)
			self.util.tap(DrawShapesConst.OUTLINE_COLOR_BLUE)

		elif p_outlineColor == 'Black':
			self.util.tap(DrawShapesConst.SHAPEOUTLINECOLORS)
			self.util.tap(DrawShapesConst.OUTLINE_COLOR_BLACK)
			
		elif p_outlineColor == 'White':
			self.util.tap(DrawShapesConst.SHAPEOUTLINECOLORS)
			self.util.tap(DrawShapesConst.OUTLINE_COLOR_WHITE)
	
	def drawShape(self, p_x1, p_y1, p_x2, p_y2, p_shapeType, p_fillEnabled = False, p_fillColor = None, p_outlineEnabled = False, p_outlineColor = None):
		self.util.tapOnWorkspace(20, 20)
		self.util.tap(MainContextMenu.SHAPES)
        self.util.tap(ShapeSubMenuConst.OPTIONS)
        self.selectShapeType(p_shapeType)
        self.setFill(p_fillEnabled, p_fillColor)
        self.setOutline(p_outlineEnabled, p_outlineColor)
        self.util.tap(DrawShapesConst.HIDE_OPTIONS)
        self.touchAndDrag(WorkspaceConst.WORKSPACE, p_x1, p_y1, p_x2, p_y2)
        self.util.tapOnWorkspace(20, 20)
        self.tap(ShapeSubMenuConst.EXIT)