domains
 x=integer
 list=integer*
 predicates
 count(list,x)
 clauses
 count([],0).
 count([_|T],N):-count(T,N1),N=N1+1.