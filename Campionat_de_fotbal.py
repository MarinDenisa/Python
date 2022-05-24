class Echipa:
	def __init__(self, nume, puncte, nrGoluriDate, nrGoluriPrimite):	
		self.nume = nume
		self.puncte = puncte
		self.nrGoluriDate = nrGoluriDate
		self.nrGoluriPrimite = nrGoluriPrimite
	def __lt__(self, other): #definim operatorul < (lt = less than)
		return self.puncte < other.puncte

k = int(input())
n = int(input())
echipe = []


for i in range(n):
	meci = input()
	meci = meci.split()
	nume1 = meci[0] 
	nrgoluriDate1 = int(meci[1]) 
	nrgoluriDate2 = int(meci[3]) 
	nume2 = meci[4] 

	gasitEchipa1, gasitEchipa2 = False, False 
	for e in range(len(echipe)): 
		if echipe[e].nume == nume1: 
			echipe[e].nrGoluriDate += nrgoluriDate1 
			echipe[e].nrGoluriPrimite += nrgoluriDate2 
			if nrgoluriDate1 > nrgoluriDate2:
				echipe[e].puncte += 3 
			elif nrgoluriDate1 == nrgoluriDate2:
				echipe[e].puncte += 1 
			gasitEchipa1 = True 
		if echipe[e].nume == nume2: 
			echipe[e].nrGoluriDate += nrgoluriDate2 
			echipe[e].nrGoluriPrimite += nrgoluriDate1 
			if nrgoluriDate2 > nrgoluriDate1:
				echipe[e].puncte += 3 
			elif nrgoluriDate1 == nrgoluriDate2:
				echipe[e].puncte += 1 
			gasitEchipa2 = True 
		if gasitEchipa1 == True and gasitEchipa2 == True:
			break 

	puncte = 0
	if gasitEchipa1 == False: 
		if nrgoluriDate1 > nrgoluriDate2:
				puncte = 3 
		elif nrgoluriDate1 == nrgoluriDate2:
			puncte = 1 
		else:
			puncte = 0 
		echipe.append(Echipa(nume1, puncte, nrgoluriDate1, nrgoluriDate2)) 
	if gasitEchipa2 == False: 
		if nrgoluriDate2 > nrgoluriDate1:
				puncte = 3 
		elif nrgoluriDate1 == nrgoluriDate2:
			puncte = 1 
		else:
			puncte = 0 
		echipe.append(Echipa(nume2, puncte, nrgoluriDate2, nrgoluriDate1))


echipe.sort(reverse = True) 
for e in echipe: 
	print(e.nume, e.puncte, e.nrGoluriDate, e.nrGoluriPrimite) 
