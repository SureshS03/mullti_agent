 domains
 town = symbol
 distance = integer
 predicates
 nondeterm road(town, town, distance)
 nondeterm route(town, town, distance)
 clauses
 road("coimbatore", "madurai", 950).
 road("trichy", "madurai", 750).
 road("coimbatore", "trichy", 250).
 road("trichy", "chennai", 300).
 road("coimbatore", "chennai", 500).
 route(Town1, Town2, Distance) :
road(Town1, Town2, Distance).
 route(Town1, Town2, Distance) :
road(Town1, X, Dist1),
 route(X, Town2, Dist2),
 distance = Dist1 + Dist2.