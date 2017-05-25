'''class MainViewConst:
	PT_MOBILE_WEBVIEW = ":Cisco Packet Tracer Mobile_WebView"
	
class KeyboardConst:
	ANDROID_KEYBOARD = ":Cisco Packet Tracer Mobile_WebView"
	PT_KEYBOARD = ':Cisco Packet Tracer Mobile_View'
	
class KeyboardCli:
	def __init__(self):
		self.KEYBOARD = KeyboardConst.PT_KEYBOARD
		self.CHARS = {
					"a":(self.KEYBOARD,185,161),
					"b":(self.KEYBOARD,579,242),
					"c":(self.KEYBOARD,404,232),
					"d":(self.KEYBOARD,361,159),
					"e":(self.KEYBOARD,347,106),
					"f":(self.KEYBOARD,467,155),
					"g":(self.KEYBOARD,536,164),
					"h":(self.KEYBOARD,634,167),
					"i":(self.KEYBOARD,804,102),
					"j":(self.KEYBOARD,728,176),
					"k":(self.KEYBOARD,803,175),
					"l":(self.KEYBOARD,898,165),
					"m":(self.KEYBOARD,770,235),
					"n":(self.KEYBOARD,691,227),
					"o":(self.KEYBOARD,879,105),
					"p":(self.KEYBOARD,958,109),
					"q":(self.KEYBOARD,192,104),
					"r":(self.KEYBOARD,443,106),
					"s":(self.KEYBOARD,275,180),
					"t":(self.KEYBOARD,516,102),
					"u":(self.KEYBOARD,695,110),
					"v":(self.KEYBOARD,502,242),
					"w":(self.KEYBOARD,261,110),
					"x":(self.KEYBOARD,336,241),
					"y":(self.KEYBOARD,618,107),
					"z":(self.KEYBOARD,249,226),
					"~":(self.KEYBOARD,56,26),
					"1":(self.KEYBOARD,156,37),
					"2":(self.KEYBOARD,237,34),
					"3":(self.KEYBOARD,314,39),
					"4":(self.KEYBOARD,420,35),
					"5":(self.KEYBOARD,498,26),
					"6":(self.KEYBOARD,583,34),
					"7":(self.KEYBOARD,680,39),
					"8":(self.KEYBOARD,770,40),
					"9":(self.KEYBOARD,861,40),
					"0":(self.KEYBOARD,942,40),
					"-":(self.KEYBOARD,1024,32),
					"=":(self.KEYBOARD,1121,40),
					"[":(self.KEYBOARD,1053,96),
					"]":(self.KEYBOARD,1149,98),
					"\\":(self.KEYBOARD,1240,92),
					":":(self.KEYBOARD,993,164),
					"'":(self.KEYBOARD,1087,159),
					",":(self.KEYBOARD,847,236),
					".":(self.KEYBOARD,954,232),
					"[return]":(self.KEYBOARD,1241,160),
					"\r":(self.KEYBOARD,1241,160),
					"\n":(self.KEYBOARD,1241,160),
					"[up]":(self.KEYBOARD, 130, 307),
					"[down]":(self.KEYBOARD, 238, 308),
					" ":(self.KEYBOARD, 600, 280),
					"[space]":(self.KEYBOARD, 600, 280),
					"[abort]":(self.KEYBOARD, 886, 312),
					"[break]":(self.KEYBOARD, 973, 312),
					"[end]":(self.KEYBOARD, 1071, 304),
					"/":(self.KEYBOARD, 1156, 302),
					"?":(self.KEYBOARD, 1249, 311),
					"[shift]":(self.KEYBOARD, 109, 226),
					"[caps]":(self.KEYBOARD, 80, 181),
					"[tab]":(self.KEYBOARD, 87, 101),
					"[delete]":(self.KEYBOARD, 1210, 40),
					"[hideKeyboard]":(self.KEYBOARD, 44, 313)
					}
		self.SPECIAL_CHARS = {
							"`":(self.KEYBOARD, 55, 25),
							"!":(self.KEYBOARD, 159, 29),
							"@":(self.KEYBOARD, 229, 40),
							"#":(self.KEYBOARD, 327, 29),
							"$":(self.KEYBOARD, 430, 31),
							"%":(self.KEYBOARD, 512, 32),
							"^":(self.KEYBOARD, 590, 30),
							"&":(self.KEYBOARD, 696, 32),
							"*":(self.KEYBOARD, 776, 20),
							"(":(self.KEYBOARD, 877, 29),
							")":(self.KEYBOARD, 951, 34),
							"_":(self.KEYBOARD, 1052, 37),
							"+":(self.KEYBOARD, 1132, 33),
							"{":(self.KEYBOARD, 1072, 97),
							"}":(self.KEYBOARD, 1166, 90),
							"|":(self.KEYBOARD, 1250, 106),
							";":(self.KEYBOARD, 1007, 167),
							'"':(self.KEYBOARD, 1090, 169),
							"<":(self.KEYBOARD, 873, 238),
							">":(self.KEYBOARD, 958, 241)
							}
		self.UPPER_CHARS = {
						"A":(self.KEYBOARD,185,161),
						"B":(self.KEYBOARD,579,242),
						"C":(self.KEYBOARD,404,232),
						"D":(self.KEYBOARD,361,159),
						"E":(self.KEYBOARD,347,106),
						"F":(self.KEYBOARD,467,155),
						"G":(self.KEYBOARD,536,164),
						"H":(self.KEYBOARD,634,167),
						"I":(self.KEYBOARD,804,102),
						"J":(self.KEYBOARD,728,176),
						"K":(self.KEYBOARD,803,175),
						"L":(self.KEYBOARD,898,165),
						"M":(self.KEYBOARD,770,235),
						"N":(self.KEYBOARD,691,227),
						"O":(self.KEYBOARD,879,105),
						"P":(self.KEYBOARD,958,109),
						"Q":(self.KEYBOARD,192,104),
						"R":(self.KEYBOARD,443,106),
						"S":(self.KEYBOARD,275,180),
						"T":(self.KEYBOARD,516,102),
						"U":(self.KEYBOARD,695,110),
						"V":(self.KEYBOARD,502,242),
						"W":(self.KEYBOARD,261,110),
						"X":(self.KEYBOARD,336,241),
						"Y":(self.KEYBOARD,618,107),
						"Z":(self.KEYBOARD,249,226)
						}
		
class KeyboardCmd:
	def __init__(self):
		self.cliKeyboard = KeyboardCli()
		self.KEYBOARD = ':Cisco Packet Tracer_View'
		self.CHARS = self.cliKeyboard.CHARS
		self.SPECIAL_CHARS = self.cliKeyboard.SPECIAL_CHARS
		self.UPPER_CHARS = self.cliKeyboard.UPPER_CHARS'''
		
