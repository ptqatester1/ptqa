#**************************************************************************
#@author: Tuan Hoang, Thi Nguyen
#@summary: GoldenPhysicalToolbar handles golden toolbar in Physical Mode
#**************************************************************************
from API.ComponentBox import ComponentBoxConst
from API.SquishSyntax import SquishSyntax
from API.Utility import UtilConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from squish import *
import object

class BackgroundInputs:
    def __init__(self):
        self.clickButton = SquishSyntax().clickButton
        self.setText = SquishSyntax().setText
        self.click = SquishSyntax().click
        
    def setBackground(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND)
    
    def browse(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_BROWSE)
    
    def useOriginalImage(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_ORIGINAL_IMAGE)
    
    def displayTiledBackgroundImage(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_TILE_IMAGE_CHECKBOX)
    
    def resizeToFitCurrentView(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_RESIZE_TO_FIT_CURRENT_VIEW)
    
    def customSize(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_CUSTOM_SIZE_RADIO)
    
    def customSizeWidth(self, width):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_CUSTOM_SIZE_WIDTH, width)
    
    def customSizeHeight(self, height):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_CUSTOM_SIZE_HEIGHT, height)
    
    def width(self, width):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_PROPERTIES_WIDTH, width)
    
    def length(self, length):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_PROPERTIES_LENGTH, length)
    
    def height(self, height):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_PROPERTIES_HEIGHT, height)
    
    def scale(self, scale):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_SCALE_EDIT, scale)
    
    def reset(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_RESET)
        
    def apply(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_APPLY)
    
    def filename(self, filename):
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_FILE_DIALOG_EDIT, filename)
    
    def open(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_FILE_DIALOG_OPEN_BUTT)
        
    def cancel(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_FILE_DIALOG_CANCEL_BUTT)

    def backgroundImageTab(self):
        self.click(GoldenPhysicalToolbarConst.SET_BACKGROUND_TAB_BACKGROUND_IMAGE)
    
    def containerIconTab(self):
        self.click(GoldenPhysicalToolbarConst.SET_BACKGROUND_TAB_CONTAINER_ICON)
    
    def containerBrowse(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_CONTAINER_BROWSE)
    
    #ContainerFilename Open and Cancel share the same dialog for now but it would be best
    #to use these when working in the container tab in case that changes in the future
    def containerFilename(self, filename):
        self.filename(filename)
    
    def containerOpen(self):
        self.open()
    
    def containerCancel(self):
        self.cancel()
    
    def containerReset(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_CONTAINER_RESET)
    
    def containerApply(self):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_CONTAINER_APPLY)
        
    def close(self):
        SquishSyntax().close(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG)
        
class Background:
    def __init__(self):
        self.sq = SquishSyntax()
        self.inputs = BackgroundInputs()
        
    def setBackground(self, filename):
        self.selectBackground(filename)
        self.inputs.apply()
        self.inputs.close()
    
    def selectBackground(self, filename):
        if not object.exists(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG):
            self.inputs.setBackground()
        self.inputs.browse()
        self.inputs.filename(filename)
        self.inputs.open()
        
