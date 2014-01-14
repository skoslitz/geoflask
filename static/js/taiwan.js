var width = 600;
var height = 600;

var lon = -121.0;
var lat = 23.6;

var projection = d3.geo.albers()
    .center([0, lat])
    .rotate([lon, 0])
    .parallels([21.5, 25.5])
    .scale(9000)
    .translate([width / 2, height / 2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("data/taiwan.json", function(error, taiwan) {

  svg.selectAll(".taiwan")
    .data(topojson.feature(taiwan, taiwan.objects.taiwan).features)
  .enter().append("path")
    .attr("class", function(d) { return "taiwan " + d.id; })
    .attr("d", path)
    .on("mouseover", function(d) {
        d3.select("#taiwanState").text(d.id).style("opacity", "1");
    })
    .on("mouseout", function(d) {
        d3.select("#taiwanState").text("Region").style("opacity", "0.4")
    });

  var graticule = d3.geo.graticule()
    .step([0.5, 0.5]);  

  svg.append("path")
    .datum(graticule)
    .attr("d", path)
    .attr("class", "graticule line");
});
    
