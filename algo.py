import os
import collections as cl

# k is the number of variables




def run(k,minterms=None,dontcare=None):
	step1 = []
	for i in range(k+1):
		step1.append([])
	# assert len(step1) == k
	#dont care or not dictionary
	dorn = {}
	unpaired = {}
	tot = minterms+dontcare
	tot.sort()
	# print(tot)
	if len(dontcare)!=0:
		for num in dontcare:
			dorn[(num,())] = True
			unpaired[(num,())] = False
	for num in minterms:
		dorn[(num,())] = False
		unpaired[(num,())] = True

	for i,num in enumerate(tot):
		st = '0:0{}b'.format(k)
		st = '{'+st+'}'
		st = st.format(tot[i])
		no1 = 0
		for ch in st:
			no1+=int(ch)
		assert no1>=0
		# if num == 0:
		# print ("in for loop printing value no1:", no1)
		step1[no1].append((num,()))
		# tmp = step1[no1-1][:]
		# print ("step no bf; ",step1[no1-1])
		# sorted(tmp, key=lambda tpl: tpl[0])
		# print ("step no ; ",step1[no1-1])
		# step1[no1-1] = tmp

		# assert len(step1) == k
	# print ("step1",step1)
	for i in range(k):
		stepn = []
		if step1 is None :
			break
		for j in range(k-i):
			stepn.append([])
		assert len(stepn) == k-i
		#at the end of loop write that step1=stepn
		for o, lstp in enumerate(step1):
			if o == len(step1)-1:
				break
			for m,tp in enumerate(lstp):
				
				# print ("lstp : ",lstp)
				lss = list(enumerate(step1))
				l,lstp2 = lss[o+1][0],lss[o+1][1]
				for n,tp2 in enumerate(lstp2):
					# print ("lstp2 : ",lstp2)
					# assert no1>=0
					if (dorn.get(tp)==True) and (dorn.get(tp2)==True):
						continue
					if  tp[-1]==tp2[-1] :
						# print ("tp and tp2",tp,tp2)
						no1 = 0
						no2 = 0
						# print(tp2)
						diff = abs(-tp2[0]+tp[0])
						# print ("difference:",diff,tp2[0],tp[0])
						st = '0:0{}b'.format(k)
						st2 = '{'+st+'}'
						st = st2.format(diff)
						st1 = st2.format(tp[0]^tp2[0])
						# print("values ",tp[0],tp2[0],"diff ",st1)
						# st = '{0:0%db}'%(k).format(tp[1]-tp2[1])
						for ch in st:
							no1+=int(ch)
						for ch in st1:
							no2+=int(ch)
						# print ("no. of ones :",no1)
						if no1 == 1 and no2 == 1:
							unpaired[tp] = False
							unpaired[tp2] = False
							tmp = list(tp2[:-1])+list(tp[:-1])
							tmp.sort()
							tmp2 = list(tp2[-1])
							tmp2.append(diff)
							tmp2 = tuple(tmp2)

							# print("fnlllllllll:",tmp2)
							fnl = tuple(tmp+[tmp2])
							# print ("fnl  ",fnl)

							
							flag = False
							tmp = []
							# print("stepn : ",stepn)
							# print ("tmp bflop: ",tmp)
							for fn in stepn:
								# print("fn : ",fn)
								# tmp+=fn
								# if fn is not None:
								# 	flag = True
								for tn in fn:
									if tn is not None:
										if tn[:-1] not in tmp:
											tmp+=[tn[:-1]]
							# if not flag:
							# 	stepn[o].append(fnl)
							# 	unpaired[tp] = False
							
							# print ("tmp aflop: ",tmp)

							
								# print ("hello if condintional")
							flag = 0
							# print ("fnl ",fnl[:-1])
							# print("tmp ",tmp)
							if fnl[:-1] in tmp:
								flag = 1
							if flag == 0:
								# print("hello")
								stepn[o].append(fnl)
								unpaired[fnl] = True
							# if len(tmp)==0:
							# 	stepn[o].append(fnl)
							# 	unpaired[tp] = False
		step1 = stepn
		# print("stepn : ",stepn)
	prime_implicants = []
	for ky in unpaired.keys():
		if unpaired[ky]:
			prime_implicants.append(tuple(ky)) 
			# print (ky)
	return prime_implicants
# run(k = 4 , minterms = [0,1,2,5,7,8,9,10,13,15], dontcare = [])
prime_impl = run(k = 5,minterms = [13,15,17,18,19,20,21,23,25,27,29,31],dontcare = [1,12,2,24])
prime_impl.sort(key = lambda tpl: -len(tpl))
print(prime_impl)


# def extract_ess(prime_impl):
# 	tmp = []
# 	minterms = []
# 	for fl in prime_impl:
# 		tmp.append(tuple(fl[:-1]))
# 		minterms += fl[:-1]
# 	minterms.sort()
# 	table = {}
# 	ess = {}
# 	for tp in tmp:
# 		for i in minterms:
# 			if i in tp:
# 				table[(tp,i)] = 1
# 			else:
# 				table[(tp,i)] = 0
# 	# tmp = [()]+tmp
# 	track_back = {}
# 	mn = remove_one(tmp,minterms,track_back)
# 	# print("mn : ",mn)

# def remove_one(tpls,minterms,track_back):
# 	if len(minterms) == 0:
# 		min
# 		return 0
# 	if track_back.get(tuple(tpls)):
# 		tp = track_back[tuple(tpls)]
# 		mn = 999999999
# 		for t in list(tp):
# 			ttp = tpls[:]
# 			mnt = list(set(minterms) - set(t))
# 			ttp.remove(t)
# 			mn = min(1+remove_one(ttp,mnt,track_back),mn)
# 		return mn
# 	mn = 999999999
# 	for tp in tpls:
# 		tmp = tpls[:]
# 		mnprev = mn
# 		tmp.remove(tp)
# 		mnts = list(set(minterms) - set(tp))
# 		mn = min(remove_one(tmp,mnts,track_back)+1,mn)
# 		# print ("tp : " ,tpls)
# 		if mn != mnprev:
# 			if track_back.get(tuple(tpls)):
# 				track_back[tuple(tpls)] =  track_back.get(tuple(tpls)) |set([tp])
# 			else:
# 				track_back[tuple(tpls)] =  set([tp])
# 		if mn == remove_one(tmp,minterms,track_back)+1:
# 			if track_back.get(tuple(tpls)):
# 				track_back[tuple(tpls)] = track_back.get(tuple(tpls)) |set([tp])
# 			else:
# 				track_back[tuple(tpls)] = set([tp])
# 	return mn
# # extract_ess(prime_impl)



