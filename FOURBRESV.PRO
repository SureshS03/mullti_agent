 domains
 x=integer
 list=integer*
 predicates
 append(x,list,list)
 rev(list,list)
 clauses
 append(X,[],[X]).
 append(X,[H|T],[H|T1]):-append(X,T,T1). rev([],[]).
 rev([H|T,rev):-rev(T,L),append(H,L,rev).