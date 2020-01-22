from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.views.generic import TemplateView
from censuskenya.models import *
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from censuskenya import serializers as c_serial
from rest_framework import generics
from collections import Counter



def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
def Graphs(request):
	Gender = []
	labels = []
	Disab = []
	Dlabels = []
	HDeaths = []
	SDeaths = []
	Below5 = []
	HDivorce = []
	SDivorce = []
	HMarried = []
	MAgeDistribution = []
	FAgeDistribution = []
	# male
	M0_10 = []
	M11_20 = []
	M21_30 = []
	M31_40 = []
	M41_50 = []
	M51_60 = []
	M61_70 = []
	M71_80 = []
	M81_90 = []
	M91_100 = []
	# female
	F0_10 = []
	F11_20 = []
	F21_30 = []
	F31_40 = []
	F41_50 = []
	F51_60 = []
	F61_70 = []
	F71_80 = []
	F81_90 = []
	F91_100 = []
	heads = Head.objects.all()
	childs = Child.objects.all()
	spouses = Spouse.objects.all()


	# Age Distribution
	for ac in childs:
		if ac.sex == 'male' and ac.age <=10:
			M0_10.append(ac.name)
		elif ac.sex == 'female' and ac.age <=10:
			F0_10.append(ac.name)
		elif ac.sex == 'male' and ac.age <=20:
			M11_20.append(ac.name)
		elif ac.sex == 'female' and ac.age <=20:
			F11_20.append(ac.name)
		else:
			pass

	for ah,aw in zip(heads,spouses):
		if ah.sex == 'male' and ah.age <=30:
			M21_30.append(ah.name)
		elif ah.sex == 'female' and ah.age <=30:
			M21_30.append(ah.name)
		elif aw.sex == 'female' and aw.age <=30:
			F21_30.append(aw.name)
		elif aw.sex == 'male' and aw.age <=30:
			F21_30.append(aw.name)
		elif ah.sex == 'male' and ah.age <=40:
			M31_40.append(ah.name)
		elif ah.sex == 'female' and ah.age <=40:
			M31_40.append(ah.name)
		elif aw.sex == 'female' and aw.age <=40:
			F31_40.append(aw.name)
		elif aw.sex == 'male' and aw.age <=40:
			F31_40.append(aw.name)
		elif ah.sex == 'male' and ah.age <=50:
			M41_50.append(ah.name)
		elif ah.sex == 'female' and ah.age <=50:
			M41_50.append(ah.name)
		elif aw.sex == 'female' and aw.age <=50:
			F41_50.append(aw.name)
		elif aw.sex == 'male' and aw.age <=50:
			F41_50.append(aw.name)
		elif ah.sex == 'male' and ah.age <=60:
			M51_60.append(ah.name)
		elif ah.sex == 'female' and ah.age <=60:
			M51_60.append(ah.name)
		elif aw.sex == 'female' and aw.age <=60:
			F51_60.append(aw.name)
		elif aw.sex == 'male' and aw.age <=60:
			F51_60.append(aw.name)
		elif ah.sex == 'male' and ah.age <=70:
			M61_70.append(ah.name)
		elif ah.sex == 'female' and ah.age <=70:
			M61_70.append(ah.name)
		elif aw.sex == 'female' and aw.age <=70:
			F61_70.append(aw.name)
		elif aw.sex == 'male' and aw.age <=70:
			F61_70.append(aw.name)
		elif ah.sex == 'male' and ah.age <=80:
			M71_80.append(ah.name)
		elif ah.sex == 'female' and ah.age <=80:
			M71_80.append(ah.name)
		elif aw.sex == 'female' and aw.age <=80:
			F71_80.append(aw.name)
		elif aw.sex == 'male' and aw.age <=80:
			F71_80.append(aw.name)
		elif ah.sex == 'male' and ah.age <=90:
			M81_90.append(ah.name)
		elif ah.sex == 'female' and ah.age <=90:
			M81_90.append(ah.name)
		elif aw.sex == 'female' and aw.age <=90:
			F81_90.append(aw.name)
		elif aw.sex == 'male' and aw.age <=90:
			F81_90.append(aw.name)
		elif ah.sex == 'male' and ah.age <=100:
			M91_100.append(ah.name)
		elif ah.sex == 'female' and ah.age <=100:
			M91_100.append(ah.name)
		elif aw.sex == 'female' and aw.age <=100:
			F91_100.append(aw.name)
		elif aw.sex == 'male' and aw.age <=100:
			F91_100.append(aw.name)

	# Male
	M0 = len(M0_10)
	MAgeDistribution.append(-M0)
	M11 = len(M11_20)
	MAgeDistribution.append(-M11)
	M21 = len(M21_30)
	MAgeDistribution.append(-M21)
	M31 = len(M31_40)
	# print(M31)
	MAgeDistribution.append(-M31)
	M41 = len(M41_50)
	MAgeDistribution.append(-M41)
	M51 = len(M51_60)
	MAgeDistribution.append(-M51)
	M61 = len(M61_70)
	MAgeDistribution.append(-M61)
	M71 = len(M71_80)
	MAgeDistribution.append(-M71)
	M81 = len(M81_90)
	MAgeDistribution.append(-M81)
	M91 = len(M91_100)
	MAgeDistribution.append(-M91)

		# Female
	F0 = len(F0_10)
	FAgeDistribution.append(F0)
	F11 = len(F11_20)
	FAgeDistribution.append(F11)
	F21 = len(F21_30)
	FAgeDistribution.append(F21)
	F31 = len(F31_40)
	FAgeDistribution.append(F31)
	F41 = len(F41_50)
	FAgeDistribution.append(F41)
	F51 = len(F51_60)
	FAgeDistribution.append(F51)
	F61 = len(F61_70)
	FAgeDistribution.append(F61)
	F71 = len(F71_80)
	FAgeDistribution.append(F71)
	F81 = len(F81_90)
	FAgeDistribution.append(F81)
	F91 = len(F91_100)
	FAgeDistribution.append(F91)				

	# Head to Female
	
	for h in heads:
		if h.sex!='0':
			Gender.append(h.sex)
		HDeaths.append(h.death_stat)
		if h.mar_stat=='Divorced':
			HDivorce.append(h.mar_stat)
	for m in heads:
		if m.mar_stat=='Married monogomous' and 'Married Polygamous':
			HMarried.append(m.name)

	# Disability distribution
	for d in heads:
		if d.disab_stat=='yes':
			Disab.append(d.disability)
	disab_count = Counter(Disab)
	disaby = [disab_count[x] for x in disab_count]
	for dl in disab_count:
		Dlabels.append(dl)

	for cg in childs:
		if cg.sex!='0':
			Gender.append(cg.sex)
	
	for s in spouses:
		if s.sex!= '0':
			Gender.append(s.sex)
		SDeaths.append(s.death_stat)
		SDivorce.append(s.mar_stat)


	gender_count = Counter(Gender)
	gender_m = [gender_count[x] for x in gender_count]
	for l in gender_count:
		labels.append(l)
	for c in childs:
		if c.age<=5:
			Below5.append(c)
	Total_married = len(HMarried)
	Total_deaths = sum(HDeaths)
	Total_divorces = len(HDivorce)
	total_pop = len(heads)+len(childs)+len(spouses)
	Birthrate = len(Below5)/total_pop*1000
	Death_rate = Total_deaths/total_pop*1000
	Divorce_rate = Total_divorces/total_pop*100
	Marriage_rate = Total_married/total_pop*100
	Growth_rate = (((total_pop/900)**0.1)-1)*100

	
	return render(request,'graphs.html',
		{
			'gy':gender_m,
			'labels':labels,
			'dy':disaby,
			'disl':Dlabels,
			'Br':Birthrate,
			'Dr':Death_rate,
			'Dir':Divorce_rate,
			'Mr':Marriage_rate,
			'Gr':Growth_rate,
			'mag':MAgeDistribution,
			'fag':FAgeDistribution
		})
