title: Choroplethenkarte 
published: 2014-02-25
author: sk

#Choroplethenkarte (Flächenkartogramm) des Teeanbaus in Japan
Vorgehensweise bei der Erstellung eines Flächenkartogramms der Anbaugebiete von Camellia sinsensis in den Präfekturen Japans.

##Rohdaten
Die [Daten](http://www.maff.go.jp/e/tokei/kikaku/nenji_e/87nenji/index.html#nse004) der Anbaugebiete werden vom jap. Ministerium für Landwirtschaft et al herausgegeben. Das Excelsheet wird in eine csv umgewandelt und auf das Wesentliche beschränkt. Weitere Berarbeitung erfolgt mit Pandas.

##Statistik mit Pandas
Die Python Library [Pandas]()


		DataFrame.describe() 
		                 ga           prod
		count     47.000000      47.000000
		mean     984.893617    8131.042553
		std     2968.198951   27580.366524
		min        0.000000       0.000000
		25%       17.000000       0.000000
		50%      143.000000       0.000000
		75%      692.000000    3140.000000
		max    18700.000000  151300.000000

Liefert die wichtigsten statistischen Werte. Es werden die Daten der Quartile für die Arbeit in d3 verwendet.

###Klasseneinteilung
Die Klasseneinteilung erfolgte nach den statistischen Quartilen. Es sei dabei auf den Artikel [Choropleth Mapping with Exploratory Data Analysis](http://www.directionsmag.com/articles/choropleth-mapping-with-exploratory-data-analysis/123579) hingewiesen.

###Darstellung in d3
Scale in d3: [Threshold Scales](https://github.com/mbostock/d3/wiki/Quantitative-Scales#wiki-threshold-scales)
		var quantize = d3.scale.threshold()
.domain([143, 692, 18700])
.range(d3.range(4).map(function(i) {  return "q" + i + "-4";  }));

dependencies: [ogr2ogr](http://www.gdal.org/ogr2ogr.html), [topojson](https://github.com/mbostock/topojson/wiki/Command-Line-Reference)
