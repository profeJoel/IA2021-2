temp_f(santiago,70).
temp_f(arica,90).
temp_f(punta_arenas, 30).
temp_f(puerto_montt, 50).

%regla
temp_c(CIUDAD,TEMP_C) :- 
    temp_f(CIUDAD,TEMP_F),
    TEMP_C is (TEMP_F - 32) * 5/9.