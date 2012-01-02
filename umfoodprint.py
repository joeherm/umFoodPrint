"""

// array with all the dining hall info
// 	dh[n][0] = hall name for db pass
// 	dh[n][1] = hash value
// 	dh[n][2] = upper right col file | don't set for in-hall cafes
var dh = new Array(21);
	dh[0]	= new Array( "BARBOUR%20DINING%20HALL", "barbour", "rightcolpics/dining.jpg" );
	dh[1]	= new Array( "BURSLEY%20DINING%20HALL", "bursley", "rightcolpics/dining.jpg" );
	dh[2]	= new Array( "COUZENS%20DINING%20HALL", "couzens", "rightcolpics/dining.jpg" );
	dh[3]	= new Array( "EAST%20QUAD%20DINING%20HALL", "east-quad", "rightcolpics/dining.jpg" );
	dh[4]	= new Array( "LLOYD%20DINING%20HALL", "lloyd", "rightcolpics/dining.jpg" );
	dh[5]	= new Array( "MARKLEY%20DINING%20HALL", "markley", "rightcolpics/dining.jpg" );
	dh[6]	= new Array( "OXFORD", "oxford", "rightcolpics/dining.jpg" );
	dh[7]	= new Array( "SOUTH%20QUAD%20DINING%20HALL", "south-quad", "rightcolpics/dining.jpg" );
	dh[8]	= new Array( "STOCKWELL%20DINING%20HALL", "stockwell", "rightcolpics/dining.jpg" );
	dh[9]	= new Array( "WEST%20QUAD%20DINING%20HALL", "west-quad", "rightcolpics/dining.jpg" );
	dh[10]	= new Array( "MARKETPLACE", "marketplace", "flash/slideshow-marketplace.swf" );
	dh[11]	= new Array( "393", "blue-apple" );
	dh[12]	= new Array( "388", "cafe-conxion" );
	dh[13]	= new Array( "389", "ciao-down-pizzeria" );
	dh[14]	= new Array( "380", "east-quad-cafe" );
	dh[15]	= new Array( "390", "markley-hideaway" );
	dh[16]	= new Array( "392", "twigs-a-la-carte" );
	dh[17]	= new Array( "394", "north-star" );
	dh[18]	= new Array( "869", "victors" );
	dh[19]	= new Array( "871", "hours" );
	dh[20]  = new Array( "1780", "north-quad-javablu" );
	dh[21]	= new Array( "North%20Quad%20Dining%20Hall", "north-quad", "flash/slideshow-northquad-dining.swf" );
	dh[22]	= new Array( "Twigs%20at%20Oxford", "twigs-at-oxford", "rightcolpics/dining.jpg" );
	http://housing.umich.edu/files/helper_files/js/menu2xml.php?location=MARKETPLACE
"""

import urllib2
from xml.etree import ElementTree as ET

response = urllib2.urlopen('http://housing.umich.edu/files/helper_files/js/menu2xml.php?location=BURSLEY%20DINING%20HALL')
tree = ET.parse(response)#.getroot()
dindin=0
entr=0
mymenu=""

for node in tree.findall(".//meal[name=\"DINNER\"]//station//course[name=\"Entree1\"]/menuitem"):
	mymenu+=node.text.strip()+";"
for node in tree.findall(".//meal[name=\"DINNER\"]//station//course[name=\"Entree2\"]/menuitem"):
	mymenu+=node.text.strip()+";"
for node in tree.findall(".//meal[name=\"DINNER\"]//station//course[name=\"Entree3\"]/menuitem"):
	mymenu+=node.text.strip()+";"
for node in tree.findall(".//meal[name=\"DINNER\"]//station//course[name=\"Entree4\"]/menuitem"):
	mymenu+=node.text.strip()+";"

print "content-type: text/xml"
print ""
print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
print "<Response>\n<Sms>"+mymenu+"</Sms>\n</Response>"

