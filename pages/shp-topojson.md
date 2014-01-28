title: Vom shp zur topojson
published: 2014-01-27
author: sk

#Vom shp zur topojson
Vorgehensweise bei der Umwandlung einer GIS shp in topojson für d3.js.  
Dependencies: [ogr2ogr](http://www.gdal.org/ogr2ogr.html), [topojson](https://github.com/mbostock/topojson/wiki/Command-Line-Reference)


In QGIS (2.0) wird die world ne_10m_admin_state_provinces geladen.  
Über die Abfrage:  

		"admin"  = 'Paraguay'  OR "admin" = 'Brazil' OR "admin" = 'Argentina' OR "admin" = 'Uruguay'
erfolgt der Ausschnitt der gewünschten Länder. Export der Auswahl als shp.

		ogr2ogr -f GEOJSON file.json file.shp
		topojson --id-property name -o fileout.json filein.json

##d3.js
Längen- und Breitenangaben:  

		var lon: +90° / -90° von West / Ost
		var lat: +90° / -90° von Nord / Süd

