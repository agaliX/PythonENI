######################################
##        Suite de Fibonacci        ##
######################################

print """
                                   I
			        I  I  I
			   IIIIIIIIIIIIIIII
		        ======================
			   IIIIIIIIIIIIIIII
			    ==============
			        \\   \\
			         �    �				  
				  �   �
			  	   �  �
				     ��
				      ��
			        ______  �*�/____  _____    _______
                               |   ___|   /�**** ||  _  |  |  ___  |
                               |  |__	    | |	  | | | |  | |   | |
                               |   __|	    | |	  | |_| |_ | |	 | |		
                               |  |	    | |	  | |   | || |	 | |
                               |  |	 ___| |__ | |__ | || |___| |
                               |__|	|________||_______||_______|
"""

nombre = input ("nombre limite : ") ## limite demand�e par l'utilisateur

a,b,c = 1,1,1                       ## Suite

while b < nombre:                   ## Tant que la valeur B n'est pas �gal � la limite demand�e, ajouter la valeur
                                    ## du r�sultat pr�c�dent au compte courant
    a,b,c = b,a+b,c+1
    print(a)                        ## Afficher la valeur du compte courant

