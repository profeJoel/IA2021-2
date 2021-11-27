mas_grande(elefante,caballo).
mas_grande(caballo,burro).
mas_grande(burro, perro).
mas_grande(burro,mono).
mas_grande(mono,hormiga).
mas_grande(perro,hormiga).

%regla
mas_grande(X,Y) :- mas_grande(X,Z),mas_grande(Z,Y).