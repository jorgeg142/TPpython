% Cargar las reglas de par_impar.pl
:- consult('par_impar.pl').

% Predicado para verificar si un número es par o impar
verificar_par_impar(N) :-
    par(N),
    write('par').

verificar_par_impar(N) :-
    impar(N),
    write('impar').
% me costo 3 hrs porque python y mi pc se pusieron de acuerdo para buguearse