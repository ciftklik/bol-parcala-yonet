import os
dosyaYolu='data.txt'

#İnteger float kontrolü
def isInt(x):
    if x%1 == 0:
        return False#tam bölünüyor
    else:
        return True


"""
Dosyayı belirtilen parcalara gore bir diziye aktarıyoruz.
Daha basitte yapılabilir.
ornek vermek gerekirse
0/100
101/200
201/300
"""
def boyutListHazirla(boyut,parca):
    bol=float(boyut)/float(parca)
    sayilar=[]
    print "toplam parca"+str(bol)
    print "toplam mb: "+str(boyut/1024*1024)
    for i in range(0,int(bol)):
        if i==0:
            j=i
        b=parca
        t=b*(i+1)
        s=str(j)+"/"+str(t)
        #print s
        sayilar.append(s)
        j=t+1
    if(isInt(bol)):
        isi=str(t+1)+"/"+str(boyut)
        #print isi
        sayilar.append(isi)

    return sayilar




boyut = os.path.getsize(dosyaYolu)
boyutlist=boyutListHazirla(boyut,50*1024*1024)