class GoldenPhysicalToolbar(SquishSyntax):
    #@summary: Jumps to location p_squishName of location type p_type in Navigation panel
    #@param p_squishName: Name of location
    #@param p_type: Type of location (i.e. Intercity, City, Building, or Wiring Closet)
    def jumpToSelectedLocation(self, p_name):
        self.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
        self.clickItem(GoldenPhysicalToolbarConst.NAVIGATION_LIST, p_name)
        self.clickButton(GoldenPhysicalToolbarConst.JUMP_TO_SELECTED_LOCATION)
        self.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    
    def wiringClosetButton(self):
        self.clickButton(GoldenPhysicalToolbarConst.WIRING_CLOSET_BUTTON)

    #@summary: This function move device to a location in physical workspace
    #@param p_name: display name of the object to move
    #@param p_type: type of object, device , wiring closet, building, city, or intercity
    #@param p_intercity_city_office_closet: Intercity_Home City_Corporate Office 
    #@param p_deviceModel: model of device
    #@param p_horizontal: horizontal value to scroll the bar to the device
    #@param p_vertical: vertical value to scroll the bar to the device

    def moveDevice(self, p_name, p_type, p_intercity_city_office_closet, p_deviceModel, p_horizontal, p_vertical):
        locationList = p_intercity_city_office_closet.split("_")
        print locationList
        self.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)
        device = GoldenPhysicalToolbarConst.RACK_DEVICE
        if p_deviceModel == ComponentBoxConst.DeviceModel.CABLE_MODEM:
            device = GoldenPhysicalToolbarConst.TABLE_DEVICE
        elif p_deviceModel == ComponentBoxConst.DeviceModel.DSL_MODEM:
            device = GoldenPhysicalToolbarConst.TABLE_DEVICE
        elif p_deviceModel == ComponentBoxConst.DeviceModel.PC:
            device = GoldenPhysicalToolbarConst.PC_DEVICE
        elif p_deviceModel == ComponentBoxConst.DeviceModel.PRINTER:
            device = GoldenPhysicalToolbarConst.TABLE_DEVICE          
        elif p_deviceModel == ComponentBoxConst.DeviceModel.LINKSYS:
            device = GoldenPhysicalToolbarConst.TABLE_DEVICE          
        #util.clickOnPhysicalWorkspace(p_horizontal, p_vertical)
        self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_H_SCROLL_BAR, p_horizontal)
        self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_V_SCROLL_BAR, p_vertical)
        self.click(device + p_name)
        dropdownObj = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
        for i in range(1, len(locationList)):      
            self.activateItem(dropdownObj, locationList[i])    
            dropdownObj = dropdownObj + "." + locationList[i]   
        print dropdownObj + "," + "Move to " + locationList[len(locationList)-1]             
        self.activateItem(dropdownObj, "Move to " + locationList[len(locationList)-1])

    #@summary: This function moves a rack device to a location in the physical workspace
    #@param p_rackNumber: Which rack the device is located (There are only 3 racks in each wiring closet)
    #@param p_deviceNumber: Which device on the rack is being moved (based on the current device ex. if you start with two and remove one the second becomes device one)
    #@param p_intercity_city_office_closet: Location where the device is being moved (Ex: "Intercity_1/Home City/Corporate Office")
    #@param p_horizontal: Horizontal value to scroll the bar to the device (optional)
    #@param p_vertical: Vertical value to scroll the bar to the device (optional)
    #@change: Changed from split("_") to split("/") because using split("_") causes Intercity_1 to be split into Intercity and 1 which is incorrect
    def moveRackDevice(self, p_rackNumber, p_deviceNumber, p_intercity_city_office_closet, p_horizontal = 0, p_vertical = 0):
        locationList = p_intercity_city_office_closet.split("/")
        #Currently intercity_1 doesn't need to be included in the path
        if 'Intercity_1' in locationList:
            #locationList.remove('Intercity_1')
            locationList[locationList.index('Intercity_1')] = 'Intercity'
        print locationList
        self.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)       
        if p_horizontal:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_H_SCROLL_BAR, p_horizontal)
        if p_vertical:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_V_SCROLL_BAR, p_vertical)
        rackDevice = GoldenPhysicalToolbarConst.RACK_BASE + str(p_rackNumber) + GoldenPhysicalToolbarConst.RACK_DEVICE_BASE + str(p_deviceNumber)
        self.click(rackDevice)
        dropdownObj = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
        #For each location activate the menu item and then append the location to the menu object name
        for i in range(len(locationList)):
            if len(locationList) == 1:
                snooze(1)
                location = locationList.pop(0)
                self.activateItem(dropdownObj, 'Move to ' + location)
            else:
                location = locationList.pop(0)
                self.activateItem(dropdownObj, location)
                dropdownObj += '.' + location
                snooze(1)        

    def moveRackDeviceToIntercity(self, p_rackNumber, p_deviceNumber, p_horizontal = 0, p_vertical = 0):
        self.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)       
        if p_horizontal:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_H_SCROLL_BAR, p_horizontal)
        if p_vertical:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_V_SCROLL_BAR, p_vertical)
        rackDevice = GoldenPhysicalToolbarConst.RACK_BASE + str(p_rackNumber) + GoldenPhysicalToolbarConst.RACK_DEVICE_BASE + str(p_deviceNumber)
        self.click(rackDevice)
        dropdownObj = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
        self.activateItem(dropdownObj, 'Move to Intercity')
    
    #Move a device from one location to another
    #p_dev is the device to move
    #    p_dev can be the device object or the squish object name
    #    p_moveTo is where to move the device to 
    def changeLocation(self, p_dev, p_moveTo, p_horizontal = None, p_vertical = None):
        locationList = p_moveTo.split("/")
        #Currently intercity_1 doesn't need to be included in the path
        if 'Intercity_1' in locationList:
            #locationList.remove('Intercity_1')
            locationList[locationList.index('Intercity_1')] = 'Intercity'
        self.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)
        if p_horizontal:
            pass#Needs implemented
        if p_vertical:
            pass#Needs implemented
        try:
            p_dev = findObject(p_dev)
        except TypeError, e:
            pass
        except Exception, e:
            raise Exception(e)
        self.click(p_dev)
        dropdownObj = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
        for i in range(len(locationList)):
            if len(locationList) == 1:
                snooze(1)
                location = locationList.pop(0)
                self.activateItem(dropdownObj, 'Move to ' + location)
            else:
                location = locationList.pop(0)
                self.activateItem(dropdownObj, location)
                dropdownObj += '.' + location
                snooze(1) 
        None
                
    #@summary: This function moves a table device to a location in the physical workspace
    #@param p_tableNumber: Which table the device is located (There are only 3 tables in each wiring closet)
    #@param p_deviceNumber: Which device on the table (There are only 2 devices on each table) is being moved
    #@param p_intercity_city_office_closet: Location where the device is being moved (Ex: "Intercity_Home City_Corporate Office")
    #@param p_horizontal: Horizontal value to scroll the bar to the device
    #@param p_vertical: Vertical value to scroll the bar to the device
    def moveTableDevice(self, p_tableNumber, p_deviceNumber, p_intercity_city_office_closet, p_horizontal = 0, p_vertical = 0):
        locationList = p_intercity_city_office_closet.split("/")
        if 'Intercity_1' in locationList:
            locationList.remove('Intercity_1')        
        print locationList
        self.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)       
        if p_horizontal:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_H_SCROLL_BAR, p_horizontal)
        if p_vertical:
            self.scrollTo(GoldenPhysicalToolbarConst.RACK_VIEW_V_SCROLL_BAR, p_vertical)
