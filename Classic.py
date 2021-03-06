class CypherText:
	kind = 'Cypher'
	def __init__(self, plaintext, method='', key=0, cypher=''):
		self.plaintext = plaintext
		self.method = method
		self.key = key
		self.cypher = cypher
		
	def flip(self):
		NewPlainText = self.cypher
		NewCypher = self.plaintext
		self.plaintext = NewPlainText
		self.cypher = NewCypher
					
	def AlphaNum(self, ABC = False):
		abc = "abcdefghijklmnopqrstuvwxyz"
def AlphaABC( ABC = False, round=False):
	#helps add a dict key to the Cyphertext class
	#round is for a viegner cypher
	key={}
	if round:
		i = 0
		looper = len(round)
		if ABC:
			for char in list("abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
				key[char] = round[i % looper]
				i = i + 1 
		else:
			for char in list("abcdefghijklmnopqrstuvwxyz"):
				key[char] = round[i % looper]
				i = i + 1 
	else:
		if ABC:
			key = {a: a for a in list("abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
		else:
			key = {a: a for a in list("abcdefghijklmnopqrstuvwxyz")}
	return key
		
def CaesarOption():
	#this is the menu for the Caesar options
	print("Hail great Caesar, which option would you like to use?")
	print "1: Caesar Cypher"
	print "2: Crack Caesar cypher"
	print "3: Vigenere Cypher"
	print "4: Vigenere Crack"
	print "5: Exit"
	answer = raw_input("?>")
	if answer == '1':
		d = CypherText(raw_input("Please print your plain text here: "), "CaesarCipher")
		d.key = int(raw_input("What key do you want to use? "))
		d.cypher = CaesarCipher(d.plaintext, d.key)
		print "This is the plain text: \n %s \n This is the Cypher Text: \n%s" % (d.plaintext, d.cypher)
		exit
	elif answer == '2':
		d = CypherText(raw_input("please input the cypher text here: "), "CeasarCrack")	
		if d.plaintext.lower() == d.plaintext or d.plaintext.upper() == d.plaintext:
			Rng = range(-25,1)
		else:
			Rng = range(-51,1)
		print "Offset : Crack"	
		for key in Rng:
			d.key = key
			d.cypher = CaesarCipher(d.plaintext,d.key)
			print "%r: %r" % (d.key, d.cypher)
		exit
	elif answer == '3':
		d = CypherText(raw_input("please input the plain text here: "), "VigenereCypher")	 
		d.key = raw_input("What is the key (word) you want to use? ")
		d.cypher = VigCipher(d.plaintext, d.key)
		print "This is the plain text: \n %s \n This is the Cypher Text: \n%s" % (d.plaintext, d.cypher)
		exit
	elif answer == '4':
	#	d = CypherText(raw_input("please input the cypher text here: "), "VigenereCrack")	
	#	d = CypherText("exkgdjxfbcjtbexucrtfgqqwwllkim", "VigenereCrack")	#windows
	#	d = CypherText("xwlqtcmxqfdbvcgqkzvtcm", "VigenereCrack") #phone
	#	d = CypherText("xvgtqihgyjvbsddg", "VigenereCrack") #taco
		d = CypherText("ubsyvkmhvyrrtsbbcrdsndwrtshxmbufrmxgabnvmircewerucamlyzbrvfwivvmlyzwapspyogsslechbgcubsvyczqrcwrmhvcxgooyvcydspomtqfpyqkgbcmerucadlcaflrsuqjrbhceqesfcehuoqmdstorcdoymeqqwaglgovggsmdabbigztbbqyfwbxwmgfpowgztyeilosrkgfahuovqfogswruqnvpwfvrnmpqqgsslatgrmqubsvyczqrswcjdeowqqroihqdspdibffnxwgztbbqyfwbxus", "VigenereCrack")	
	#	print VigR(d.plaintext)
		(g1,g2,g3)  = Kasisiki(d.plaintext)
		d.key = Kasisiki2(d.plaintext, g1[0])
		
		print "Ah,here we go: %r" % d.key
	elif answer == '5':
		print 'Adios, Caesar!'
		return none
	else:
		print "eh? What was that? didn't hear you!"
		CaesarOption()

def listsame(list1,list2):
	#counts the number of times two elements in the same location of two diffrent list are the same
	count = 0
	for i in range(0,min(len(list1),len(list2))):
			if list1[i] == list2[i]:
				count += 1
	return count
	
def VigR(cypher):
	list = []
	print max(1,len(cypher)-26)
	#for i in range(max(len(cypher) - 26,0),len(cypher)):
	#for i in range(len(cypher) - 20,len(cypher)):
	for i in range(max(1,len(cypher)-26),len(cypher)):
		print "l: %r\t\t\t -l:%r" % (cypher[:i], cypher[-i:])
		list.append(round(listsame(cypher[:i],cypher[-i:])/(i+1.00),2))
	return list	

def StringSearch(str, search):
	#searches for all matches in a string (str) of search	
	d=[]
	d.append(str.find(search))
	while str.find(search,max(d)+1) != -1 :
		d.append(str.find(search,max(d)+1))
	if len(d) == 1:
		return False
	else:
		return d
def factors(n):    
	#produces a list of factors for a given number
    return reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))

def maxgcd(num, l):
	#goes through a list and compares the numbers to pull out the maximum GCD
	set = 0
	for i in range(0,len(l)):
		GCD = gcd(num,l[i])
		if num != l[i] and set < GCD :
			set = GCD
	return set
			
def gcd(x, y):
	#greatest Common Divisor
    while y != 0:
        (x, y) = (y, x % y)
    return x
	
def Kasisiki(cypher):
	#This uses the Kasisiki method of finding common groupings of letters 
	#First step in the cypher method
	diffdict = {}
	gcddict = {}
	difflist = []
	for SC in range(2, 6):
		for i in range(1, min(len(cypher),52)):
			result = StringSearch( cypher,cypher[ i : i + SC ])
			if result:
				for i in range(0,len(result)-1):
					difflist.append(result[i+1] - result[i])
	difflist2 = list(set(difflist))
	difflist2.sort()
	g1 = (0,0)
	g2 = (0,0)
	g3 = (0,0)
	for i in difflist:
		d = maxgcd(i,difflist2)
		diffdict[d] = diffdict.get(d,0) + 1
		if g3[1] < diffdict[d]:
			if g1[1] < diffdict[d]:
				g1 = (d, diffdict[d])
			if g2[1] < diffdict[d] and g1[0] != d :
				g2 = (d,diffdict[d])
			if g3[1] < diffdict[d] and g1[0]!= d and g2[0]!=d:
				g3 = (d, diffdict[d])
	print "Here are the top 3 guesses, along with frequency count: \n1st: %r\n2nd: %r\n3rd %r\n" % (g1,g2,g3)
	return (g1,g2,g3)
def Kasisiki2(cypher, key):
	# this is the second step, where we break the cypher up into multiple (one row per 'key' character)
	# then look for frequency anlysis  (ie, e shows up the most time, well then work from there
	d = ['a'] * key
	results = ['a'] * key
	ky = 0
	cypher.lower()
	print cypher, "\n"
	while ky < key:
		i = ky
		print ky
		substr = ''
		while i < len(cypher):
			substr += cypher[i]
			i += key
		substr = list(substr)
		x = ('a',0)
		for i in list('abcdefghijklmnopqrstuvwxyz'):
		#	print i, substr.count(i)
			if substr.count(i) > x[1]:
				x = (i, substr.count(i))
		
		d[ky] = x 
		results[ky] = chr((ord(x[0]) - 97 - 4) % 26 + 97)
		ky += 1

	print d
	print results
	return ''.join(results)
	#for i in diffdict:
	#	gcddict[gcd( i, diffdict[i]
	
					
	
	
def CaesarCipher(plaintext, key):
	#the purpose of this is to either create a Caesar Cipher or decrypt one by moving each letter
	#key number of places (if key is < 0, then we are moving backwards it)
	#this cypher will scramble symbols and numbers into a different range then alpha range
	if plaintext.lower() == plaintext:
		#all lower case
		for char in range(0,len(plaintext)):
			#-97 to get only lower case, adding key, mod 26, then + 97 for proper ASCI
			plaintext = plaintext[:char] +  chr((((ord(plaintext[char])- 97) + key) % 26) + 97) + plaintext[char + 1:]
			
	elif plaintext.upper() == plaintext:
		#all upper case
		for char in range(0,len(plaintext)):
			#-65 to get only upper case chars, adding key, mod 26, then + 65 for proper ASCI
			plaintext = plaintext[:char] +  chr((((ord(plaintext[char])- 65) + key) % 26) + 65) + plaintext[char + 1:] 
	else:
		#Both upper and lower case
		for char in range(0,len(plaintext)):
			ch = (((ord(plaintext[char])- 65) + key) % 58) + 65
			if ch in range(91,97): # moving through the [, \\ , ], ^,_,' of ASCII
				ch = ch + key/abs(key) * 6
			plaintext = plaintext[:char] +  chr(ch) + plaintext[char + 1:] 
	return plaintext
def VigCipher(plaintext, key):
	#the purpose of this is to create a Vigenere cypher and move each lever by the key (a word)
	#key number of places (if key is < 0, then we are moving backwards it)
	#this cypher will scramble symbols and numbers into a different range then alpha range
	# -96,-64 is becuase on the key I want a to = 1, not 0
	Len = len(key)
	i = 0
	if plaintext.lower() == plaintext:
		#all lower case
		for char in range(0,len(plaintext)):
			#-97 to get only lower case, adding key, mod 26, then + 97 for proper ASCI
			plaintext = plaintext[:char] +  chr((((ord(plaintext[char])- 97) + ord(key[i]) - 96) % 26) + 97) + plaintext[char + 1:]
			i = (i + 1) % Len
			
	elif plaintext.upper() == plaintext:
		#all upper case
		for char in range(0,len(plaintext)):
			#-65 to get only upper case chars, adding key, mod 26, then + 65 for proper ASCI
			plaintext = plaintext[:char] +  chr((((ord(plaintext[char])- 65) + ord(key[i]) - 64) % 26) + 65) + plaintext[char + 1:] 
			i = (i + 1) % Len
	else:
		#Both upper and lower case
		for char in range(0,len(plaintext)):
			ch = (((ord(plaintext[char])- 65) + ord(key[i]) - 64) % 58) + 65
			if ch in range(91,97): # moving through the [, \\ , ], ^,_,' of ASCII
				ch = ch + 6
			plaintext = plaintext[:char] +  chr(ch) + plaintext[char + 1:] 
			i = (i + 1) % Len
	return plaintext
	
	
def AlphaDict(Upcase = False):
	#generates a dict with the same key and value pair
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	if Upcase:
		alphabet = alphabet + alphabet.upper()
	return {al:al for al in list(alphabet)}

def partword(Word):
	i=0
	Rng = range(i,len(Word)+1)
	PrintWord = ''
	while i <= len(Word):
		PrintWord = PrintWord + Word[i:i+5] + ' '
		i = i + 5
	print PrintWord
	
def SubOption():
	#This is for the substitution cypher subscreen
	print "OOOOOOOO, panzy, here is the SUBSTITUION OPTIONS"
	print "1. Create a substitution cypher from plaintext"
	print "2. Crack a substitution"
	print "3. exit"
	ans = raw_input("?> ")
	if ans == '1':
		d = CypherText(raw_input("Please print your plain text here: "), "Substitution")
		d.key = AlphaABC(True)
		d.key = SubAlpha()
		d.cypher = SubCypher(d.plaintext, d.key)
		print("Here is the original Text: \n %r \n Here is the cypher: \n %r") % (d.plaintext, d.cypher)
		print d.key
		exit
	elif ans == '2':
		#d = CypherText(raw_input("please put in the cypher text: "),"Crack Substitution",{})
		d = CypherText("rgjjgmvktotzpgtstbgpcatjwpgocmgjs","Crack Substitution",{})
		while True:
			looper = raw_input("Would you like to guess a few translations? :").lower()
			if looper in ('y','ye','yes',' y',' ye',' yes','y ','ye ','yes '):
				d.key = SubAlpha(d.key)
			d.cypher, d.key = SubDecrypt(d.plaintext, d.key,d.cypher)
			if raw_input("Keep going? ").lower() in ('n','no',' n',' no','n ','no '):
				break
		exit
	else:
		exit
	
def SubAlpha(alpha={}):
	while True:
		print alpha.keys()
		print alpha.values()
		print "hit enter to quit"
		key = raw_input("What character do you want to replace? > ")
		if key == '':
			break
		value = raw_input("And what do you want to replace it with? > ")
		if key == '':
			break
		alpha[key] = value
	return alpha
	
def SubCypher(plaintext, alpha={}):
	#This does a substitution method
	#it returns the cypher and the dictionary used
	for i in range(0,len(plaintext)):
		plaintext = plaintext[:i] +  alpha.get(plaintext[i],plaintext[i]) + plaintext[i + 1:] 
	return  plaintext
	
def BuildAlpha(cypher, word, alpha={}):
	#checks to see if the cypher word is mapped to the proper word or blanke
	#then updates aplha with a new mapping or returns FALSE if a conflict arises
	for i in range(0,len(cypher)):
		if not alpha.has_key(cypher[i]) or alpha[cypher[i]] == word[i]:
			alpha[cypher[i]]=alpha.get(cypher[i],word[i])
		else:
			return False
	return alpha
		
def SubDecrypt(cypher, alpha = {},plaintext=''):
	guessword = raw_input("What word do you believe is in the cypher text? ")
	guessnum, guessmap = WordMapping(guessword)
	Rng = range(0,len(cypher) - len(guessword)+1)
	for i in Rng:
		
		Cyph, Cyphmap = WordMapping(cypher[i:i+len(guessword)])
		if Cyph == guessnum:
			print "We have a match! Cypher is %r \t Guess-word is %r" % (cypher[i:i+len(guessword)], guessword)
			print "Checking to see if it matches with the current dictionary:"
			if BuildAlpha(cypher[i:i+len(guessword)], guessword, alpha) == False:
				print "Looks like we have a match error, continuing down the path"
				continue
			print "match!"
	
	print "here is translation thus far:"
	partword(cypher)
	plaintext = SubCypher(cypher, alpha)
	partword(plaintext)
			
	return ( plaintext, alpha)
		
def WordMapping(String):
	String = list(String)
	OutStr = ''
	Map = {}
	Rmap = {}
	i = -1
	for char in String:
		if not Map.has_key(char):
			i = i + 1
		Map[char] = str(Map.get(char,i))
		Rmap[i] = char
		OutStr = OutStr + Map[char]
	return (''.join(OutStr), Rmap)

	
print "Welcome to the basic Cypher Crack, how may I help you?"
print "1: Caesar Options"
print "2: Simple substitution options"
print "3: Test the Cypher class"
ans =  raw_input("?> ")
if ans == '1':
	CaesarOption()
	exit
elif ans == '2':
	SubOption()
	exit
else:
	exit
#http://www.martani.net/2011/04/cracking-vigenere.html
