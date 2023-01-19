async function program() {
    //step 1: load the dataset
    var data = await d3.csv("city.csv");
    console.log(data);

    //step 2: create the SVG
    var width = 600,
        height = 200;

    //step 3: bind the data with SVG shapes and texts
    svg = d3
        .select("#chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    var barHeight = 25;

    var text = svg
        .selectAll("text")
        .data(data)
        .join("text")
        .attr("dy", "1.25em")
        .attr("x", 0)
        .attr("y", function (d, i) {
            return i * barHeight;
        }) 
        .attr("font-size", 16)
        .text(function (d, i) {
            return d.name;
        });

    var bar = svg
        .selectAll("rect")
        .data(data)
        .join("rect")
        .attr("x", 80)
        .attr("y", function (d, i) {
            return i * barHeight;
        }) 
        .attr("width", function (d, i) {
            return d.population / 20000;
        })
        .attr("height", barHeight)
        .style("fill", "steelblue")
        .style("stroke", "white");

    

    // var population2width = d3.scaleLinear()
    //     .domain([0, 12000000])
    //     .range([0, 200]);

    // var sequentialColor = d3.scaleSequential()
    //     .domain([0, 12000000])
    //     .interpolator(d3.interpolateViridis);

    // var bar = svg.selectAll("rect")
    //     .data(data)
    //     .join("rect")
    //     .attr("x", 80)
    //     .attr("y", function(d, i) {
    //         return padding + i * (barHeight + padding);
    //     })
    //     .attr("width", function(d, i) {
    //         return population2width(d.population);
    //     })
    //     .attr("height", barHeight)
    //     .style("fill", function(d, i) {
    //         return sequentialColor(d.population);
    //     });

    // svg.append("g")
    //     .attr("transform", "translate(80,160)")
    //     .call(d3.axisBottom(population2width).ticks(2, ".2"))
}

program();
