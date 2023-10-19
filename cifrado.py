import operator

#Aqui irá el texto que queramos descifrar:
texto="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

diccionario={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

for indice,caracter in enumerate(texto):
	#if caracter!=' ' and caracter!=',' and caracter!='.' and caracter!='0' and caracter!='1' and caracter!='2':
	if caracter.isalpha() and caracter.isupper():
		diccionario[caracter]+=1

lista_ord=sorted(diccionario.items(),key=operator.itemgetter(1),reverse=True)

print(lista_ord)
print(" ")
textoDescifrado = texto
#Aqui irá la frecuencia de letras que nos den (por orden):
letrasOrdPorFreq = ['e','a','o','l','s','n','d','r','u','i','t','c','p','m','y','q','b','h','g','f','V','j','ñ','z','x','k','w']
cont=0

#en la lista de las letras ordenadas por las frecuencias en castellano hay que ver si estan algunas descifradas o no.

for par in lista_ord:
	#print(par[0])
	textoDescifrado=textoDescifrado.replace(par[0],letrasOrdPorFreq[cont])
	cont+=1
	
print(textoDescifrado)
print(" ")
#hay letras que ya estarán bien puestas según el análisis de frecuencias (no hay que reemplazar todas)
#NO HAY QUE CAMBIAR NADA POR v PORQUE ESA YA ESTA PUESTA
textoDescifrado=textoDescifrado.replace('d','l'.upper()); 
textoDescifrado=textoDescifrado.replace('o','r'.upper());
textoDescifrado=textoDescifrado.replace('r','d'.upper()); 
textoDescifrado=textoDescifrado.replace('p','m'.upper());
textoDescifrado=textoDescifrado.replace('l','o'.upper());
textoDescifrado=textoDescifrado.replace('h','j'.upper());
textoDescifrado=textoDescifrado.replace('u','c'.upper());
textoDescifrado=textoDescifrado.replace('s','i'.upper());
textoDescifrado=textoDescifrado.replace('q','b'.upper());
textoDescifrado=textoDescifrado.replace('i','u'.upper());
textoDescifrado=textoDescifrado.replace('b','q'.upper());
textoDescifrado=textoDescifrado.replace('c','s'.upper());
textoDescifrado=textoDescifrado.replace('ñ','z'.upper());
textoDescifrado=textoDescifrado.replace('y','f'.upper());
textoDescifrado=textoDescifrado.replace('m','p'.upper());
textoDescifrado=textoDescifrado.replace('g','y'.upper());
textoDescifrado=textoDescifrado.replace('f','g'.upper());
textoDescifrado=textoDescifrado.replace('j','x'.upper());
textoDescifrado=textoDescifrado.replace('V','h'.upper()); #la 'v' que estaba ya descifrada en el texto codificado se mantendrá como 'v', las otras que se han puesto tras hacer el análisis de frecuencias no, porque son 'V'

#print(textoDescifrado) #comentar esta línea al acabar de descifrar todo el texto
print(textoDescifrado.upper()) #comentar esta línea durante el descifrado y descomentarla al acabar de descifrar todo el texto, para que salga todo en mayúscula