def Home(request):
	return render(request,'index.html')

class Headserial(generics.ListCreateAPIView):
	queryset = Head.objects.all()
	serializer_class = c_serial.HeadSerializer

class Spouseserial(generics.ListCreateAPIView):
	queryset = Spouse.objects.all()
	serializer_class = c_serial.SpouseSerializer

class Childserial(generics.ListCreateAPIView):
	queryset = Child.objects.all()
	serializer_class = c_serial.ChildSerializer

class Watukaserial(generics.ListCreateAPIView):
	queryset = Watuka.objects.all()
	serializer_class = c_serial.WatukaSerializer



def watuka(request):
	data = serialize('geojson', Watuka.objects.all())
	return HttpResponse(data, content_type='json')

def population(request):
	data = serialize('geojson', Population.objects.all())
	return HttpResponse(data, content_type='json')


def Spous(request):
	data = serialize('geojson', Spouse.objects.all())
	return HttpResponse(data, content_type='json')

def Heady(request):
	data = serialize('geojson', Head.objects.all())
	return HttpResponse(data, content_type='json')


def AnalyticalView(request):
	Gender = []
	labels = []
	heads = Head.objects.all()
	for h in heads:
		Gender.append(h.sex)

	gender_count = Counter(Gender)
	gender_m = [gender_count[x] for x in gender_count]
	for l in gender_count:
		labels.append(l)

	return JsonResponse({'gy':gender_m,'labels':labels})


	




