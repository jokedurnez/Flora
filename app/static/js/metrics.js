var inter = setInterval(function() {updateData();}, 200);

// legend
////////////////////

var legendVals = ["acc_x",'acc_y','acc_z']
var color = ['steelblue', 'red', 'green']
var legend6 = d3.select('.legend6').selectAll("legend").data(legendVals)
legend6.enter().append("div").attr("class","legends6")
legend6.html(function(d,i) { return d } ).style("color", function(d,i) { return color[i] } )


// createfigure
///////////////////

// define dimensions of graph
var m = [80, 80, 80, 80]; // margins
var w = 1000 - m[1] - m[3]; // width
var h = 400 - m[0] - m[2]; // height


// X scale will fit all values from data[] within pixels 0-w
var x = d3.scale.linear().domain([0, 20]).range([0, w]);
// Y scale will fit values from 0-10 within pixels h-0 (Note the inverted domain for the y-scale: bigger is up!)
var y = d3.scale.linear().domain([-20, 20]).range([h, 0]);
// automatically determining max range can work something like this
// var y = d3.scale.linear().domain([0, d3.max(data)]).range([h, 0]);

// create a line function that can convert data[] into x and y points
var line = d3.svg.line()
// assign the X function to plot our line as we wish
.x(function(d,i) {
return x(i);
})
.y(function(d) {
return y(d);
})

// Add an SVG element with the desired dimensions and margin.
var graph = d3.select("#graph").append("svg:svg")
    .attr("width", w + m[1] + m[3])
    .attr("height", h + m[0] + m[2])
  .append("svg:g")
    .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

// create yAxis
var xAxis = d3.svg.axis().scale(x).tickSize(-h).tickSubdivide(true);

// Add the x-axis.
graph.append("svg:g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + h + ")")
    .call(xAxis);


// create left yAxis
var yAxisLeft = d3.svg.axis().scale(y).ticks(4).orient("left");

// Add the y-axis to the left
graph.append("svg:g")
    .attr("class", "y axis")
    .attr("transform", "translate(-25,0)")
    .call(yAxisLeft);


function updateData() {
  d3.json("http://192.168.0.15:7000/api/feel/read20",
    function(error, data){console.log(data);
      if (error) throw error;
      d3.select("#graph svg").selectAll("path").remove();
      // create a simple data array that we'll plot with a line (this array represents only the Y values, X will just be the index location)

      console.log(data);

      graph.append("svg:path")
      .attr("d", line(data.acc_x))

      graph.append("svg:path")
      .attr("d", line(data.acc_y))
      .style("stroke", "red")

      graph.append("svg:path")
      .attr("d", line(data.acc_z))
      .style("stroke", "green")

    })
}
