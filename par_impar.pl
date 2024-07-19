% Definición de regla para determinar si un número es par
par(N) :-
    N mod 2 =:= 0.

% Definición de regla para determinar si un número es impar
impar(N) :-
    \+ par(N).
% no me quiero aplazar profe 61 tengo que hacer
