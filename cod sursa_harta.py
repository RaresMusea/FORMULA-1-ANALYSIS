import folium
tooltip='Click For More Info'


m= folium.Map(location=[45.9442858, 25.0094303], zoom_start=3)
#Continents
#Australia
folium.Marker([-28.921631, 133.574658],
                popup='<div><div><h1 align="center"><strong>The Continent Of Australia<strong></h1><br></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Heidfeld_and_Rosberg_-_2008_Melb_GP.jpg" align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 35 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 3.38% of the F1 International events took place here.</strong></h3></div><br><div><h4 align="center">Most wins (drivers):</h4></div><div><ul><li> Lex Davison (4)</li><li>Michael Schumacher (4)</li></ul></strong></div><br><div><h4 aling="center">Most wins (constructors):</h4></div><div><ul><li>Ferrari</li><li>Mclaren</li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)
folium.Marker([-34.928497, 138.600739],
                popup='<div><div><h1 align="center"><strong>Adelaide<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Pole_Adelaide.jpg/1200px-Pole_Adelaide.jpg" align="center" width="250px"/></div><br><div><h3 align="center"><strong>This city hosted 11 F1 events from 1950 to 2020.</div><br><div><h3 align="center"><strong>31.42% of the F1 events hosted by Australia took place here.</div><br><div><h4 align="center"><strong>Circuit Name:Adelaide Street Circuit</strong></h4></div><br><div><h4 align="center">Main Events</h4></div><div><ul><li><b>Australian Grand Prix</b></li><li><b>Adelaide 500</b></li><li><b>Race of a Thousand Years</b></li></ul></div><br><div><h4 align="center">Circuit Configuration:</h4></div><div><ul><li><b>Length:3.780 km (2.349 mi)</b></li><li><b>Turns:16</b></li><li><b>Race lap record:1:15.381 (United Kingdom Damon Hill, Williams FW15C Renault, 1993, Formula One)</b></li></ul></div></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='green',icon='flag')).add_to(m)
folium.Marker([-37.8136,144.9631],
                popup='<div><div><h1 align="center"><strong>Melbourne<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/1953_Australian_Grand_Prix_start.jpg"   width="250px" align="center"/></div><div><h3 align="center"><strong>This city hosted 24 F1 events from 1950 to 2020.</div><div><h3 align="center"><strong> 68.57% of the F1 events hosted by Australia took place here.<h3></h3></div><br><div><h4 align="center"><strong>Circuit Name:Albert Park Circuit</strong></h4></div><br><div><h4 align="center">Main Events:</h4><div><div><ul><li><b>Formula One</b></li><li><b>Australian Grand Prix</b></li><li><b>Melbourne 400</b></li></ul></div><br><div><h4 align="center">Circuit Configuration:</h4></div><div><ul><li><b>Length:5.303 km(3.296 mi)</b></li><li><b>Turns:16</b></li><li><b>Race lap record:1:24.125 (Germany Michael Schumacher, Ferrari, 2004)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)
#Europe
folium.Marker([50.792047, 15.437569],
                popup='<div><div><h1 align="center"><strong>Europe<strong></h1><br></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/2018_Austrian_Grand_Prix_turn_1_%2843147259711%29.jpg/1200px-2018_Austrian_Grand_Prix_turn_1_%2843147259711%29.jpg"  align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 645 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 62.31% of F1 International events took place here.</strong></h3></div><br><div><h4 aling="center">Most wins (drivers):</h4></div><div><li><b>Michael Schumacher(6)</b></li></ul></strong></div><br><div><h4 align="center">Most wins (constructors):</h4></div><div><ul><li><b>Ferrari</b></li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)

#Asia
folium.Marker([45.089036, 83.621328],
                popup='<div><div><h1 align="center"><strong>Asia<strong></h1><br></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Stuvikcar.jpg"  align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 124 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 11.98% of the F1 International events took place here.</strong></h3></div><br><div><h4 align="center">Most wins (drivers):</h4></div><div><li><b>Michael Schumacher(6)</b></li></ul></strong></div><br><div><h4 align="center">Most wins (constructors):</h4></div><div><ul><li><b>McLaren (9)</b></li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)

#Africa

folium.Marker([9.275622, 22.982587],
                popup='<div><div><h1 align="center"><strong>Africa<strong></h1><br></div><div><img src="resources/africa.jpg"  align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 24 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 2.31% of the F1 International events took place here.</strong></h3></div><br><div><h4 align="center">Most wins (drivers):</h4></div><div><li><b>United Kingdom- Jim Clark (4)</b></li></ul></strong></div><br><div><h4 align="center">Most wins (constructors):</h4></div><div><ul><li><b> Lotus (6)</b></li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)

#North America

folium.Marker([54.525963, -105.255119],
                popup='<div><div><h1 align="center"><strong>North America<strong></h1><br></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Start_1991_USA.jpg/1200px-Start_1991_USA.jpg"   align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 140 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 13.52% of the F1 International events took place here.</strong></h3></div><br><div><h4 align="center">Most wins (drivers):</h4></div><div><li><b>	United Kingdom, Lewis Hamilton (6)</b></li></ul></strong></div><br><div><h4 align="center">Most wins (constructors):</h4></div><div><ul><li><b>Italy, Ferrari (10)</b></li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)

#South America

folium.Marker([-22.268764, -58.468373],
                popup='<div><div><h1 align="center"><strong>South America<strong></h1><br></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Safety_Car_at_2006_Brazil.jpg/1200px-Safety_Car_at_2006_Brazil.jpg"  align="center" width="250px"/></div><br><div><h3 align="center"><strong>This Continent held 67 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 6.47% of the F1 International events took place here.</strong></h3></div><br><div><h4 align="center">Most wins (drivers):</h4></div><div><li><b>		France, Alain Prost (6)</b></li></ul></strong></div><br><div><h4 align="center">Most wins (constructors):</h4></div><div><ul><li><b>	United Kingdom ,McLaren (12)</b></li></ul></div></div>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)


#Spain
#Country itself

folium.Marker([40.346544, -3.837014],

                popup='<div><div><h1 align="center"><strong>Spain<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 57 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 8.83% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Spain has a total of 7 F1 circuits: <strong></h4></div><div><ul><li><b>Circuit de Barcelona-Catalunya</b></li><li><b>Montjuic Circuit</b></li><li><b>Circuito De Jerez</b><li><b>Jarama Circuit</b></li><li><b>Valencia Stret Circuit</b></li><li><b>Circuito de Perdalbes</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities from Spain 

folium.Marker([41.551460, 2.248460],

                popup='<div><div><h1 align="center"><strong>Montmelo<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Pit_Lane_Entrance%40circuitdeCatalunya.jpg"   width="250px" align="center"/></div><br><div><h4 align="center"><strong>This city hosted 30 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 52.63% of the F1 events hosted by Spain took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit de Barcelona-Catalunya</h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>1992 Summer Olympics Formula One</b></li><li><b>Spanish Grand Prix</b></li><li><b>MotoGP</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.655 km (2.892 mi)</b></li><li><b>Turns:16</b></li><li><b>Race lap record:1:18.183 (Finland Valtteri Bottas, Mercedes, 2020)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([39.470242, -0.376800],

                popup='<div><div><h1 align="center"><strong>Valencia<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/Valencia_Street_Circuit_GT_Open.jpg" alt="Valencia Street Circuit GT Open.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 5 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 8.77% of the F1 events hosted by Spain took place here.</strong></h3></div><div><h4 align="center"><strong>Circuit Name:Valencia Street Circuit</h4></div><br><div><h4 align="center">This circuit was closed in 2013.</h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>European Grand Prix</b></li></div><br><div><div><h4 align="center">Car Configuration:</h4></div><br><div><ul><li><b>Length:5.419 km (3.367 mi)</b></li><li><b>Turns:25</b></li><li><b>Race lap record:1:38.683 (Timo Glock, Toyota, 2009, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([36.685005, -6.126074],
                popup='<div><div><h1 align="center"><strong>Jerez De La Frontera<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Circuito_Jerez_-_20170528_140446.jpg/1200px-Circuito_Jerez_-_20170528_140446.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 7 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 12.28% of the F1 events hosted by Spain took place here.</strong><br></h4></strong></div><div><h4 align="center"><strong>Circuit Name:Circuito De Jerez</strong></h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>European Grand Prix</b></li></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.428 km (2.751 mi)</b></li><li><b>Turns:13</b></li><li><b>Race lap record:1:23.135 (Germany Heinz-Harald Frentzen, Williams-Renault FW19, 1997)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([40.504810, -3.532270],

                popup='<div><div><h1 align="center"><strong>Jarama<strong></h1></div><div><img src="resources/jarama (1).jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 9 F1 events from 1950 to 2020.</strong></h3></div><br><div><h3 align="center"><strong> 15.78% of the F1 events hosted by Spain took place here.</strong></h3>/div><div><h4 align="center"><strong>Circuit Name:Circuito del Jarama</strong></h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>World Touring Car Championship</b></li><ul><li><b>Spanish Grand Prix</b></div><br><div><div><h4 align="center">Car Configuration:</h4></div><br><div><ul><li><b>Length:3.850 km (2.392 mi)</b></li><li><b>Turns:11</b></li><li><b>Race lap record:1:16.44 (Gilles Villeneuve, Ferrari 312T4, 1979)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([41.385063, 2.173404],

                popup='<div><div><h1 align="center"><strong>Barcelona<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/b/b6/Circuit_MontjuichPark.png"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 4 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 7.01% of the F1 events hosted by Spain took place here.</strong></h3></div><div><h4 align="center"><strong>Circuit Name:Montjuic Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Penya Rhin Grand Prix</b></li><ul><li><b>Spanish Grand Prix</b></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.79 km (2.35 mi)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:1:23.8 - 101.169 mph (Sweden Ronnie Peterson, Lotus-Ford, 1973)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([41.385063, 2.173404],

                popup='<div><div><h1 align="center"><strong>Barcelona<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/b/b6/Circuit_MontjuichPark.png"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 6 F1 events from 1950 to 2020.</strong</h3></div><br><div><h3 align="center"><strong> 10.52% of the F1 events hosted by Spain took place here.</strong></h3></div><div><h4 align="center"><strong>1.Circuit Name:Montjuic Circuit</strong></h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Penya Rhin Grand Prix</b></li><ul><li><b>Spanish Grand Prix</b></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.79 km (2.35 mi)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:1:23.8 - 101.169 mph (Sweden Ronnie Peterson, Lotus-Ford, 1973)</b></li></ul></div><br><div><h4 align="center"><strong>2.Circuit Name:Pedralbes Circuit(retired in 1955)</strong></h4></div><br><div><h4 align="center">Major events</h4></div><div><ul><li><b>Spanish Grand Prix</b></li><li><b>Penya Rihn Grand Prix</b></li></ul></div><br><div><h4 align="center">Car Configuration:</h4></div><br><div><ul><li><b>Lenght:	6.333 km (3.936 mi)</b></li><li><b>Turns:6</b></li><li><b>Race lap record:2:20.4 – 100.923 mph (Italy Alberto Ascari, Lancia, 1954)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Portugal
#Country itself

folium.Marker([39.399872, -8.224454],

                popup='<div><div><h1 align="center"><strong>Portugal<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/1200px-Flag_of_Portugal.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 17 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 2.63% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Portugal has a total of 4 F1 circuits: <strong></h4><div><ul><li><b>Autodromo do Estoril</b></li><li><b>Monsanto Park Circuit</b></li><li><b>Circuito de Boavista</b><li><b>Autodromo Internacional do Algarve</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)




#Cities

folium.Marker([38.706180, -9.397820],

                popup='<div><div><h1 align="center"><strong>Estoril<strong></h1></div><div><img src="resources/estoril.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 13 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 76.47% of the F1 events hosted by Portugal took place here.</strong></h3></div><div><h4 align="center"><strong>Circuit Name:Circuito de Estoril</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>A1 Grand Prix</b></li><li><b>6 Hours of Estoril</b></li><li><b>Portuguese Grand Prix</b></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.182 km (2.599 mi)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:1:22.446 (United Kingdom David Coulthard, Williams-Renault FW16B, 1994)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([38.707010, -9.135640],
                popup='<div><div><h1 align="center"><strong>Lisbon<strong></h1></div><div><img src="resources/monsanto1.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 5.88% of the F1 events hosted by Portugal took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Monsanto Park Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Portguese Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.440 km (3.380 mi)</b></li><li<b>Turns:9<b></li><li><b>Race lap record:2:05.07 (United Kingdom Stirling Moss, Cooper, 1959)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([41.150150, -8.610320],
                popup='<div><div><h1 align="center"><strong>Oporto<strong></h1></div><div><img src="resources/boavista1.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 2 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 11.76% of the F1 events hosted by Portugal took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuito da Boavista</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Portguese Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:7.4 km (4.59815 mi)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:2:27.53 (United Kingdom John Surtees, Lotus-Climax, 1960)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([37.137630, -8.534400],
                popup='<div><div><h1 align="center"><strong>Portimao<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/0/00/AM007.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 5.88% of the F1 events hosted by Portugal took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autodromo Internacional do Algarve</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Portguese Grand Prix</b></li><li><b>A1 Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.653 km (2.891 mi)</b></li><li><b>Turns:15</b></li><li><b>Race lap record:1:18.750 (United Kingdom Lewis Hamilton, Mercedes, 2020, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Turkey
#Country itself

folium.Marker([41.211722, 28.536226],

                popup='<div><div><h1 align="center"><strong>Turkey<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/1200px-Flag_of_Turkey.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 8 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 1.24% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Turkey has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Instanbul Park</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([41.013000, 28.974800],
                popup='<div><div><h1 align="center"><strong>Istanbul<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Istanbul_Park_aerial.jpg/1200px-Istanbul_Park_aerial.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 8 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 100.00% of the F1 events hosted by Turkey took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Istanbul Park</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Turkish Grand Prix</b></li><li><b>Le Mans Series</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.338 km (3.317 mi)</b></li><li><b>Turns:14</b></li><li><b>Race lap record:1:24.770 (Colombia Juan Pablo Montoya, McLaren-Mercedes, 2005)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Monaco
#Country itself

folium.Marker([43.738419, 7.424616],

                popup='<div><div><h1 align="center"><strong>Monaco<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Flag_of_Monaco.svg/1200px-Flag_of_Monaco.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 66 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 10.23% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Monaco has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Circuit de Monaco</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([43.740420, 7.425580],
                popup='<div><div><h1 align="center"><strong>Monte Carlo<strong></h1></div><div><img src="resources/monaco.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 66 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 100.00% of the F1 events hosted by Monaco took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit de Monaco</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Monaco Grand Prix</b></li><li><b>Historic Grand Prix of Monaco</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.34 km (2.075 mi)</b></li><li><b>Turns:18</b></li><li><b>Race lap record:1:14.260 (Netherlands Max Verstappen, Red Bull-TAG Heuer, 2018)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#France
#Country itself

folium.Marker([46.377254, 1.553843],

                popup='<div><div><h1 align="center"><strong>France</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 61 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 9.45% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>France has 7 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Circuit de Nevers Magny-Cours</b></li><li><b>Circuit Paul Ricard</b></li><li><b>Dijon-Prenois Circuit</b></li><li><b>Circuit de Charade</b></li><li><b>Rouen-Les-Essarts</b></li><li><b>Circuit des 24 heures du Mans</b></li><li><b>Reims-Gueux</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities

folium.Marker([46.883940, 3.151300],
                popup='<div><div><h1 align="center"><strong>Magny-Cours<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Mark_Webber_2006.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 18 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 29.50% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit de Nevers Magny-Cours</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>French Grand Prix</b></li><li><b>GP2</b></li><li><b>Superleague Formula</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.412 km (2.741 mi)</b></li><li><b>Turns:17</b></li><li><b>Race lap record:1:15.377 (Germany Michael Schumacher, Ferrari F2004, 2004 French Grand Prix)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([43.222510, 5.762810],
                popup='<div><div><h1 align="center"><strong>La Castellet<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/6/64/2011_WSR_Paul_Ricard_-_Daniel_Ricciardo.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 16 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 26.22% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Paul Ricard</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>GP2</b></li><li><b>6 Hours of Castellet</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.842 km (2018)</b></li><li><b>Turns:21</b></li><li><b>Race lap record:1:32.740 (Germany Sebastian Vettel, Ferrari, 2019)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([47.322048, 5.041480],
                popup='<div><div><h1 align="center"><strong>Dijon<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Dijon-Prenois1.jpg/1200px-Dijon-Prenois1.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 6 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 9.83% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Dijon-Prenois</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>West European Cup</b></li><li><b>Formula Renault 2.0</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.800 km (2.361 mi) (1977)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:1:02.200, (Patrick Tambay, Renault RE50, 1984)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([45.777210, 3.082520],
                popup='<div><div><h2 align="center"><strong>Clermont-Ferrand<strong></h2></div><div><img src="resources/clermont.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 4 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 6.55% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit de Charade</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>French Grand Prix</b></li><li><b>French Supertouring Championship</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:8.055 km (5.005 miles)</b></li><li><b>Turns:48</b></li><li><b>Race lap record:2:53.9, (Chris Amon, Matra, 1972)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([49.443233, 1.099971],
                popup='<div><div><h1 align="center"><strong>Rouen<strong></h1></div><div><img src="resources/essarts.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 5 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 8.19% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Rouen-Les-Essarts</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>French Grand Prix</b></li><li><b>French Touring Car Championship</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:6.542 km (1957-1968)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:2:11.4 (Australia Jack Brabham, Brabham-Climax, 1964) (1955 configuration)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([48.007751, 0.198520],
                popup='<div><div><h1 align="center"><strong>Le Mans<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/United-autosports-le-mans-test-087.jpg/1200px-United-autosports-le-mans-test-087.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 1.63% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit des 24 heures du Mans</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>24 Hours of Le Mans</b></li><li><b>French Grand Prix</b></li><li><b>ACO</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	13.626 km (8.467 mi)</b></li><li><b>Turns:38</b></li><li><b>Race lap record:3:17.297 (Mike Conway, Toyota Gazoo Racing, 2019, LMP1)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([49.258327, 4.031696],
                popup='<div><div><h1 align="center"><strong>Reims<strong></h1></div><div><img src="resources/reims.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 11 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 18.03% of the F1 events hosted by France took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Reims-Gueux</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>12 Hours of Reims</b></li><li><b>French Grand Prix</b></li><li><b>Grand Prix de la Marne</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	8.348 km (5.1872067 mi)</b></li><li><b>Turns:6</b></li><li><b>Race lap record:2:11.3, (Lorenzo Bandini, 1966)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#UK
#Country itself

folium.Marker([55.429013, -4.858886],

                popup='<div><div><h1 align="center"><strong>UK</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png" width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 75 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 11.62% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>UK has 4 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Silverstone Circuit</b></li><li><b>Donington Park</b></li><li><b>Brands Hatch Circuit</b></li><li><b>Aintree Motor Racing Circuit</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([52.091660, -1.026140],
                popup='<div><div><h1 align="center"><strong>Silverstone<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Niki_Lauda_Ferrari_312T_JPGP_S_75_2.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 55 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 73.33% of the F1 events hosted by UK took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Silverstone Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Birtish Grand Prix</b></li><li><b>Grand 70th Anniversary Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	5.901 km (3.667 mi)</b></li><li><b>Turns:18</b></li><li><b>Race lap record:1:27.097 (Netherlands Max Verstappen, Red Bull-Honda, 2020)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([52.844429, -1.337690],
                popup='<div><div><h1 align="center"><strong>Castle Donington<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/SF_Donington_4.jpg/1200px-SF_Donington_4.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 1.33% of the F1 events hosted by UK took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Donington Park</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>BTCC</b></li><li><b>British GT</b></li><li><b>Download Festival</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	4.020 km (2.498 mi)</b></li><li><b>Turns:12</b></li><li><b>Race lap record:<ul><li>1:18.029 (Brazil Ayrton Senna, McLaren-Ford, 1993) (race/wet/pit lane)<b></b></li><li><b>1:19.379 (United Kingdom Damon Hill, Williams-Renault, 1993) (race/wet/full lap)</b></li><li><b>1:10.458 (France Alain Prost, Williams-Renault, 1993) (practice/dry/full lap)</b></li></ul></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([51.270340, 0.523840],
                popup='<div><div><h1 align="center"><strong>Kent<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/7/70/Jame_Hunt_RoC_77.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 14 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 18.66% of the F1 events hosted by UK took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Brands Hatch Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Birtish Grand Prix</b></li><li><b>Formula 3000 International</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.908 km (2.4283186 mi)	</b></li><li><b>Turns:9</b></li><li><b>Race lap record:1:09.593 (United Kingdom Nigel Mansell, Williams-Honda, 1986)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([53.408371, -2.991573],
                popup='<div><div><h1 align="center"><strong>Liverpool<strong></h1></div><div><img src="resources/liverpool.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 5 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 6.66% of the F1 events hosted by UK took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Aintree Motor Racing Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Birtish Grand Prix</b></li><li><b>Grand Prix de Europe</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.828 km (3.000 mi) </b></li><li><b>Turns:8</b></li><li><b>Race lap record:1:55.0 (United Kingdom Jim Clark, Lotus-Climax, 1962)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Germany
#Country itself

folium.Marker([51.069017, 10.236470],

                popup='<div><div><h1 align="center"><strong>Germany</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1200px-Flag_of_Germany.svg.png"  width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 80 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 12.40% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>UK has 3 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Hockenheimring</b></li><li><b>Nurburgring</b></li><li><b>AVUS</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([49.329895, 8.570925],
                popup='<div><div><h1 align="center"><strong>Hockenheim<strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Kimi_Raikkonen_-_Turn_1_of_the_Hockenheimring_-_2014_German_Grand_Prix.jpg/1200px-Kimi_Raikkonen_-_Turn_1_of_the_Hockenheimring_-_2014_German_Grand_Prix.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 38 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 47.5% of the F1 events hosted by Germany took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Hockenheimring</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>World RX of Hockenheim</b></li><li><b>German Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.574 km (2.842 mi) </b></li><li><b>Turns:17</b></li><li><b>Race lap record:1:13.780 (Finland Kimi Räikkönen, McLaren, 2004)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([50.341350, 6.951810],
                popup='<div><div><h1 align="center"><strong>Nurburg</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/2/22/N%C3%BCrburgring_Luftaufnahme_2004.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 41 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong> 51.24% of the F1 events hosted by Germany took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Nurburgring</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>German Grand Prix</b></li><li><b>Luxembourg Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.148 km (1.198 mi) </b></li><li><b>Turns:15</b></li><li><b>Race lap record:1:28.139 (Netherlands Max Verstappen, Red Bull Racing RB16, 2020, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([52.523430, 13.411440],
                popup='<div><div><h1 align="center"><strong>Berlin</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Bundesarchiv_B_145_Bild-P016402%2C_Berlin%2C_Rennen_auf_der_Avus.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>1.25% of the F1 events hosted by Germany took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:AVUS(Automobil-Verkehrs- und Übungsstraß)</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>1926 German Grand Prix</b></li><li><b>1959 German Grand Prix </b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:8.300 km (5.157 mi) </b></li><li><b>Turns:15</b></li><li><b>Race lap record:Tony Brooks, Ferrari, 1959, 2:04.5 (240.00 km/h)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Hungary
#Country itself

folium.Marker([46.995241, 19.152317],
                popup='<div><div><h1 align="center"><strong>Hungary</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_Hungary.svg/1200px-Flag_of_Hungary.svg.png"   width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 34 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 5.27% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Hungary has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Hungaroring</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([47.498138, 19.040550],
                popup='<div><div><h1 align="center"><strong>Budapest</strong></h1></div><div><img src="resources/Hungary.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 34 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Hungary took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Hungaroring</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Hungarian Grand Prix</b></li><li><b>Hungarian motorcycle Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.831 km (3.001 mi) </b></li><li><b>Turns:16</b></li><li><b>Race lap record:1:16.627 (United Kingdom Lewis Hamilton, Mercedes, 2020)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Belgium
#Country itself

folium.Marker([50.503887, 4.469936],
                popup='<div><div><h1 align="center"><strong>Belgium</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/1200px-Flag_of_Belgium.svg.png"   width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 66 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 10.23% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Belgium has 3 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Circuit de Spa-Francorchamps</b></li><li><b>Circuit Zolder</b></li><li><b>Nivelles-Baulers</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([50.492360, 5.863250],
                popup='<div><div><h1 align="center"><strong>Spa</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/%C2%A9J.Breuer.jpg/1200px-%C2%A9J.Breuer.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 54 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>81.81% of the F1 events hosted by Belgium took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit de Spa-Francorchamps</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Spa 24 Hours</b></li><li><b>Belgian Grand Prix</b></li><li><b>Blancpain Endurance Series</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:7.004 km (4.352 mi) </b></li><li><b>Turns:20</b></li><li><b>Race lap record:1:46.286 (Finland Valtteri Bottas, Mercedes, 2018)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([51.038483, 5.290413],
                popup='<div><div><h1 align="center"><strong>Heusden-Zolder</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Circuit_Zolder_6-11-2008_16-29-22.jpg/1200px-Circuit_Zolder_6-11-2008_16-29-22.jpg"     width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 10 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>15.15% of the F1 events hosted by Belgium took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Zolder</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>24 Hours of Zolder</b></li><li><b>Belgian Grand Prix</b></li><li><b>Superleaue Formula</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:<ul><li><b>4.220 km (1973)</b></li><li><b>4.262km (1975-84)</b></li></ul><li><b>Turns:11</b></li><li><b>Race lap record:1:19.294, René Arnoux, Ferrari 126C4, 1984</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([50.845540, 4.355710],
                popup='<div><div><h1 align="center"><strong>Brussels</strong></h1></div><div><img src="resources/nivelles.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 2 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>3.03% of the F1 events hosted by Belgium took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Nivelles-Baulers</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Belgian Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	3.72 km (2.314 mi)</b></li><li><b>Turns:7</b></li><li><b>Race lap record:1:11.31 (New Zealand Denny Hulme, United Kingdom McLaren-Ford, 1974, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Italy
#Country itself

folium.Marker([41.804078, 14.003463],
                popup='<div><div><h1 align="center"><strong>Italy</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/1200px-Flag_of_Italy.svg.png"   width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 99 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 15.34% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Italy  has 4 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Autodromo Nazionale di Monza</b></li><li><b>Autodromo Internazionale Enzo e Dino Ferrari</b></li><li><b>Autodromo Internazionale del Mugello</b></li><li><b>Pescara Circuit</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities

folium.Marker([45.583130, 9.272970],
                popup='<div><div><h1 align="center"><strong>Monza</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/8/80/Autodromo_Monza.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 69 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>69.69% of the F1 events hosted by Italy took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autodromo Nazionale di Monza</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Italian Grand Prix</b></li><li><b>1000 km Monza</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.793 km ( 3.599 mi)</b></li><li><b>Turns:11</b></li><li><b>Race lap record:1:21.046 (Brazil Rubens Barrichello, Ferrari, 2004)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([44.355888, 11.716090],
                popup='<div><div><h1 align="center"><strong>Imola</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/4/40/Imola2008.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 28 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>28.28% of the F1 events hosted by Italy took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autodromo Internazionale Enzo e Dino Ferrari</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Emilia Romagna Grand Prix (2020)</b></li><li><b>Le Mans Series</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.909 km ( 3.050 mi)</b></li><li><b>Turns:17</b></li><li><b>Race lap record:1:15.484 (United Kingdom Lewis Hamilton, Mercedes, 2020)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([44.001040, 11.238540],
                popup='<div><div><h1 align="center"><strong>Mugello</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Mitjet-italie.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>1.01% of the F1 events hosted by Italy took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Mugello,Autodromo Internazionale del Mugello</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Tuscan Grand Prix </b></li><li><b>Italian motorcycle Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.245 km (3.259 mi)</b></li><li><b>Turns:15</b></li><li><b>Race lap record:1:18.833 (United Kingdom Lewis Hamilton, Mercedes, 2020)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([42.464828, 14.214090],
                popup='<div><div><h1 align="center"><strong>Pescara</strong></h1></div><div><img src="resources/pescara1.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>1.01% of the F1 events hosted by Italy took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Pescara Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Pescara Grand Prix </b></li><li><b>Coppa Acerbo</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:25.578 km  (15.894 miles)</b></li><li><b>Turns:38</b></li><li><b>Race lap record:9:44.6 (United Kingdom Stirling Moss, Vanwall)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Austria
#Country itself

folium.Marker([47.516232, 14.550072],
                popup='<div><div><h1 align="center"><strong>Austria</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/1200px-Flag_of_Austria.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 34 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 5.27% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Austria has 3 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Red Bull Ring</b></li><li><b>A1-Ring</b></li><li><b>Zeltweg Airfieldt</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([48.209210, 16.372780],
                popup='<div><div><h1 align="center"><strong>Speilburg</strong></h1></div><div><img src="resources/a1r.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 33 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>97.05% of F1 events hosted by Austria took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:1.A1-Ring </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Austrian Grand Prix </b></li><li><b>DTM</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	4.326 km (2.688 mi)</b></li><li><b>Turns:9</b></li><li><b>Race lap record:1:08.337 (Germany Michael Schumacher, Ferrari F2003-GA, 2003, Formula One)</b></li></ul></div><br><div><h4 align="center"><strong>2.Circuit Name:Red Bull Ring</strong> </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Australian Grand Prix </b></li><li><b>ELMS 4 Hours of Red Bull Ring</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.318 km (2.683 mi)</b></li><li><b>Turns:10</b></li><li><b>Race lap record:1:05.619 (Spain Carlos Sainz Jr., McLaren-Renault MCL35, 2020, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([47.269120, 15.012060],
                popup='<div><div><h1 align="center"><strong>Styria</strong></h1></div><div><img src="resources/austriaz.jpg" width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>2.94% of F1 events hosted by Austria took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Zeltweg Airfield </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Austrian Grand Prix(1964) </b></li><li><b>FIA World Sportscar</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.1865 km (1.98 miles)</b></li><li><b>Turns:5</b></li><li><b>Race lap record:1:04.820 (Switzerland Jo Siffert, Germany Porsche 908, 1968, 500km of Zeltweg)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Netherlands
#Country itself     

folium.Marker([52.132633, 5.291266],
                popup='<div><div><h1 align="center"><strong>Netherlands</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/1200px-Flag_of_the_Netherlands.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 30 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 4.65% of the  European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strong>Netherlands has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Circuit Park Zandvoort</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([52.371849, 4.530260],
                popup='<div><div><h1 align="center"><strong>Zandvoort</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Circuit_Zandvoort_motorsport_race_track_in_the_Netherlands_%2846940292845%29.jpg/1200px-Circuit_Zandvoort_motorsport_race_track_in_the_Netherlands_%2846940292845%29.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 30 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Netherlands took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Park Zandvoort </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Dutch Grand Prix </b></li><li><b>DTM</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.307 km (2.676 mi)</b></li><li><b>Turns:15</b></li><li><b>Race lap record:1:22.849 (Netherlands Klaas Zwart, Jaguar R5 F1, 2014, BOSS GP Series)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Switzerland
#Country itself 


folium.Marker([46.818188, 8.227512],
                popup='<div><div><h1 align="center"><strong>Switzerland</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/1200px-Flag_of_Switzerland.svg.png"      width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 5 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 0.77% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Switzerland  has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Circuit Bermgarten</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([46.947975, 7.447447],
                popup='<div><div><h1 align="center"><strong>Bern</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Tennikurvebremgarp.jpg/1200px-Tennikurvebremgarp.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 5 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Switzerland took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Bermgarten</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b> European Drivers Championship</b></li><li><b>Grand Prix motorcycle racing</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:7.28 km (4.524 mi)</b></li><li><b>Turns:13</b></li><li><b>Race lap record:2:34.5 (Bernd Rosemeyer, Auto Union, 1936)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Sweden
#Country itself 

folium.Marker([60.128162, 18.643501],
                popup='<div><div><h1 align="center"><strong>Sweden</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Flag_of_Sweden.svg/1200px-Flag_of_Sweden.svg.png"      width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 6 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 0.93%  the of European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Switzerland  has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Anderstorp Circuit</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([64.741203, 20.975740],
                popup='<div><div><h1 align="center"><strong>Anderstorp</strong></h1></div><div><img src="resources/sweden.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 6 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Sweden took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Anderstorp Cicuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Swedish Grand Prix</b></li><li><b>Swedish motorcycle Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	4.025 km (2.501 mi)</b></li><li><b>Turns:8</b></li><li><b>Race lap record:1:24.836, Niki Lauda, Brabham BT46B, 1978</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)


#Russia
#Country itself 

folium.Marker([55.478853, 37.584011],
                popup='<div><div><h1 align="center"><strong>Russia</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/1200px-Flag_of_Russia.svg.png"      width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 7 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 1.08% of the European F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Switzerland  has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Sochi Autodorm</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([43.584469, 39.720280],
                popup='<div><div><h1 align="center"><strong>Sochi</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Sochi_adler_aerial_view_2018_15.jpg/1200px-Sochi_adler_aerial_view_2018_15.jpg" alt="Sochi adler aerial view 2018 15.jpg"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 7 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Russia took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Sochi Autodrom</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Russian Grand Prix</b></li><li><b>Russian Touring Car Championship</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.848 km (3.634 mi)</b></li><li><b>Turns:18</b></li><li><b>Race lap record:1:35.761 (United Kingdom Lewis Hamilton, Mercedes, 2019, F1)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)


#Asia
#Malaysia
#Country itself 

folium.Marker([5.090944, 102.500754],
                popup='<div><div><h1 align="center"><strong>Malaysia</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/1200px-Flag_of_Malaysia.svg.png"      width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 19 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 15.32% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Malaysia  has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Sepang International Circuit</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([3.139003, 101.686852],
                popup='<div><div><h1 align="center"><strong>Kuala Lumpur</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Sepang-international-circuit.JPG/1200px-Sepang-international-circuit.JPG"  width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 19 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Malaysia took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Sepang International Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Malaysian Grand Prix</b></li><li><b>Malaysia Merdeka Endurance Race</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.543 km (3.444 mi)</b></li><li><b>Turns:18</b></li><li><b>Race lap record:1:34.080 (Germany Sebastian Vettel, Ferrari, 2017)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Bahrain
#Country itself 

folium.Marker([26.071586, 50.561433],
                popup='<div><div><h1 align="center"><strong>Bahrain</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Bahrain.svg/1200px-Flag_of_Bahrain.svg.png"      width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 18 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 14.51% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Bahrain has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Bahrain International Circuit</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([26.057590, 50.528260],
                popup='<div><div><h1 align="center"><strong>Sakhir</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Bahrain_International_Circuit_back_straight.jpg/1200px-Bahrain_International_Circuit_back_straight.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 18 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Bahrain took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Bahrain International Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Bahrain Grand Prix</b></li><li><b>Sakhir Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.412 km (3.362 mi)</b></li><li><b>Turns:15</b></li><li><b>Race lap record:<ul><li><b>1:30.252 (Germany Michael Schumacher, Ferrari, 2004, original layout)</b></li><li><b>1:31.447 (Spain Pedro de la Rosa, McLaren-Mercedes, 2005 Bahrain Grand Prix, revised layout)</b></li><li><b>1:31.447 (Spain Pedro de la Rosa, McLaren-Mercedes, 2005 Bahrain Grand Prix, revised layout)</b></li></ul></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Singapore
#Country itself 

folium.Marker([1.352083, 103.819839],
                popup='<div><div><h1 align="center"><strong>Singapore</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/1200px-Flag_of_Singapore.svg.png"  width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 12 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 9.67% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Singapore has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Marina Bay Street Circuit</b></li></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([1.284434, 103.856246],
                popup='<div><div><h1 align="center"><strong>Marina Bay</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Pit_building_2014_Singapore.jpg/1200px-Pit_building_2014_Singapore.jpg"   width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 12 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Singapore took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Marina Bay Street Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Singapore Grand Prix</b></li><li><b>Porsche Carrera Cup Asia</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.063 km (3.146 mi)</b></li><li><b>Turns:23</b></li><li><b>Race lap record:<li><b>1:41.905 (Denmark Kevin Magnussen, Haas-Ferrari, 2018)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Japan
#Country itself

folium.Marker([35.746512, 138.139337],
                popup='<div><div><h1 align="center"><strong>Japan</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/1200px-Flag_of_Japan.svg.png"  width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 37 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 29.83% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Japan has 3 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Suzuka Circuit</b></li><li><b>Fuji Speedway</b><li><b>Suzuka Circuit</b></li><li><b>Okayama International Circuit</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities

folium.Marker([34.879610, 136.551980],
                popup='<div><div><h1 align="center"><strong>Suzuka</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/F1_2014_JAP_Lewis_Hamilton_4968.jpg/1200px-F1_2014_JAP_Lewis_Hamilton_4968.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 31 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>83.78% of the F1 events hosted by Japan took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Suzuka Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Japanese Grand Prix</b></li><li><b>Suzuka 8 Hours</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.807  km (3.608 mi)</b></li><li><b>Turns:17</b></li><li><b>Race lap record:<li><b>1:30.983 (United Kingdom Lewis Hamilton, Mercedes, 2019)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([36.312830, 139.806720],
                popup='<div><div><h1 align="center"><strong>Oyama</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Fuji_speedway_eastgate.JPG/1200px-Fuji_speedway_eastgate.JPG"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 4 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>10.81% of the F1 events hosted by Japan took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Fuji Speedway</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Asian Le Mans Series</b></li><li><b>FIA World Endurance Fuji 6 Hours</b></li><li><b>Japanese Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.563  km (2.835 mi)</b></li><li><b>Turns:17</b></li><li><b>Race lap record:<li>1:18.426 (Brazil Felipe Massa, Ferrari F2008, Formula One, 2008)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([34.672031, 133.917084],
                popup='<div><div><h1 align="center"><strong>Okayama</strong></h1></div><div><img src="resources/okayama.jpg"    width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 2 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>5.40% of the F1 events hosted by Japan took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Okayama International Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>SUPER GT</b></li><li><b>Super Taikyu</b></li><li><b>F1 Pacific Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.703 km (2.300 mi)</b></li><li><b>Turns:13</b></li><li><b>Race lap record:<li><b>1:14.023 (Germany Michael Schumacher, Benetton B194, 1994)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#China
#Country itself

folium.Marker([28.226970, 113.517403],
                popup='<div><div><h1 align="center"><strong>China</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/1200px-Flag_of_the_People%27s_Republic_of_China.svg.png"   width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 16 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 12.90% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>China has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Shanghai International Circuit</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([31.230391, 121.473701],
                popup='<div><div><h1 align="center"><strong>Shanghai</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Shanghai_Circuit_Main_Grandstand_o.jpg/1200px-Shanghai_Circuit_Main_Grandstand_o.jpg"     width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 16 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by China took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Shanghai International Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Chinese Grand Prix</b></li><li><b>4 Hours of Shanghai</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	5.451 km (3.388 mi)</b></li><li><b>Turns:16</b></li><li><b>Race lap record:<li><b>1:32.238 (Germany Michael Schumacher, Ferrari, 2004)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#UAE
#Country itself

folium.Marker([23.424076, 53.847816],
                popup='<div><div><h1 align="center"><strong>UAE</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/1200px-Flag_of_the_United_Arab_Emirates.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 12 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 9.67% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>UAE has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Yas Marina Circuit</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities

folium.Marker([24.453884, 54.377342],
                popup='<div><div><h1 align="center"><strong>Abu Dhabi</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/YasMarina1.jpeg/1200px-YasMarina1.jpeg"     width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 12 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by UAE took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Yas Marina Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Abu Dhabi Grand Prix</b></li><li><b>GP2 Asia Series</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	5.554 km (3.451 mi)</b></li><li><b>Turns:21</b></li><li><b>Race lap record:<li><b>1:39.283 (United Kingdom Lewis Hamilton, Mercedes, 2019)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Korea
#Country itself

folium.Marker([35.907757, 127.766922],
                popup='<div><div><h1 align="center"><strong> South Korea</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/1200px-Flag_of_South_Korea.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 3 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 2.41% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>South Korea has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Korean International Circuit</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)



#Cities

folium.Marker([35.154723, 126.827245],
                popup='<div><div><h1 align="center"><strong>Yeongam Country</strong></h1></div><div><img src="resources/kore.jpg"     width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 3 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Korea took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Korean International Circuit</h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Korean Grand Prix</b></li><li><b>Challenge Asia</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	5.615 km (3.489 mi)</b></li><li><b>Turns:18</b></li><li><b>Race lap record:<li><b>1:39.605 (Germany Sebastian Vettel, Red Bull Racing, 2011)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Azerbaijan
#Country itself

folium.Marker([40.143105, 47.576927],
                popup='<div><div><h1 align="center"><strong> Azerbaijan</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Azerbaijan.svg/1200px-Flag_of_Azerbaijan.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 4 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 3.22% of the Asian F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Azerbaijan has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Baku City Circuit</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)


#Cities

folium.Marker([40.409264, 49.867092],
                popup='<div><div><h1 align="center"><strong>Baku</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Baku_City_Circuit%2C_April_9%2C_2018_SkySat.jpg/1200px-Baku_City_Circuit%2C_April_9%2C_2018_SkySat.jpg"      width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 4 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Azerbaijan took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Baku City Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Azerbaijan Grand Prix</b></li><li><b>FIA Formula 2</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	6.003 km (3.73 mi)</b></li><li><b>Turns:20</b></li><li><b>Race lap record:<li><b>1:43.009 (Monaco Charles Leclerc, Ferrari, 2019, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Africa
#South Africa
#Country itself

folium.Marker([-29.764377, 22.026725],
                popup='<div><div><h1 align="center"><strong>South Africa</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/1200px-Flag_of_South_Africa.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 23 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 95.83% of the African F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>South Africa has 2 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Prince George Circuit</b></li><li><b>Kyalami</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([-32.153690, 26.446400],
                popup='<div><div><h1 align="center"><strong>Eastern Cape Province</strong></h1></div><div><img src="resources/prince george.jpg"      width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 3 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>12.5% of the F1 events hosted by South Africa took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Prince George Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>South African Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.920 km (2.436 mi)</b></li><li><b>Turns:8</b></li><li><b>Race lap record:<li><b>1:27.6 (Jim Clark, Lotus-Climax 1965)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([-25.975300, 28.118870],
                popup='<div><div><h1 align="center"><strong>Midrand</strong></h1></div><div><img src="resources/kya.jpg"      width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 20 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>83.33% of the F1 events hosted by South Africa took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Kyalami </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>South African Grand Prix(1967-1985;1992-1993)</b></li><li><b>Kyalami 9 Hours</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.522 km (2.810 mi)-2016</b></li><li><b>Turns:18 (2016)</b></li><li><b>Race lap record:<li><b>1:27.6 1:17.578 (United Kingdom ,Nigel Mansell, Williams-Renault FW14, 1992, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Morocco
#Country itself

folium.Marker([30.221102, -8.982166],
                popup='<div><div><h1 align="center"><strong>Morocco</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Morocco.svg/1200px-Flag_of_Morocco.svg.png"    width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held only one F1 event from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 4.16% of the African F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Morocco has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Ain-Diab Circuit</b></li><li><b>Ain-Diab Circuit </b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([33.596458, -7.615480],
                popup='<div><div><h1 align="center"><strong>Casablanca</strong></h1></div><div><img src="resources/aindiab.jpg"      width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Morocco took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Ain-Diab Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>South Moroccan Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:7.618km (4.734 mi)</b></li><li><b>Turns:14</b></li><li><b>Race lap record:<li><b>2:22.5,Stirling Moss,Vanhall,1958</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Canada
#Country itself

folium.Marker([49.439557, -76.221555],
                popup='<div><div><h1 align="center"><strong>Canada</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/1200px-Flag_of_Canada_%28Pantone%29.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 50 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 35.71% of the North American F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Canada has 3 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Circuit Gilles Villeneuve</b></li><li><b>Mosport International Raceway</b></li><li><b>Circuit Mont-Tremblant </b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([45.501690, -73.567253],
                popup='<div><div><h1 align="center"><strong>Montreal</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/e/e8/MTL-turn2exit-f1canadiangp.png"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 40 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>80% of the F1 events hosted by Canada took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Gilles Villeneuve </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Canadian Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.361km (2.709 mi)</b></li><li><b>Turns:14</b></li><li><b>Race lap record:<li><b>1:13.078 (Finland Valtteri Bottas,Mercedes, 2019)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([51.253777, -85.323212],
                popup='<div><div><h1 align="center"><strong>Ontario</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Moss_Corner_Turn_5a_and_5b_at_Canadian_Tire_Motorsport_Park.jpg/1200px-Moss_Corner_Turn_5a_and_5b_at_Canadian_Tire_Motorsport_Park.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 8 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>16% of the F1 events hosted by Canada took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name: Mosport International Raceway </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Canadian Grand Prix</b></li><li><b>FIM Road Racing World Championship</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.957km (2.458 mi)</b></li><li><b>Turns:10</b></li><li><b>Race lap record:<li><b>1:13.299,Mario Andretti,1977</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([52.939915, -73.549133],
                popup='<div><div><h1 align="center"><strong>Quebec</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Mont-Tremblant_Control_Tower.JPG/1200px-Mont-Tremblant_Control_Tower.JPG"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 2 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>4% of the F1 events hosted by Canada took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Mont-Tremblant </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Canadian Grand Prix</b></li><li><b>Trans-Am</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.26 km (2.65 mi)-2004</b></li><li><b>Turns:17</b></li><li><b>Race lap record:<li><b>1:16.776 (Tristan Gommendy, Panoz DP01, 2007, Champ Car)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)


#USA
#Country itself

folium.Marker([56.130367, -106.346771],
                popup='<div><div><h1 align="center"><strong>USA</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/1200px-Flag_of_the_United_States.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 70 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 50% of the North American F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>USA has 10 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Indianapolis Motor Speedway</b></li><li><b>Phoenix Street Circuit</b></li><li><b>Detroit Street Circuit</b></li><li><b>Fair Park Circuit</b></li><li><b>Long Beach Circuit</b></li><li><b>Caesars Palace Circuit</b></li><li><b>Watkins Glen Circuit </b></li><li><b>Sebring International Raceway </b></li><li><b>Circuit Of The Americas </b></li><li><b>Riversade International Raceway </b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([39.768402, -86.158066],
                popup='<div><div><h1 align="center"><strong>Indianapolis</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Formula_one.jpg/1200px-Formula_one.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 19 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>27.14% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Indianapolis Motor Speedway </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Indianapolis 500</b></li><li><b>IndyCar Series</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:2.605 mi (4.192 km)</b></li><li><b>Turns:13</b></li><li><b>Race lap record:<li><b>1:10.399, 133.546 mph 214.921 km/h (Brazil Rubens Barrichello, Ferrari F2004, 2004, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([33.448376, -112.074036],
                popup='<div><div><h1 align="center"><strong>Phoenix</strong></h1></div><div><img src="resources/phoenix (1).jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 3 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>4.28% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Phoenix Street Circuit  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:<ul><li><b>3.800 km (2.361 mi)(1989-1990)</b></li><li><b>	3.721 km (2.312 mi)(1991)</b></li></ul><li><b>Turns:<ul><li><b>15(1989-1990)</b></li><li><b>15 (1991)</b></li></ul><li><b>Race lap record:<ul><li><b>1:31.050 (Austria Gerhard Berger, McLaren-Honda MP4/5B, 1990)(1989-1990)</b></li><li><b>1:21.434 (Brazil Ayrton Senna, McLaren-Honda MP4/6, 1991)</b></li></ul></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([42.331429, -83.045753],
                popup='<div><div><h1 align="center"><strong>Detroit</strong></h1></div><div><img src="resources/detroit1.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 7 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>10% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Detroit Street Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>CART</b></li><li><b>Trans-Am</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:<ul><li><b>	4.168 km (2.590 mi)(1982)</b><li><b>	4.023 km (2.499 mi)(1983-1988)</b></li></ul></li><li><b>Turns:<ul><li><b>24(1982)</b></li><li><b>22(1983-1988)</b></li></ul><li><b>Race lap record:<ul><li><b>1:50.438 (France Alain Prost, Renault RE30B, 1982)-1982</b><li><b>1:40.464 (Brazil Ayrton Senna, Lotus-Honda 99T, 1987)-(1923-1988)</b></li></ul></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)


folium.Marker([32.776665, -96.796989],
                popup='<div><div><h1 align="center"><strong>Dallas</strong></h1></div><div><img src="resources/dallasc.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>1.42% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Fair Park Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Dallas Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.901 km (2.424 miles)</b></li><li><b>Turns:23</b></li><li><b>Race lap record:<li><b>1:45.353, Austria Niki Lauda, McLaren-TAG</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([36.778259, -119.417931],
                popup='<div><div><h1 align="center"><strong>California</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Mark_Smith_Long_Beach_Grand_Prix_1993_Indy_car_race_CART.jpg"      width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 9 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>12.85% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>1.Circuit Name:Long Beach Circuit </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Long Beach Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:1.968 mi (3.167 km)</b></li><li><b>Turns:11</b></li><li><b>Race lap record:<li><b>1:06.2254 (Hélio Castroneves, Dallara DW12 Chevrolet, 2017, IndyCar)</b></li></div><br><div><h4 align="center">2.Circuit Name:Riversade International Raceway </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>United States Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.271 km (3.275 mi)</b></li><li><b>Turns:9</b></li><li><b>Race lap record:<li><b>1:56.3 (Jack Brabham 1960)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([38.802608, -116.419388],
                popup='<div><div><h1 align="center"><strong>Nevada</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Derek_Warwick_Las_Vegas_1982.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 2 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>2.85% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Caesars Palace Circuit  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Las Vegas Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.650 km (2.268 mi)-1982</b></li><li><b>Turns:14</b></li><li><b>Race lap record:<li><b>1:19.639, Michele Alboreto, Tyrrell-Ford, 1982</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([40.712776, -74.005974],
                popup='<div><div><h1 align="center"><strong>New York</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Tom_pryce_watglen_75_full.jpg/1200px-Tom_pryce_watglen_75_full.jpg"       width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 20 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>28.57% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Watkins Glen Circuit   </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>United States Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.435 km (3.377 mi)</b></li><li><b>Turns:11</b></li><li><b>Race lap record:<li><b>1:33.291 (Bruno Giacomelli, Alfa Romeo, 1980)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([27.664827, -81.515755],
                popup='<div><div><h1 align="center"><strong>Florida</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/2018_12_Hours_of_Sebring_Sunset_Bend.jpg/1200px-2018_12_Hours_of_Sebring_Sunset_Bend.jpg"        width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 1 F1 event from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>1.42% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Sebring International Raceway   </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>IMSA WeatherTech SprotsCar</b></li><li><b>12 Hours of Sebring</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:8.66 km (5.38 mi)</b></li><li><b>Turns:14</b></li><li><b>Race lap record:<li><b>3:05.0 (Maurice Trintignant, 1959)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([30.267153, -97.743057],
                popup='<div><div><h1 align="center"><strong>Austin</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/2018_US_Grand_Prix_at_the_Circuit_of_the_Americas.jpg/1200px-2018_US_Grand_Prix_at_the_Circuit_of_the_Americas.jpg"        width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 8 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>11.42% of the F1 events hosted by USA took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Circuit Of The Americas   </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>United States Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:3.426 mi (5.513 km)</b></li><li><b>Turns:20</b></li><li><b>Race lap record:<li><b>1:36.169 (Monaco Charles Leclerc, Ferrari SF90, 2019)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Mexico
#Country Itself

folium.Marker([23.322080, -102.167423],
                popup='<div><div><h1 align="center"><strong>Mexico</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/1200px-Flag_of_Mexico.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 20 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 14.28% of the North American F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Mexico has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Autódromo Hermanos Rodríguez</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([19.432608, -99.133209],
                popup='<div><div><h1 align="center"><strong>Mexico City</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Grand-Am_Rolex_Series_Mexico_2008.jpg/1200px-Grand-Am_Rolex_Series_Mexico_2008.jpg"           width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 20 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Brazil took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autódromo Hermanos Rodríguez  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Mexican Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.304 km (2.674 mi)</b></li><li><b>Turns:17</b></li><li><b>Race lap record:<li><b>1:18.741 (Finland Valtteri Bottas, Mercedes, 2018, FIA Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)


#Brazil
#Country itself

folium.Marker([-14.235004, -51.925282],
                popup='<div><div><h1 align="center"><strong>Brazil</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1200px-Flag_of_Brazil.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 47 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 70.14% of the South American F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Brazil has 2 F1 circuits: <strong></h4></div><br><div><div><ul><li><b>Autódromo José Carlos Pace</b></li><li><b>Autódromo Internacional Nelson Piquet</b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([-23.550520, -46.633308],
                popup='<div><div><h1 align="center"><strong>Sao Paulo</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Michael_Schumacher_2006_Brazil_last_overtaking.jpg"            width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 37 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>78.72% of the F1 events hosted by Mexico took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autódromo José Carlos Pace  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Brazilian Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:4.309 km (2.677 mi)</b></li><li><b>Turns:15</b></li><li><b>Race lap record:<li><b>1:10.540 (Finland Valtteri Bottas, Mercedes AMG F1 W09 EQ Power+, 2018)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

folium.Marker([-22.906847, -43.172897],
                popup='<div><div><h1 align="center"><strong>Rio de Janeiro</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/A_Escuderia_Emerson_Fittipaldi_Copersucar%2C_Jacarepagua%2C_1978.tif/lossy-page1-1200px-A_Escuderia_Emerson_Fittipaldi_Copersucar%2C_Jacarepagua%2C_1978.tif.jpg"            width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 10 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>21.27% of the F1 events hosted by Brazil took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autódromo Internacional Nelson Piquet  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Brazilian Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:5.031 km (3.126 mi)</b></li><li><b>Turns:11</b></li><li><b>Race lap record:<li><b>1:32.507 (Italy Riccardo Patrese, Williams-Renault FW12C, 1989)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)

#Argentina
#Country itself

folium.Marker([-38.416096, -63.616673],
                popup='<div><div><h1 align="center"><strong>Argentina</strong></h1></div><div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/1200px-Flag_of_Argentina.svg.png"     width="250px" align="center"/></div><br><div><h4 align="center"><strong>This country held 20 F1 events from 1950 to 2020.</strong></h4></div><br><div><h4 align="center"><strong> It means that 29.85% of the South American F1 events took place here.</strong></h4></div><br><div><h4 align="center"><strgn>Argentina has only one F1 circuit: <strong></h4></div><br><div><div><ul><li><b>Autodromo Juan y Oscar Galvez </b></li></ul></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='orange')) .add_to(m)

#Cities

folium.Marker([-34.603683, -58.381557],
                popup='<div><div><h1 align="center"><strong>Buenos Aires</strong></h1></div><div><img src="resources/unnamed.jpg"            width="250px" align="center"/></div><br><div><h3 align="center"><strong>This city hosted 20 F1 events from 1950 to 2020.</strong></h3></div><br><div><strong><h3 align="center"><strong>100% of the F1 events hosted by Brazil took place here.</strong></h3></div><br><div><h4 align="center"><strong>Circuit Name:Autodromo Juan y Oscar Galvez  </h4></div><br><div><h4 align="center"></h4></div><br><div><h4 align="center">Major events:</h4></div><br><div><ul><li><b>Formula One</b></li><li><b>Argentine Grand Prix</b></li></ul></div><br><div><div><h4 align="center">Circuit Configuration:</h4></div><br><div><ul><li><b>Length:	5.968 km (3.708 mi)</b></li><li><b>Turns:16</b></li><li><b>Race lap record:<li><b>1:42.665 (Brazil Nelson Piquet, Brabham-Ford BT49C, 1981, Formula One)</b></li></ul></div></div>',
                tooltip=tooltip,
               icon=folium.Icon(color='green',icon='flag')) .add_to(m)
                
m.save('map.html')
