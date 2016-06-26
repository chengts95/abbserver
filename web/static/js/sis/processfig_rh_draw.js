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
					
					var lineFunction = d3.svg.line()
                        .x( function(d) { return d[0]; })
                        .y( function(d) { return d[1]; })
                        .interpolate("linear");

					vis.append("path")
				    .attr("d", lineFunction(Boiler_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
					.attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(fdj_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
					.attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(MS_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",2)
					.attr("fill","none")
					.attr("marker-end","url(#arrow)");
				
				 vis.append("path")
				    .attr("d", lineFunction(RS_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",2)
					.attr("fill","none")
				    .attr("marker-end","url(#arrow)");
					
		
					vis.append("path")
						    .attr("d", lineFunction(HIP_pointlist))  
							.attr("stroke","black")
							.attr("stroke-width",2)
							.attr("fill","yellow");
					
					vis.append("path")
						    .attr("d", lineFunction(LP_pointlist))  
							.attr("stroke","black")
							.attr("stroke-width",2)
							.attr("fill","yellow");
						
					vis.append("path")
				    .attr("d", lineFunction(IP_LP_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",2)
					.attr("marker-end","url(#arrow)")
					.attr("fill","none");
				
					
					vis.append("path")
				    .attr("d", lineFunction(MainAxis_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",4)
					
					
					vis.append("path")
						    .attr("d", lineFunction(MainFeedWater_HH_pointlist))  
							.attr("stroke","green")
							.attr("stroke-width",2)
						   .attr("marker-end","url(#arrow)")
						     .attr("fill","none");
							
					vis.append("path")
						    .attr("d", lineFunction(MainFeedWater_LH_pointlist))  
							.attr("stroke","green")
							.attr("stroke-width",2)
							 .attr("marker-end","url(#arrow)")
								 .attr("fill","none");
				
					vis.append("path")
						    .attr("d", lineFunction(HH1_pointlist))  
							.attr("stroke","black")
							.attr("stroke-width",2)
		                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(HH2_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","none");
			
					vis.append("path")
					
				    .attr("d", lineFunction(HH3_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","none");
					
					vis.append("path")
					
				    .attr("d", lineFunction(HP_HH1_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",1)
						.attr("marker-end","url(#arrow)")
                    .attr("fill","none");
				
                vis.append("path")
				    .attr("d", lineFunction(HP_PQ_HH2_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",1)
						.attr("marker-end","url(#arrow)")
                    .attr("fill","none");
				
					vis.append("path")
					    .attr("d", lineFunction(IP_HH3_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",1)
						.attr("marker-end","url(#arrow)")
	                    .attr("fill","none");
					
	               vis.append("path")
					
				    .attr("d", lineFunction(dw_HH3_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
	               vis.append("path")
					
				    .attr("d", lineFunction(dw_HH2_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                   .attr("fill","none");
						
	               vis.append("path")
					
				    .attr("d", lineFunction(dw_HH1_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                  .attr("fill","none");
						
					vis.append("path")
				    .attr("d", lineFunction(deaerator_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(IP_deaerator_pointlist))  
					.attr("stroke","red")
					.attr("stroke-width",2)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
			
					vis.data(fwpump_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                       .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(deaerator_fwpump_pointlist))  
					.attr("stroke","green")
					.attr("stroke-width",2)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
					.attr("d", lineFunction(LH4_pointlist))  
						.attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
					vis.append("path")
					.attr("d", lineFunction(LH3_pointlist))  
						.attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
					vis.append("path")
					.attr("d", lineFunction(LH2_pointlist))  
						.attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
					vis.append("path")
					    .attr("d", lineFunction(LH1_pointlist))  
						.attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(ZH_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","none");
					

					vis.append("path")
				    .attr("d", lineFunction(dw_LH1_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(dw_LH21_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(dw_LH32_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(dw_LH43_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
				    .attr("d", lineFunction(dw_ZH_pointlist))  
					.attr("stroke","blue")
					.attr("stroke-width",1)
					   .attr("marker-end","url(#arrow)")
                    .attr("fill","none");
					
					vis.append("path")
					     .attr("d", lineFunction(PQ1_LP_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",2)
			
	                    .attr("fill","none");
					
					vis.append("path")
					.attr("d", lineFunction(PQ2_LP_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",2)
						.attr("marker-end","url(#arrow)")
				        .attr("fill","none");
				
					vis.append("path")
					   .attr("d", lineFunction(LP_CQ_LH1_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",1)
						   .attr("marker-end","url(#arrow)")
	                    .attr("fill","none");
			
					vis.append("path")
					   .attr("d", lineFunction(LP_CQ_LH2_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",1)
						   .attr("marker-end","url(#arrow)")
	                    .attr("fill","none");
					
					vis.append("path")
					   .attr("d", lineFunction(LP_CQ_LH3_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",1)
						   .attr("marker-end","url(#arrow)")
	                    .attr("fill","none");
					

					vis.append("path")
					   .attr("d", lineFunction(LP_CQ_LH4_pointlist))  
						.attr("stroke","red")
						.attr("stroke-width",1)
						   .attr("marker-end","url(#arrow)")
	                    .attr("fill","none");
					
					
					vis.data(condenser_circle)
					   .append("circle")
				        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy",function(d) {return d.y_axis;})
                        .attr("r",function(d) {return d.radius;})
			   	        .attr("stroke","black")
						.attr("stroke-width",2)
	                    .attr("fill","none");
					
	              vis.append("path")
					
				    .attr("d", lineFunction(condenser_hall_pointlist))  
					.attr("stroke","black")
					.attr("stroke-width",2)
                    .attr("fill","none");
	              
	              vis.append("path")
					
				    .attr("d", lineFunction(condenser_water_pointlist))  
					.attr("stroke","green")
					.attr("stroke-width",2)
		             .attr("fill","none");