#         if (p_tableNumber == 1 and p_deviceNumber == 1):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE1_DEVICE1
#         elif (p_tableNumber == 1 and p_deviceNumber == 2):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE1_DEVICE2
#         elif (p_tableNumber == 2 and p_deviceNumber == 1):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE2_DEVICE1
#         elif (p_tableNumber == 2 and p_deviceNumber == 2):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE2_DEVICE2
#         elif (p_tableNumber == 3 and p_deviceNumber == 1):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE3_DEVICE1
#         elif (p_tableNumber == 3 and p_deviceNumber == 2):
#             tableDevice = GoldenPhysicalToolbarConst.TABLE3_DEVICE2
        if p_tableNumber == 1:
            tableDevice = GoldenPhysicalToolbarConst.TABLE1_DEVICE1.replace('QWidget1', 'QWidget' + str(p_deviceNumber))
        elif p_tableNumber == 2:
            tableDevice = GoldenPhysicalToolbarConst.TABLE2_DEVICE1.replace('QWidget1', 'QWidget' + str(p_deviceNumber))
        else:
            tableDevice = GoldenPhysicalToolbarConst.TABLE_BASE + str(p_tableNumber) + GoldenPhysicalToolbarConst.TABLE_DEVICE_BASE + str(p_deviceNumber) + GoldenPhysicalToolbarConst.TABLE_END
        self.click(tableDevice)
        dropdownObj = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
        for i in range(len(locationList)):
            if len(locationList) == 1:
                snooze(1)
                location = locationList.pop(0)
                self.activateItem(dropdownObj, 'Move to ' + location)
            else:
                location = locationList.pop(0)
                self.activateItem(dropdownObj, location)
                dropdownObj += '.' + location
                snooze(1)
        
    #@summary: Enables the grid for Intercity with scales p_x and p_y
    #@note: To disable the grid, pass in any valid values for p_x and p_y
    #@param p_x: Grid-X (m) value
    #@param p_y: Grid-Y (m) value
    def setGridIntercity(self, p_x, p_y):
        self.click(GoldenPhysicalToolbarConst.GRID)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_INTERCITY_CHECKBOX)
        self.setText(GoldenPhysicalToolbarConst.GRID_INTERCITY_X, p_x)
        self.setText(GoldenPhysicalToolbarConst.GRID_INTERCITY_Y, p_y)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_DIALOG_OK)

    #@summary: Enables the grid for City with scales p_x and p_y
    #@note: To disable the grid, pass in any valid values for p_x and p_y
    #@param p_x: Grid-X (m) value
    #@param p_y: Grid-Y (m) value
    def setGridCity(self, p_x, p_y):
        self.click(GoldenPhysicalToolbarConst.GRID)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_CITY_CHECKBOX)
        self.setText(GoldenPhysicalToolbarConst.GRID_CITY_X, p_x)
        self.setText(GoldenPhysicalToolbarConst.GRID_CITY_Y, p_y)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_DIALOG_OK)

    #@summary: Enables the grid for Building with scales p_x and p_y
    #@note: To disable the grid, pass in any valid values for p_x and p_y
    #@param p_x: Grid-X (m) value
    #@param p_y: Grid-Y (m) value
    def setGridBuilding(self, p_x, p_y):
        self.click(GoldenPhysicalToolbarConst.GRID)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_BUILDING_CHECKBOX)
        self.setText(GoldenPhysicalToolbarConst.GRID_BUILDING_X, p_x)
        self.setText(GoldenPhysicalToolbarConst.GRID_BUILDING_Y, p_y)
        self.clickButton(GoldenPhysicalToolbarConst.GRID_DIALOG_OK)

    #@summary: Sets background image p_imagePath in backgroounds subdirectory p_imageLocation
    #@param p_imagePath: Path to the image
    #@param p_imageLocation: Logical, Intercity, City, or Building
    def setBackgroundImage(self, p_imageLocation, p_imagePath):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND)
        for i in range(0, 20):
            p_text = str(findObject(GoldenPhysicalToolbarConst.SET_BACKGROUND_LIST + ".item_" + str(i) + "/1").text)
            if(p_imagePath == p_text):
                self.clickItem(GoldenPhysicalToolbarConst.SET_BACKGROUND_LIST, str(i)+"/1")
                break
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_APPLY)
        self.close(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG)
        
    #@summary: Sets background image p_imagePath in backgroounds subdirectory p_imageLocation
    #@param p_imagePath: Path to the image
    #@param p_imageLocation: Logical, Intercity, City, or Building
    def setTiledBackgroundImage(self, p_image, p_imageX, p_imageY):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND)
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_TILE_IMAGE_CHECKBOX)
        #self.clickItem(GoldenPhysicalToolbarConst.SET_BACKGROUND_LIST, p_imageLocation + "|" + p_imagePath + "|")
        self.clickItem_x_y(GoldenPhysicalToolbarConst.SET_BACKGROUND_LIST, p_image, p_imageX, p_imageY)
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_APPLY)
        self.close(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG)

    #@summary: Sets background image p_imagePath in backgroounds subdirectory p_imageLocation
    #@param p_imagePath: Path to the image
    #@param p_imageLocation: Logical, Intercity, City, or Building
    def setBackgroundBrowseImage(self, p_imagePath):
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND)
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_BROWSE)
        self.setText(GoldenPhysicalToolbarConst.SET_BACKGROUND_FILE_DIALOG_EDIT, p_imagePath)
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_FILE_DIALOG_OPEN_BUTT)
        self.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND_APPLY)
        self.close(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG)
    
    def setCustomSize(self, p_width, p_height):
        None
        
    #@summary: group several cables together
    #@param p_start_point_list: x-y coordinations of all the bendpoints [(300,400), (500, 600), (100, 200)]
    #@param p_end_point: x-y coordination of the endpoint(200, 100)
    def groupCable(self, p_start_point_list, p_end_point):
        #create bend point on the cable
        menu_num = 1
        self.click_x_y(UtilConst.ICON2_PHYSICAL_WORKSPACE, p_end_point[0], p_end_point[1])
        self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu" + str(menu_num) , "Create BendPoint")
        #self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu1" , "Create BendPoint")
        for point in p_start_point_list:
            menu_num +=1
            self.click_x_y(UtilConst.ICON2_PHYSICAL_WORKSPACE, point[0], point[1])
            self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu" + str(menu_num), "Create BendPoint")
            #self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu1", "Create BendPoint")
            self.dragAndDrop(UtilConst.ICON2_PHYSICAL_WORKSPACE, point[0], point[1], UtilConst.ICON2_PHYSICAL_WORKSPACE, p_end_point[0], p_end_point[1])
    
    
    #@summary: add  bendpoint
    #@param p_bendpoint_list: x-y coordinations of all the bendpoints [(300,400), (500, 600), (100, 200)]
    def addBendpoint(self, p_bendpoint_list):
        #create bend point on the cable
        menu_num = 1
        for point in p_bendpoint_list:
            self.click_x_y(UtilConst.ICON2_PHYSICAL_WORKSPACE, point[0], point[1])
            self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu" + str(menu_num), "Create BendPoint")
            menu_num +=1
            #self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu1" , "Create BendPoint")
            
    #@summary: change Color of cables
    def changeCableColor(self, p_cable_list, p_red, p_green, p_blue):
        menu_num = 1   
        for point in p_cable_list:
            menu_num +=1
            self.click_x_y(UtilConst.ICON2_PHYSICAL_WORKSPACE, point[0], point[1])
            #self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu" + str(menu_num), "Color Cable")
            self.activateItem(UtilConst.ICON2_PHYSICAL_WORKSPACE + ".QMenu1", "Color Cable")
            self.setText(GoldenPhysicalToolbarConst.SELECT_COLOR_RED, p_red)
            self.setText(GoldenPhysicalToolbarConst.SELECT_COLOR_GREEN, p_green)
            self.setText(GoldenPhysicalToolbarConst.SELECT_COLOR_BLUE, p_blue)
            self.clickButton(GoldenPhysicalToolbarConst.SELECT_COLOR_OK)   
            
    def moveBendpoint(self, p_x1, p_y1, p_x2, p_y2):
        self.dragAndDrop(UtilConst.ICON2_PHYSICAL_WORKSPACE, p_x1, p_y1, UtilConst.ICON2_PHYSICAL_WORKSPACE, p_x2, p_y2)   
    
    def newGenericContainer(self):
        self.clickButton(GoldenPhysicalToolbarConst.NEW_GENERIC_CONTAINER)
        
    def newCloset(self):
        self.clickButton(GoldenPhysicalToolbarConst.NEW_CLOSET)
        
    def newBuilding(self):
        self.clickButton(GoldenPhysicalToolbarConst.NEW_BUILDING)
        
    def newCity(self):
        self.clickButton(GoldenPhysicalToolbarConst.NEW_CITY)
        
    def workingCloset(self):
        self.clickButton(GoldenPhysicalToolbarConst.WORKING_CLOSET)
