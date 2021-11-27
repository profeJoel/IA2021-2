%hechos - > base de conocimiento
% categoria(instancia).
gato(juanito).
gato(garfield).
gato(gato_con_botas).
gato(don_gato).
gato(tom).
gato(doraemon).
gato(neko).
gato(hello_kitty).
gato(silvestre).
gato(felix).

raton(mickey).
raton(jerry).
raton(speedy_gonzalez).
raton(mini).
raton(remi).
raton(cerebro).
raton(pinky).
raton(stuart_little).

%relaciones
enemigos(tom,jerry).
amigos(pinky,cerebro).
se_gustan(mickey, mini).

% reglas -> razonamiento: deducción o inducción - conjuntivas o disjuntivas

cartoon(X,Y) :- gato(X),raton(Y),enemigos(X,Y).

/** Formato de las reglas
:- se lee "si" o "implica que"
, es una conjunción de la regla A,B
; es un disjunción de la regla A;B

P :- Q;R.
P :- Q.
P :- R.

P :- Q,R;S,T,U.
P :- (Q,R);(S,T,U).
P :- Q,R.
P :- S,T,U.
*/

amigos(X,Y) :- not(enemigos(X,Y)).
amigos(X,Y) :- se_gustan(X,Y).

pareja(X,Y) :- se_gustan(X,Y).