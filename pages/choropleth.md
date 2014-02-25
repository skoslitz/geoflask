title: Choroplethenkarte 
published: 2014-02-25
author: sk

#Choroplethenkarte (Flächenkartogramm) des Teeanbaus in Japan
Vorgehensweise bei der Erstellung eines Flächenkartogramms der Anbaugebiete von Camellia sinsensis in den Präfekturen Japans.

##Rohdaten
Die [Daten](http://www.maff.go.jp/e/tokei/kikaku/nenji_e/87nenji/index.html#nse004) der Anbaugebiete werden vom jap. Ministerium für Landwirtschaft et al herausgegeben. Das Excelsheet wird in eine csv umgewandelt und auf das Wesentliche beschränkt. Weitere Berarbeitung erfolgt mit Pandas.

##Statistik mit Pandas
Die Python Library [Pandas]()


dependencies: [ogr2ogr](http://www.gdal.org/ogr2ogr.html), [topojson](https://github.com/mbostock/topojson/wiki/Command-Line-Reference)
