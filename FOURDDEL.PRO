domains
 list=integer*
 predicates
 del(integer,list,list)
 clauses
 del(X,[X|T],T).
 del(X,[H|T],[H|T1]):
del(X,T,T1).