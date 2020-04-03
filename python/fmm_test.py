from fmm import Network,NetworkGraph,STMATCH,STMATCHAlgorConfig
network = Network("../example/data/edges.shp")
graph = NetworkGraph(network)
print graph.get_num_vertices()
model = STMATCH(network,graph)
wkt = "LINESTRING(0.200812146892656 2.14088983050848,1.44262005649717 2.14879943502825,3.06408898305084 2.16066384180791,3.06408898305084 2.7103813559322,3.70872175141242 2.97930790960452,4.11606638418078 2.62337570621469)"
config = STMATCHAlgorConfig()
config.k = 4
config.gps_error = 0.5
config.radius = 0.4
result = model.match_wkt(wkt,config)
print type(result)
print list(result.opath)
print list(result.cpath)


result2 = model.match_wkt_test(wkt,config)
print type(result2)
print list(result2.opath)
print list(result2.cpath)
