title: shp -> topojson | Binify
published: 2014-01-27
author: sk

#Vom shp zur topojson
Vorgehensweise bei der Umwandlung einer GIS shp in topojson für d3.js.  
Dependencies: [ogr2ogr](http://www.gdal.org/ogr2ogr.html), [topojson](https://github.com/mbostock/topojson/wiki/Command-Line-Reference)


In QGIS (2.0) wird die world ne_10m_admin_state_provinces geladen.  
Über die Abfrage:  

		"admin"  = 'Paraguay'  OR "admin" = 'Brazil' OR "admin" = 'Argentina' OR "admin" = 'Uruguay'
erfolgt der Ausschnitt der gewünschten Länder. Export der Auswahl als shp.

Mit dem CLI von ogr2ogr und topojson erfolgt die Umwandlung in geojson->topojson.

**Wichtig**: geojson und topojson file sollten die gleichen Namen haben, da die Methode d3.json später auf das Objekt aus der geojson zugreift.

		ogr2ogr -f GEOJSON file.json file.shp
		topojson --id-property name -o fileout.json filein.json

##Einige Parameter in d3.js
[d3 Wiki Standard Projections](https://github.com/mbostock/d3/wiki/Geo-Projections#wiki-standard-projections)

Längen- und Breitenangaben:  

		var lon: +180° / -180° von West / Ost
		var lat: +90° / -90° von Nord / Süd
		var projection = d3.geo.albers()
            .center([0, lat])
            .rotate([lon, 0])
 
Breitenangaben (lat) des Kartenausschnitts (parallels):

		.parallels([-12, -35])

#Binify

Hexagon binning dot density maps
[Intro binify](http://kevin.schaul.io/2013/04/19/introducing-binify/)
