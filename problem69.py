#https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))



#Roman numerals I 	V 	X 	L 	 C 	     D 	 M
#               1 	5 	10 	50 	100 	500 1000

#some special cases as we cant have more than III one after each other
"""
 	Thousands 	Hundreds 	Tens 	Units
1 	    M           C 	      X 	   I
2 	    MM          CC 	      XX 	   II
3 	    MMM         CCC 	  XXX 	   III
4 		            CD 	       XL 	    IV
5 		            D 	        L 	     V
6 		            DC 	       LX 	    VI
7 		            DCC 	   LXX 	    VII
8 		            DCCC 	   LXXX 	VIII
9 		            CM 	        XC 	     IX
"""
# Well be looking at this table