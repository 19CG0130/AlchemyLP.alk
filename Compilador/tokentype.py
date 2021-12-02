#Definir todos los tokens y enumerarlos
#Alt + 175 = »
import enum
class TokenType(enum.Enum):
    materia = -1 #EOF
    triaPrima = 0 #NEWLINE
    azufre = 1 #NUMBER
    mercurio = 2 #IDENT
    sal = 3 #STRING
    #TRANSMUTE (KEYWORDS)
    mentalismo = 101 #LABEL
    GOTO = 102 #GOTO
    manifestar = 103 #PRINT
    proyeccion = 104 #INPUT
    LET = 105 #LET
    causaYEfecto = 106 #IF
    efectoYCausa = 107 #THEN
    putrefaccionCausaYEfecto = 108 #ENDIF
    polaridad = 109 #WHILE
    REPEAT = 100 #REPEAT
    putrefaccionPolaridad = 111 #ENDWHILE
    implementar = 112 #DECLARA

    #MATTER (OPERADORES)
    disolucion = 201 #EQ
    calcinacion = 202 #PLUS
    congelacion = 203 #MINUS
    dijestion = 204 #ASTERISK
    fijacion = 205 #SLASH
    cancer = 206 #EQEQ
    destilacion = 207 #NOTEQ
    sublimacion = 208 #LT 
    precipitacion = 209 #LTEQ
    oro = 210 #GT
    sol = 211 #GTEQ