class MainViewConst:
	PT_MOBILE_WEBVIEW = ":Packet Tracer Mobile.webview_WebView"
	
class KeyboardConst:
	ANDROID_KEYBOARD = ":Packet Tracer Mobile.keyboardview_View"
	PT_KEYBOARD = ":Packet Tracer Mobile.keyboardview_View_2"
	
class KeyboardCli:
	def __init__(self):
		self.KEYBOARD = KeyboardConst.PT_KEYBOARD
		self.CHARS = {
					"a":(self.KEYBOARD, 277, 241),
					"b":(self.KEYBOARD, 868, 363),
					"c":(self.KEYBOARD, 606, 348),
					"d":(self.KEYBOARD, 541, 238),
					"e":(self.KEYBOARD, 520, 159),
					"f":(self.KEYBOARD, 700, 232),
					"g":(self.KEYBOARD, 804, 246),
					"h":(self.KEYBOARD, 951, 250),
					"i":(self.KEYBOARD, 1206, 153),
					"j":(self.KEYBOARD, 1092, 264),
					"k":(self.KEYBOARD, 1204, 262),
					"l":(self.KEYBOARD, 1347, 247),
					"m":(self.KEYBOARD, 1155, 352),
					"n":(self.KEYBOARD, 1036, 340),
					"o":(self.KEYBOARD, 1318, 157),
					"p":(self.KEYBOARD, 1437, 163),
					"q":(self.KEYBOARD, 288, 156),
					"r":(self.KEYBOARD, 664, 159),
					"s":(self.KEYBOARD, 412, 270),
					"t":(self.KEYBOARD, 774, 153),
					"u":(self.KEYBOARD, 1042, 165),
					"v":(self.KEYBOARD, 753, 363),
					"w":(self.KEYBOARD, 391, 165),
					"x":(self.KEYBOARD, 504, 361),
					"y":(self.KEYBOARD, 927, 160),
					"z":(self.KEYBOARD, 373, 339),
					"~":(self.KEYBOARD, 84, 39),
					"1":(self.KEYBOARD, 234, 55),
					"2":(self.KEYBOARD, 355, 51),
					"3":(self.KEYBOARD, 471, 58),
					"4":(self.KEYBOARD, 630, 52),
					"5":(self.KEYBOARD, 747, 39),
					"6":(self.KEYBOARD, 874, 51),
					"7":(self.KEYBOARD, 1020, 58),
					"8":(self.KEYBOARD, 1155, 60),
					"9":(self.KEYBOARD, 1291, 60),
					"0":(self.KEYBOARD, 1413, 60),
					"-":(self.KEYBOARD, 1536, 48),
					"=":(self.KEYBOARD, 1681, 60),
					"[":(self.KEYBOARD, 1579, 144),
					"]":(self.KEYBOARD, 1723, 147),
					"\\":(self.KEYBOARD, 1860, 138),
					":":(self.KEYBOARD, 1489, 246),
					"'":(self.KEYBOARD, 1630, 238),
					",":(self.KEYBOARD, 1270, 354),
					".":(self.KEYBOARD, 1431, 348),
					"[return]":(self.KEYBOARD, 1861, 240),
					"\r":(self.KEYBOARD, 1861, 240),
					"\n":(self.KEYBOARD, 1861, 240),
					"[up]":(self.KEYBOARD, 195, 440),
					"[down]":(self.KEYBOARD, 357, 440),
					" ":(self.KEYBOARD, 888, 440),
					"[space]":(self.KEYBOARD, 888, 440),
					"[abort]":(self.KEYBOARD, 1329, 440),
					"[break]":(self.KEYBOARD, 1459, 440),
					"[end]":(self.KEYBOARD, 1606, 440),
					"/":(self.KEYBOARD, 1734, 440),
					"?":(self.KEYBOARD, 1873, 440),
					"[shift]":(self.KEYBOARD, 163, 339),
					"[caps]":(self.KEYBOARD, 120, 271),
					"[tab]":(self.KEYBOARD, 130, 151),
					"[delete]":(self.KEYBOARD, 1860, 38),
					"[hideKeyboard]":(self.KEYBOARD, 66, 440)
					}
		self.SPECIAL_CHARS = {
							"`":(self.KEYBOARD, 82, 37),
							"!":(self.KEYBOARD, 238, 43),
							"@":(self.KEYBOARD, 343, 60),
							"#":(self.KEYBOARD, 490, 43),
							"$":(self.KEYBOARD, 645, 46),
							"%":(self.KEYBOARD, 768, 48),
							"^":(self.KEYBOARD, 885, 45),
							"&":(self.KEYBOARD, 1044, 48),
							"*":(self.KEYBOARD, 1164, 30),
							"(":(self.KEYBOARD, 1315, 43),
							")":(self.KEYBOARD, 1426, 51),
							"_":(self.KEYBOARD, 1578, 55),
							"+":(self.KEYBOARD, 1698, 49),
							"{":(self.KEYBOARD, 1608, 145),
							"}":(self.KEYBOARD, 1749, 135),
							"|":(self.KEYBOARD, 1875, 159),
							";":(self.KEYBOARD, 1510, 250),
							'"':(self.KEYBOARD, 1635, 253),
							"<":(self.KEYBOARD, 1309, 357),
							">":(self.KEYBOARD, 1437, 361)
							}
		self.UPPER_CHARS = {
						"A":(self.KEYBOARD, 277, 241),
						"B":(self.KEYBOARD, 868, 363),
						"C":(self.KEYBOARD, 606, 348),
						"D":(self.KEYBOARD, 541, 238),
						"E":(self.KEYBOARD, 520, 159),
						"F":(self.KEYBOARD, 700, 232),
						"G":(self.KEYBOARD, 804, 246),
						"H":(self.KEYBOARD, 951, 250),
						"I":(self.KEYBOARD, 1206, 153),
						"J":(self.KEYBOARD, 1092, 264),
						"K":(self.KEYBOARD, 1204, 262),
						"L":(self.KEYBOARD, 1347, 247),
						"M":(self.KEYBOARD, 1155, 352),
						"N":(self.KEYBOARD, 1036, 340),
						"O":(self.KEYBOARD, 1318, 157),
						"P":(self.KEYBOARD, 1437, 163),
						"Q":(self.KEYBOARD, 288, 156),
						"R":(self.KEYBOARD, 664, 159),
						"S":(self.KEYBOARD, 412, 270),
						"T":(self.KEYBOARD, 774, 153),
						"U":(self.KEYBOARD, 1042, 165),
						"V":(self.KEYBOARD, 753, 363),
						"W":(self.KEYBOARD, 391, 165),
						"X":(self.KEYBOARD, 504, 361),
						"Y":(self.KEYBOARD, 927, 160),
						"Z":(self.KEYBOARD, 373, 339)
						}
		
class KeyboardCmd:
	def __init__(self):
		self.cliKeyboard = KeyboardCli()
		self.KEYBOARD = KeyboardConst.PT_KEYBOARD
		self.CHARS = self.cliKeyboard.CHARS
		self.SPECIAL_CHARS = self.cliKeyboard.SPECIAL_CHARS
		self.UPPER_CHARS = self.cliKeyboard.UPPER_CHARS