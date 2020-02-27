import os
import copy, json
from ast import literal_eval

newguard = list()
with open("C:/Users/yvanm/Downloads/newsguard.csv", 'r') as f2:
    lies = f2.readlines()
    for i in lies:
        newguard.append(i.split(','))

finalNewguard = newguard[1:]
print("newsguard.csv ",finalNewguard)


with open("C:/Users/yvanm/Downloads/mediabiasfactchecksources.json", 'r') as f:
    lies = f.read()
dataJSON = json.loads(lies)
print("mediabiasfactcheckSources.json ", dataJSON)


listWeblink = list()
with open("C:/Users/yvanm/Downloads/data/data/NewsTrustData/NewstrustSources.tsv",'r')as f:
    rd = f.readlines()
    for i in rd:
        if 'web-link' in i:
            listWeblink.append(i[16:].strip('/\n'))
        elif 'Location' in i :
            listWeblink.append(i.strip('\n').strip('\t'))

    for element in listWeblink:
        print(element)

listRanking = list()
with open("C:/Users/yvanm/Downloads/data/data/NewsTrustData/NewstrustSources.tsv",'r')as g:
    rd = g.readlines()
    for i in rd:
        if 'overall-ratings' in i:
            listRanking.append(i.strip('overall-ratings\t').strip('\n'))

finalRatings = list()
for e in listRanking:
    finalRatings.append(literal_eval(e))

trustSources = list()
for f in zip(listWeblink,finalRatings):
    trustSources.append(f)
print("NewsTrustSources.tsv ",trustSources)


print(len(finalNewguard))
print(len(dataJSON))
print(len(trustSources))

semiFinal = list()
for ng in finalNewguard:
    for js in dataJSON:

            if ng[0] == js['source']:
                source_newgaurd = ng[0]
                score_newgaurd_Rating = eval(ng[1])/20
                #source_json = js['source']
                source_json_Rating = js['factualReporting']

                semiFinal.append((source_newgaurd, score_newgaurd_Rating, source_json_Rating))
                break




def extraitRating(array):
    if len(array) <= 0:
        return 0.0
    else:
        return array[-5]


listPrincipal = list()
for sf in semiFinal:
    for trust in trustSources:
        site,ratingNG,ratingJSON =sf
        siteTrust,ratingArrays =trust
        if site == siteTrust.strip('www.'):
            sourceFinal = site
            ratingFromNewGuard = ratingNG
            ratingFromJSON = ratingJSON
            ratingsFromTSV = extraitRating(ratingArrays)

            listPrincipal.append((sourceFinal, ratingFromNewGuard, ratingFromJSON,ratingsFromTSV  ))

            break

#comparison newsguard and newsTrust
newguard_newstrust = list()
for ng in finalNewguard:
    for nt in trustSources :
        sitetrust,ratingArrays = nt
        if ng[0] == sitetrust.strip('www.') :
           source_newgaurd = ng[0]
           score_newgaurd_Rating = eval(ng[1]) / 20
           ratingsFromTSV = extraitRating(ratingArrays)

           newguard_newstrust.append((source_newgaurd,score_newgaurd_Rating,ratingsFromTSV))
           break


#comparaison newstrust and mediabiaisfactcheck
new_array=[('source','rating JSON', 'rating TSV')]
for dt in dataJSON:
    for ts in trustSources:
        sitetrust,ratingArrays=ts

        if dt['source']==sitetrust.strip('www.'):
            source=dt['source']
            ratingFromJSON = dt['factualReporting']
            ratingFromtsv=extraitRating(ratingArrays)
            new_array.append((source, ratingFromtsv,ratingFromJSON ))

            break






print('\n')
print("comparison of all Sources")
print("-------------------------")
for element in listPrincipal:
   print(element)
print("Lenght: ",len(listPrincipal))
print("\n")

print("Comparison of mediabiasfactcheckSources and Newsguard ")
print("-----------------------------------------------------")
for hall in semiFinal:
    print(hall)
print(len(semiFinal))
print("\n")

print("Comparison of Newsguard and NewsTrustSource")
print("-------------------------------------------")
for hill in newguard_newstrust:
    print(hill)
print(len(newguard_newstrust))
print("\n")

print("Comparison of mediabiasfactcheckSources and NewsTrustSource ")
print("-----------------------------------------------------------")
for el in new_array:
    print(el)
print(len(new_array))

