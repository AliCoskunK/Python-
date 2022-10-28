print("AKVARYUM HOBİSİ BAŞLANGIÇ REHBERİNE HOŞGELDİN")

print("Öncelikle akvaryum hacmini hesaplamamız gerekiyor" )

genislik=input("Akvaryum genişliğini giriniz (cm) :")
derinlik=input("Akvaryum derinliğini giriniz (cm) :")
uzunluk=input("Akvaryum uzunluğunu giriniz (cm) :")

hacim=int(genislik)*int(derinlik)*int(uzunluk)/1000
print("Akvaryumun Litresi : :",hacim)
print("Hacim hesaplamasından sonra çıkan sorulara evet yada hayır olarak cevap verebilirsin")



if hacim>400:
  print("Uyumluluk tablosunu ve balık başına düşen 25 litrelik su hacmini dikkate alarak istediğiniz balığı besleyebilirsiniz") 
  
elif 0<hacim<100:
  print("Bu hacimle canlı doğuran,tetra(tetralar sürü balıklarıdır 6 lı veya 10 lu beraber beslenmelidir aksi taktirde öleceklerdir)ciklet familyasından balıklar besleyebilirsiniz.Uyarı:FANUSTA BALIK BESLENMEZ!!")



else:
  100<hacim<200
  print("Ortalama bir su hacmine sahipsiniz çoğu Discus,Arowana ırkı gbi büyük balıklar dışında,Tetra,Guppy,Ciklet ırklarına uygun bir akvaryuma sahipsiniz")
  
dahası=input("Akvaryum hakkında daha fazla bilgi almak ister misin?")


if dahası==("evet"):
  
  print("Akvaryum 1853 yılında Londra dan hayatımıza giriş yapmıştır,hobinin amacı evimizde doğadan bir ferahlık penceresi açmaktır ve mümkün olduğunda doğanın eve yansıtılmasını sağlamaktır yani renkli kumlar plastik bitkiler,fanusta balık beslemek akvaryum hobisine ait değildir")


elif dahası!=("evet")or("hayır"):
  print("Lütfen soruları evet yada hayır olarak cevaplayınız")

else:
  dahası==("hayır")
  
  
  print("TAMAM")




dahası2=input("Uzman sayılabileceğim bitkili akvaryumlar konusundada bilgi almak ister misin? ")

if dahası2==("evet"):
  
  print("Bitkili akvaryumlarda en önemli nokta kurulum aşamasında seçilen kum ve aydınlatmadır bitkili akvaryumlar diğer akvaryumlara göre biraz daha emek isteyen ama manzara olarakta diğerlerinden çok önde olan bir alandır.Bitkilerin rasgele ekilmemesi,belli aralıklarla budanması,gübrelenmesi ve aydınlatma süresinin doğru ayarlanıp bitkilerin yosun riski engellenmelidir.Ayrıca akvaryumdaki balıkların fazla yemlenmemesi yemlenirsede salyangoz,vatoz,yada karides ırklarıyla fazla yem tüketilip bakteri çakışması engellenmelidir ")

elif dahası2!=("evet")or("hayır"):
  print("Lütfen soruları evet yada hayır olarak cevaplayınız")





else:
  dahası2==("hayır")
  
  print("TAMAM")


hap=input("Akvaryum konusunda akılda kalıcı hap bilgiler vermek istiyorum tabi sende istersen?")


if hap==("evet"):
 
  print("Takashi Amano akvaryum hobisine çok büyük katkılarıyla bilinen japon akvarist,yazar ve fotoğrafçıdır.Amano karidesi kendisi keşfetmiş ve soy ismini vermiştir ayrıca akvaryumlarda fazla aydınlatma ve nitrat seviyelerinin yükselmesiyle ortaya çıkan,bitkilerin ölümüne sebep olan sakal yosununu %99 oranında ortadan kaldıran tek canlı Amano karidestir")

elif hap!=("evet")or("hayır"):
  print("Lütfen soruları evet yada hayır olarak cevaplayınız")


else :
  hap==("hayır")
  print( "TAMAM")

  hap2=input("Bir tane daha hap bilgi ister misin?")


  if hap2==("evet"):
    print("Dünyanın belli bölgelerinde stresli meslek gruplarına günde belirli bir süre zorunlu akvaryum izletilir bunun sebebi akvaryumun ve su sesinin insan zihnini dinginleştirme ve rahatlatma etkisidir")

  elif hap2!=("evet")or("hayır"):
    print("Lütfen soruları evet yada hayır olarak cevaplayınız")
 

  else:
    hap2==("hayır")
    print("Abi senin hayır demeyeceğine eminim ama her ihtimale karşı hayır içinde bir koşul kodu yazdım")
    











  
 

