domains
 person=address(name,street,city,state,zip)
 name,street,city,state,zip=String
 predicates
 readaddress(person)
 go
 clauses
 go:
readaddress(Address),nl,write(Address),nl,nl,
 write("Accept(y/n)?"),readchar(Reply),Reply='y',!.
 go:
nl,write("please re-enter"),nl,go.
 readaddress(address(N,street,city,state,zip)):
write("Name:"),readln(N),
 write("Street:"),readln(street),
 write("City:"),readln(city),
 write("State:"),readln(state),
 write("Zip:"),readln(zip).