var vis = d3.select("#svg_device").append("svg")
	    		.attr("width", 600)
               .attr("height", 300);

var	scaleX = d3.scale.linear()
	        	.domain([0,300])
		        .range([150,600]);
					
var	scaleY = d3.scale.linear()
		        .domain([0,300])
		        .range([200,0]);

 //{% if devices=='hp' %}			
 if (curdevices=="hp")
  {	 
      vis.selectAll("polygon")
					.data([pointlist])
					.enter().append("polygon")
					.attr("points",function(d) { 
					      return d.map(function(d) 
					    		  { return [scaleX(d.x),scaleY(d.y)].join(","); }).join(" ");})
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","yellow");
  };    
//{% end %}

//{% if devices=='ecs' %}	
if (curdevices=="ecs")
  {	

 var lineFunction = d3.svg.line()
    .x( function(d) { return d.x; })
    .y( function(d) { return d.y; })
    .interpolate("linear");

	vis.append("path")
	    .attr("d", lineFunction(pointlist))  
		.attr("stroke","black")
		.attr("stroke-width",2)
	    .attr("fill","yellow");
  }; 
//{% end %}
  
vis.selectAll("text")
			   .data(taglist)
			   .enter()
			   .append("text")
			    .attr("class", "tagtext")
			   .text(function(d) { return d.value;})
			   .attr("text-anchor", "middle")
			   .attr("x", function(d,i) {return d.x;})
			   .attr("y", function(d,i) { return d.y;})
			   .attr("font-family", "sans-serif")
			   .attr("font-size", "11px")
			   .attr("fill", "blue");