#python ile büyük dosyaları satır satır okuma işleme arama yapma
import os,time,re,sys,random,threading

#regex desenimiz
regex = r"[0-9]+"

dosyaYolu='data.txt'            
def oku(boyut):
    bas=boyut.split('/')[0]
    son=boyut.split('/')[1]
    f=open(dosyaYolu)
    f.seek(int(bas))
    lines=f.read(int(son)).splitlines()
    f.close()
    a=re.findall(regex,lines[0])
    if(str(a)!="[]"):
        print a
        raw_input('bulundu ...')
        

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
boyutlist=boyutListHazirla(boyut,50*1024*1024)#50 mb lik parcalar.

print len(boyutlist)

#ayni anda en fazla 5 islem yapiyor.
maxthreads = 5
for i in range(0,len(boyutlist)):
    while threading.activeCount() >= maxthreads:
        time.sleep(0.2)
        sys.stdout.write(str(i)+ " Bekliyor.\r")
        sys.stdout.flush()
    sys.stdout.write(str(i)+ " Araniyor.\r")
    sys.stdout.flush()
    threading.Thread(target = oku, args=(boyutlist[i])).start()
