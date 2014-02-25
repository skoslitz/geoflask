title: Choroplethenkarte 
published: 2014-02-25
author: sk

#Choroplethenkarte
##Vorgehensweise bei der Erstellung eines Flächenkartogramms der Anbaugebiete von Camellia sinsensis in den Präfekturen Japans.

###Rohdaten
Die [Daten](http://www.maff.go.jp/e/tokei/kikaku/nenji_e/87nenji/index.html#nse004) der Anbaugebiete werden vom jap. Ministerium für Landwirtschaft et al herausgegeben. Das Excelsheet wird in eine csv umgewandelt und auf das Wesentliche beschränkt. Weitere Berarbeitung erfolgt mit Pandas.

###Statistik mit Pandas
Die Python Library [Pandas](http://pandas.pydata.org/pandas-docs/stable/cookbook.html)


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

liefert die wichtigsten statistischen Werte. Es werden die Daten der Quartile für die Arbeit in d3 verwendet.

###Klasseneinteilung
Die Klasseneinteilung erfolgte nach den statistischen Quartilen. Es sei dabei auf den Artikel [Choropleth Mapping with Exploratory Data Analysis](http://www.directionsmag.com/articles/choropleth-mapping-with-exploratory-data-analysis/123579) hingewiesen.

###Darstellung in d3

Die Karte selbst, wird aus einer topojson entwickelt. Die Daten des Teeanbaus liefert eine csv/tsv.
Eine Funktion muss nun die Daten (japanTea.tsv) anhand der id an die Objekte der topojson abbilden.
Dafür ist d3.map() geeignet:

		var rateById = d3.map();

Beim laden der Daten erfolgt dann eine Klasseneinteilung der Daten aus der .tsv:

		queue()
    		.defer(d3.json, "../japan/japan.json")
    		.defer(d3.tsv, "../japan/japanTea.tsv", function(d) { rateById.set(d.id, +d.GrowingArea); })
    		.await(ready);
    		
    		
Die Funktion ready "zeichnet" nun die svg aus den Daten der japan.json und der Klassen aus japanTea.tsv und setzt einen css-Selektor (die Quartilsklasse)

		function ready(error, japan) {
  		svg.append("g")
      		.attr("class", "japan")
    		.selectAll("path")
      		.data(topojson.feature(japan, japan.objects.japan).features)
    		.enter().append("path")
      		.attr("class", function(d) { return quantize(rateById.get(d.properties.NAME_1)); })
      		.attr("d", path)
		.attr("d", path).on("mouseover", function(d) {
      		return d3.select("#japanState").text(d.properties.NAME_1).style("opacity", "1");
    		}).on("mouseout", function(d) {
	        return d3.select("#japanState").text("Region").style("opacity", "0.4");
    		});
    		
    		
Der css-Selektor wird mit Hilfe folg. Methode gesetzt:


		var quantize = d3.scale.threshold()
		.domain([143, 692, 18700])
		.range(d3.range(4).map(function(i) {  return "q" + i + "-4";  }));


Hinweis:
Scale in d3: [Threshold Scales](https://github.com/mbostock/d3/wiki/Quantitative-Scales#wiki-threshold-scales)
Werte für die d3.domain() sind die Quartile. D3.range gibt die Klasse als späteren css-Selektoren zurück.

In der Css der Karte werden nun Werte für die Klassen ('q1-4', ...) mit Hilfe von [colorbrewer](colorbrewer2.org) gesetzt. 

Das Kartenlayout erfolgt wie üblich.


dependencies: [ogr2ogr](http://www.gdal.org/ogr2ogr.html), [topojson](https://github.com/mbostock/topojson/wiki/Command-Line-Reference)
