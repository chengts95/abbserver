 	    var vis = d3.select("#svg_device").append("svg")
		 			    		.attr("width", 800)
	       	                    .attr("height", 500);

					var	scaleX = d3.scale.linear()
						        	.domain([0,300])
							        .range([150,600]);
										
					var	scaleY = d3.scale.linear()
							        .domain([0,300])
							        .range([200,0]);
					
					
					var defs = vis.append("defs");
					var arrowMarker = defs.append("marker")
											.attr("id","arrow")
											.attr("markerUnits","strokeWidth")
										    .attr("markerWidth","10")
					                        .attr("markerHeight","10")
					                        .attr("viewBox","0 0 10 10") 
					                        .attr("refX","8")
					                        .attr("refY","5")
					                        .attr("orient","auto");
					var arrow_path = "M2,2 L8,5 L2,8";
					arrowMarker.append("path")
								.attr("d",arrow_path)
								.attr("fill","#000");
					
					var defsdx = vis.append("defs");
					var dxMarker = defsdx.append("marker")
											.attr("id","dx")
											.attr("markerUnits","strokeWidth")
										    .attr("markerWidth","10")
					                        .attr("markerHeight","6")
					                        .attr("viewBox","0 0 10 6") 
					                        .attr("refX","5")
					                        .attr("refY","0")
					                        .attr("orient","bottom");
					var dx_path = "M0,0 L10,0 M1,3 L9,3 M3,6 L7,6";
					dxMarker.append("path")
								.attr("d",dx_path)
								.attr("fill","red");
					
									
					var defsx6 = vis.append("defs");
					var x6Marker = defsx6.append("marker")
											.attr("id","x6")
											.attr("markerUnits","strokeWidth")
										    .attr("markerWidth","10")
					                        .attr("markerHeight","50")
					                        .attr("viewBox","0 0 10 50") 
					                        .attr("refX","5")
					                        .attr("refY","0")
					                        .attr("orient","bottom");
					var x6_path = "M0,5 L5,0 L10,5 M0,9 L5,4 L10,9 M5,4 L5,12 M2,12 L8,12 L8,20 L2,20 L2,12 M5,20 L5,28 M0,24 L5,28 L10,24 M0,27 L5,31 L10,26 M5,31 L5,50";
					x6Marker.append("path")
								.attr("d",x6_path)
								.attr("fill","none");
				
					var lineFunction = d3.svg.line()
                        .x( function(d) { return d[0]; })
                        .y( function(d) { return d[1]; })
                        .interpolate("linear");

					vis.append("text")
					   .text("220KV 2")
					   .attr("text-anchor", "middle")
					   .attr("x", 110)
					   .attr("y", 15)
					   .attr("font-family", "sans-serif")
					   .attr("font-size", "11px")
					   .attr("fill", "black");
					
					vis.append("path")
				      .attr("d", lineFunction(L220kv2_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",3)
					  
				  	vis.append("path")
				      .attr("d", lineFunction(L220kv2_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",3)
					  
					 vis.data(L220kv2_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","red")
						.attr("stroke-width",2)
	                    .attr("fill","none");
				
				
				 vis.append("text")
					   .text("220KV 1")
					   .attr("text-anchor", "middle")
					   .attr("x", 110)
					   .attr("y", 45)
					   .attr("font-family", "sans-serif")
					   .attr("font-size", "11px")
					   .attr("fill", "black");
					
					vis.append("path")
				      .attr("d", lineFunction(L220kv1_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",3)
					  
					  vis.append("path")
				      .attr("d", lineFunction(L220kv1_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",3)
					  
					 vis.data(L220kv1_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","red")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
				 	vis.append("path")
				      .attr("d", lineFunction(L45022_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  
				 	vis.append("path")
				      .attr("d", lineFunction(L45022_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  
					vis.append("path")
				      .attr("d", lineFunction(L45022_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
				
					   	vis.append("path")
				      .attr("d", lineFunction(L45021_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  
				 	vis.append("path")
				      .attr("d", lineFunction(L45021_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  
					vis.append("path")
				      .attr("d", lineFunction(L45021_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  
				   	vis.append("path")
				      .attr("d", lineFunction(L4502d1_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					  .attr("fill","none")
				 	 .attr("marker-end","url(#dx)");	
						
					  
				 	vis.append("path")
				      .attr("d", lineFunction(L4502d1_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					  
					vis.append("path")
				      .attr("d", lineFunction(L4502d1_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(L4502_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					vis.append("path")
				      .attr("d", lineFunction(L4502_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","black");
					vis.append("path")
				      .attr("d", lineFunction(L4502_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.data(L4502_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                     .attr("cy",function(d) {return d.y_axis;})
                     .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","red")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(L4502_4_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(L4502d2_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none")
					   	 .attr("marker-end","url(#dx)");	
					  
				 	vis.append("path")
				      .attr("d", lineFunction(L4502d2_2_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					  
					vis.append("path")
				      .attr("d", lineFunction(L4502d2_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.data(c2zb_1)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","red")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.append("path")
				       .attr("d", lineFunction(c2zb_1_in_1))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.append("path")
				        .attr("d", lineFunction(c2zb_1_in_2))  
					    .attr("stroke","red")
					    .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(L4502d0_1_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none")
					     .attr("marker-end","url(#dx)");
					  
				 	vis.append("path")
				        .attr("d", lineFunction(L4502d0_2_pointlist))  
					    .attr("stroke","red")
					    .attr("stroke-width",1)
					    .attr("fill","none");
					  
					vis.append("path")
				      .attr("d", lineFunction(L4502d0_3_pointlist))  
					  .attr("stroke","red")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.data(j2cgb_c)
					    .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","blue")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(j2cgb_l_1))  
					  .attr("stroke","blue")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.data(j2cgb_c_1)
					    .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","blue")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					

					vis.append("path")
				      .attr("d", lineFunction(j2cgb_l_2))  
					  .attr("stroke","blue")
					  .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.append("path")
				        .attr("d", lineFunction(j2cgb_l_3))  
					    .attr("stroke","blue")
					    .attr("stroke-width",1)
					    .attr("fill","none");
					
					vis.data(j2cgb_c_2)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                     .attr("cy",function(d) {return d.y_axis;})
                     .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","blue")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.data(j2cgb_c_3)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                     .attr("cy",function(d) {return d.y_axis;})
                     .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","blue")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.data(j2cgb_c_4)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                     .attr("cy",function(d) {return d.y_axis;})
                     .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","blue")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.data(j621_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                       .attr("cy",function(d) {return d.y_axis;})
                       .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","purple")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(j621_l_1))  
					  .attr("stroke","purple")
					  .attr("stroke-width",1)
					    .attr("fill","none")
					  	 .attr("marker-end","url(#x6)");
					
					
					vis.data(j622_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                    .attr("cy",function(d) {return d.y_axis;})
                    .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","purple")
						.attr("stroke-width",1)
	                    .attr("fill","none");
					
					vis.append("path")
				      .attr("d", lineFunction(j622_l_1))  
					  .attr("stroke","purple")
					  .attr("stroke-width",1)
					  .attr("fill","none")
					 .attr("marker-end","url(#x6)");
