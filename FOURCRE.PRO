domains
 list=integer*
 predicates
 replace(integer,integer,list,list) clauses
 replace(X,Y,[X|T],[Y|T]).
 replace(X,Y,[H|T],[H|T1]):-replace(X,Y,T,T1).