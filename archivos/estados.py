
def estado():
    #diccionario con la representación gráfica del estado del juego
    #autor: Ignacio Chacón
   rv = {
    0 : """
            -----
            |   |
            |   
            |  
            |  
            |
            |
         ___|___""",
    1:  """
            -----
            |   |
            |   0
            |   
            |  
            |  
            |
         ___|___""",  
    2 : """
            -----
            |   |
            |   0
            |   |
            |  
            |  
            |
         ___|___""",
    3 : """
            -----
            |   |
            |   0
            |  /|
            |  
            |  
            |
         ___|___""",
    4 : """
            -----
            |   |
            |   0
            |  /|/
            |  
            |  
            |
         ___|___""",
    5 : """
            -----
            |   |
            |   0
            |  /|/
            |  /
            |  
            |
         ___|___""",
    6 : """
            -----
            |   |
            |   0
            |  /|/
            |  //
            |  
            |
         ___|___""",
    7 : """
            -----
            |   |
            |   0
            |  /|/
            |  //
            |  RIP
            |
         ___|___"""}
   return rv
