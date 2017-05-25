##Chris Allen

from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.View.ViewConst import ViewConst
from API.MenuBar.Tools.ToolsConst import ToolsConst
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.MenuBar.Help.HelpConst import HelpConst

class MenuBarConst:
    fileconst = FileConst
    editconst = EditConst
    optionsconst = OptionsConst
    viewconst = ViewConst
    toolsconst = ToolsConst
    extensionsconst = ExtensionsConst
    helpconst = HelpConst
    MAIN_MENU_BAR = ':CAppWindowBase.m_pMenubar'
    FILE_MENU = ':File Menu'
    EDIT_MENU = ':Edit Menu'
    OPTIONS_MENU = ':Options Menu'
    VIEW_MENU = ':View Menu'
    TOOLS_MENU = ':Tools Menu'
    EXTENSIONS_MENU = ':Extensions Menu'
    HELP_MENU = ':Help Menu'