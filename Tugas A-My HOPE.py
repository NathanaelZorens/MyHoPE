from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("My HoPE(Mind your Health of Psychological Emotion)")
root.geometry("1120x700")

class Person:
 global name
 name=StringVar()
 global Dep_Lvl
 Dep_Lvl=IntVar()
 global Mot_Lvl
 Mot_Lvl=IntVar()
 global Agr_Lvl
 Agr_Lvl=IntVar()
 global Pan_Lvl
 Pan_Lvl=IntVar()
  
 def setName(self,name): 
  self.name=name
 def getName(self):
  return self.name 
 def setDepLev(self,Dep_Lvl):
  self.Dep_Lvl=Dep_Lvl
 def getDepLev(self):
  return self.Dep_Lvl
 def setMotLev(self,Mot_Lvl):
  self.Mot_Lvl=Mot_Lvl
 def getMotLev(self):
  return self.Mot_Lvl
 def setAgrLev(self,Agr_Lvl):
  self.Agr_Lvl=Agr_Lvl
 def getAgrLev(self):
  return self.Agr_Lvl
 def setPanLev(self,Pan_Lvl):
  self.Pan_Lvl=Pan_Lvl
 def getPanLev(self):
  return self.Pan_Lvl


Data_fr=LabelFrame(root,padx=40,pady=40)
Data_fr.grid(row=1,column=0,padx=20,pady=20)
P1=Person()
Idtt=Toplevel()
Idtt.title("Nama")
Idtt.lift(root)
Idtt.geometry("200x100")
Name_E = Entry(Idtt, width=15)

def InNam():
 root.deiconify()
 n=Name_E.get() 
 P1.setName(n)
 Idtt.destroy()
Enter_B= Button(Idtt, width=10, text="Enter",command=InNam)
Expl_L= Label(Idtt,text="Masukkan nama Anda: ").pack() 
Name_E.pack(pady=10)
Enter_B.pack()

def DefaultVeliyu(self):
 self.setDepLev(0)
 self.setMotLev(0)
 self.setAgrLev(0)
 self.setPanLev(0)

def ShoData():
 Deita=Toplevel()
 Deita.title("Data")
 DataName_L=Label(Deita,text="Nama: "+P1.getName())
 DataDep=Label(Deita,text="Tingkat Depresi: "+str(P1.getDepLev()))
 DataMot=Label(Deita,text="Tingkat Harapan/Motivasi: "+str(P1.getMotLev()))
 DataAgr=Label(Deita,text="Tingkat Agresi: "+str(P1.getAgrLev()))
 DataPan=Label(Deita,text="Tingkat Kepanikan: "+str(P1.getPanLev()))
 
 DataName_L.grid(row=1,column=0)
 DataDep.grid(row=2,column=0)
 DataMot.grid(row=3,column=0)
 DataAgr.grid(row=4,column=0)
 DataPan.grid(row=5,column=0)
 
 def ResetAll(self):
  DefaultVeliyu(self)
  Deita.destroy()
  Q1_Dep.rbc.set(0);Q2_Dep.rbc.set(0);Q3_Dep.rbc.set(0);Q4_Dep.rbc.set(0);Q5_Dep.rbc.set(0)
  Q6_Dep.rbc.set(0);Q7_Dep.rbc.set(0);Q8_Dep.rbc.set(0);Q9_Dep.rbc.set(0)
  Q1_Mot.rbc.set(0);Q2_Mot.rbc.set(0);Q3_Mot.rbc.set(0);Q4_Mot.rbc.set(0)
  Q5_Mot.rbc.set(0);Q6_Mot.rbc.set(0);Q7_Mot.rbc.set(0);Q8_Mot.rbc.set(0)
  Q1_Agr.dmc.set("No."+str(1));Q2_Agr.dmc.set("No."+str(2));Q3_Agr.dmc.set("No."+str(3));Q4_Agr.dmc.set("No."+str(4));Q5_Agr.dmc.set("No."+str(5))
  Q6_Agr.dmc.set("No."+str(6));Q7_Agr.dmc.set("No."+str(7));Q8_Agr.dmc.set("No."+str(8));Q9_Agr.dmc.set("No."+str(9));Q10_Agr.dmc.set("No."+str(10))
  Q11_Agr.dmc.set("No."+str(11));Q12_Agr.dmc.set("No."+str(12));Q13_Agr.dmc.set("No."+str(13));Q14_Agr.dmc.set("No."+str(14));Q15_Agr.dmc.set("No."+str(15))
  Q16_Agr.dmc.set("No."+str(16));Q17_Agr.dmc.set("No."+str(17));Q18_Agr.dmc.set("No."+str(18));Q19_Agr.dmc.set("No."+str(19));Q20_Agr.dmc.set("No."+str(20))
  Q1_Pan.rbc.set(0);Q2_Pan.rbc.set(0);Q3_Pan.rbc.set(0);Q4_Pan.rbc.set(0);Q5_Pan.rbc.set(0)
  Q6_Pan.rbc.set(0);Q7_Pan.rbc.set(0);Q8_Pan.rbc.set(0);Q9_Pan.rbc.set(0);Q10_Pan.rbc.set(0)
 
 Ok_B=Button(Deita,text="OK",command=Deita.destroy).grid(row=6,column=0)
 Res_B=Button(Deita,text="Reset",command=lambda: ResetAll(P1)).grid(row=6,column=1)
 DepWarn=Label(Deita, text="(!)",fg="red")
 MotWarn=Label(Deita, text="(!)",fg="red")
 AgrWarn=Label(Deita, text="(!)",fg="red")
 PanWarn=Label(Deita, text="(!)",fg="red")
 if(P1.getDepLev()>17): 
   DepWarn.grid(row=2,column=1,columnspan=2) 
 if(0<P1.getMotLev()<17):
   MotWarn.grid(row=3,column=1,columnspan=2) 
 if(P1.getAgrLev()>64):
  AgrWarn.grid(row=4,column=1,columnspan=2)   
 if(P1.getPanLev()>27):
  PanWarn.grid(row=5,column=1,columnspan=2) 
 
DataShow_B= Button(Data_fr, width=10, text="Data Anda",command=ShoData).grid(row=0,column=0) 
 
#==============================
DefaultVeliyu(P1)
Qlist_fr=LabelFrame(root,padx=40,pady=40)
Qlist_fr.grid(row=0,column=0,padx=20,pady=20)

global QAgr_fr
global QDep_fr
global QMot_fr
global QPan_fr

Qch=StringVar()
QDep_fr=LabelFrame(root,padx=30,pady=5,text="Depression",fg="darkblue",bd=5)
QMot_fr=LabelFrame(root,padx=30,pady=5,text="Hope&Motivation",fg="green",bd=5)
QAgr_fr=LabelFrame(root,padx=30,pady=5,text="Agression",fg="orange",bd=5)
QPan_fr=LabelFrame(root,padx=30,pady=5,text="Panic Attack",fg="purple",bd=5)

def QChoice(cho):
 Dx=QDep_fr.winfo_exists()
 Mx=QMot_fr.winfo_exists()
 Ax=QAgr_fr.winfo_exists()
 Px=QPan_fr.winfo_exists()

 if(cho=="Depresi"):
  QDep_fr.grid(row=0,column=1,padx=20,pady=10,rowspan=7)
  
  if(Mx==1):
   QMot_fr.grid_forget()
  if(Ax==1):
   QAgr_fr.grid_forget()
  if(Px==1):
   QPan_fr.grid_forget()  
 elif(cho=="Motivasi"): 
  QMot_fr.grid(row=0,column=1,padx=20,pady=10,rowspan=7)
  
  if(Dx==1):
   QDep_fr.grid_forget()
  if(Ax==1):
   QAgr_fr.grid_forget()
  if(Px==1):
   QPan_fr.grid_forget()
 elif(cho=="Agresi"):
  QAgr_fr.grid(row=0,column=1,padx=20,pady=10,rowspan=7)
  
  if(Dx==1):
   QDep_fr.grid_forget()
  if(Mx==1):
   QMot_fr.grid_forget()
  if(Px==1):
   QPan_fr.grid_forget() 
 elif(cho=="Panik"): 
  QPan_fr.grid(row=0,column=1,padx=20,pady=10,rowspan=7)
  
  if(Dx==1):
   QDep_fr.grid_forget()
  if(Mx==1):
   QMot_fr.grid_forget()
  if(Ax==1):
   QAgr_fr.grid_forget()
 else:
  return
    
Qlist_DdM=OptionMenu(Qlist_fr, Qch,"Depresi","Motivasi","Agresi","Panik",command=QChoice)
Qlist_L=Label(Qlist_fr,text="Silahkan pilih tes:").grid(row=0,column=0)
Qlist_DdM.grid(row=1,column=0)
Qch.set("Pilih")

#Depression Questionaire ========= Depression =========== Depression ===========

class DepSet:
 global rbc
 rbc=IntVar()
 
 def __init__(self,r):
     self.rbc=IntVar()
     global A_Dep
     global B_Dep
     global C_Dep
     global D_Dep
     A_Dep=Radiobutton(QDep_fr,text="Tidak sama sekali",variable=self.rbc,value=0,padx=10)
     B_Dep=Radiobutton(QDep_fr,text="Beberapa hari",variable=self.rbc,value=1,padx=10)
     C_Dep=Radiobutton(QDep_fr,text="Lebih dari 3/4 hari",variable=self.rbc,value=2,padx=10)
     D_Dep=Radiobutton(QDep_fr,text="Hampir setiap hari",variable=self.rbc,value=3,padx=10)
     A_Dep.grid(row=r,column=0)
     B_Dep.grid(row=r,column=1)
     C_Dep.grid(row=r,column=2)
     D_Dep.grid(row=r,column=3)
     self.rbc.set(0)

  
ExDep_L=Label(QDep_fr,text="Jawab dengan apa yang anda rasakan selama Seminggu ini.",padx=0,justify=LEFT).grid(row=0,column=0,columnspan=3,sticky=W)
Q1Dep_L=Label(QDep_fr,text="1.Sedikit ketertarikan atau menikmati hal yang dilakukan",padx=0,justify=LEFT).grid(row=1,column=0,columnspan=3,sticky=W)
Q1_Dep=DepSet(2)
Q2Dep_L=Label(QDep_fr,text="2.Merasa Sedih, Depresi, atau Tidak punya harapan",padx=0,justify=LEFT).grid(row=3,column=0,columnspan=3,sticky=W)
Q2_Dep=DepSet(4)
Q3Dep_L=Label(QDep_fr,text="3.Kesulitan tidur atau tidur terlalu banyak",padx=0,justify=LEFT).grid(row=5,column=0,columnspan=3,sticky=W)
Q3_Dep=DepSet(6)
Q4Dep_L=Label(QDep_fr,text="4.Merasa Letih atau Tidak punya tenaga",padx=0,justify=LEFT).grid(row=7,column=0,columnspan=3,sticky=W)
Q4_Dep=DepSet(8)
Q5Dep_L=Label(QDep_fr,text="5.Tidak nafsu makan atau makan terlalu banyak",padx=0,justify=LEFT).grid(row=9,column=0,columnspan=3,sticky=W)
Q5_Dep=DepSet(10)
Q6Dep_L=Label(QDep_fr,text="6.Merasa bersalah terhadap diri sendiri,atau merasa gagal atau merasa telah mengecewakan orang lain",padx=0,justify=LEFT).grid(row=11,column=0,columnspan=6,sticky=W)
Q6_Dep=DepSet(12)
Q7Dep_L=Label(QDep_fr,text="7.Kesulitan berkonsentrasi, misalnya saat membaca atau menonton sesuatu",padx=0,justify=LEFT).grid(row=13,column=0,columnspan=3,sticky=W)
Q7_Dep=DepSet(14)
Q8Dep_L=Label(QDep_fr,text="8.Bergerak atau berbicara sangat pelan, atau bahkan bergerak atau berbicara sangat cepat dan terburu-buru",padx=0,justify=LEFT).grid(row=15,column=0,columnspan=6,sticky=W)
Q8_Dep=DepSet(16)
Q9Dep_L=Label(QDep_fr,text="9.Berpikir lebih baik mati atau melukai diri sendiri",padx=0,justify=LEFT).grid(row=17,column=0,columnspan=3,sticky=W)
Q9_Dep=DepSet(18)

YoAns_Dep=[]
def EnDep():
 YoAns_Dep.clear()
 YoAns_Dep.append(Q1_Dep.rbc.get())
 YoAns_Dep.append(Q2_Dep.rbc.get())
 YoAns_Dep.append(Q3_Dep.rbc.get())
 YoAns_Dep.append(Q4_Dep.rbc.get())
 YoAns_Dep.append(Q5_Dep.rbc.get())
 YoAns_Dep.append(Q6_Dep.rbc.get())
 YoAns_Dep.append(Q7_Dep.rbc.get())
 YoAns_Dep.append(Q8_Dep.rbc.get())
 YoAns_Dep.append(Q9_Dep.rbc.get())
 ag=0
 l=0
 for ag in range(len(YoAns_Dep)):
  l=l+YoAns_Dep[ag]  
 ag+=1
 P1.setDepLev(l)

 messagebox.showinfo("Tingkat Depresi", "Nilai Tingkat Depresi anda "+str(P1.getDepLev())+"/27")
 
EnterDep_B=Button(QDep_fr,text="Submit",command=EnDep).grid(row=20,column=6)

#Depression Questionaire ========= Depression =========== Depression ===========

#Motivation Questionaire ========= Motivation =========== Motivation ===========
class MotSet: 
 global rbc
 rbc=IntVar()


 def __init__(self,r):
     self.rbc=IntVar()
     global A_Mot
     global B_Mot
     global C_Mot
     global D_Mot
     A_Mot=Radiobutton(QMot_fr,text="Sangat Salah",variable=self.rbc,value=1,padx=10)
     B_Mot=Radiobutton(QMot_fr,text="Lumayan Salah",variable=self.rbc,value=2,padx=10)
     C_Mot=Radiobutton(QMot_fr,text="Lumayan Benar",variable=self.rbc,value=3,padx=10)
     D_Mot=Radiobutton(QMot_fr,text="Sangat Benar",variable=self.rbc,value=4,padx=10)
     A_Mot.grid(row=r,column=0)
     B_Mot.grid(row=r,column=1)
     C_Mot.grid(row=r,column=2)
     D_Mot.grid(row=r,column=3)
     self.rbc.set(1)
     
  
ExMot_L=Label(QMot_fr,text="Jawab dengan apa yang anda rasakan selama Seminggu ini.",padx=0,justify=LEFT).grid(row=0,column=0,columnspan=3,sticky=W)
Q1Mot_L=Label(QMot_fr,text="1.Saya mengejar tujuan/target saya dengan semangat",padx=0,justify=LEFT).grid(row=1,column=0,columnspan=3,sticky=W)
Q1_Mot=MotSet(2)
Q2Mot_L=Label(QMot_fr,text="2.Saya dapat memikirkan banyak cara untuk melepaskan diri dari hambatan",padx=0,justify=LEFT).grid(row=3,column=0,columnspan=3,sticky=W)
Q2_Mot=MotSet(4)
Q3Mot_L=Label(QMot_fr,text="3.Masa lalu saya mempersiapkan saya untuk masa depan",padx=0,justify=LEFT).grid(row=5,column=0,columnspan=3,sticky=W)
Q3_Mot=MotSet(6)
Q4Mot_L=Label(QMot_fr,text="4.Ada banyak cara mengatasi suatu masalah",padx=0,justify=LEFT).grid(row=7,column=0,columnspan=3,sticky=W)
Q4_Mot=MotSet(8)
Q5Mot_L=Label(QMot_fr,text="5.Saya cukup berhasil belakangan ini",padx=0,justify=LEFT).grid(row=9,column=0,columnspan=3,sticky=W)
Q5_Mot=MotSet(10)
Q6Mot_L=Label(QMot_fr,text="6.Saya dapat memikirkan banyak cara untuk mendapatkan hal yang penting bagi saya",padx=0,justify=LEFT).grid(row=11,column=0,columnspan=6,sticky=W)
Q6_Mot=MotSet(12)
Q7Mot_L=Label(QMot_fr,text="7.Saya mencapai tujuan yang telah saya targetkan",padx=0,justify=LEFT).grid(row=13,column=0,columnspan=3,sticky=W)
Q7_Mot=MotSet(14)
Q8Mot_L=Label(QMot_fr,text="8.Walaupun saya patah semangat, saya dapat mencari solusi untuk menyelesaikan masalah",padx=0,justify=LEFT).grid(row=15,column=0,columnspan=6,sticky=W)
Q8_Mot=MotSet(16)

YoAns_Mot=[]
def EnMot():
 YoAns_Mot.clear()
 YoAns_Mot.append(Q1_Mot.rbc.get())
 YoAns_Mot.append(Q2_Mot.rbc.get())
 YoAns_Mot.append(Q3_Mot.rbc.get())
 YoAns_Mot.append(Q4_Mot.rbc.get())
 YoAns_Mot.append(Q5_Mot.rbc.get())
 YoAns_Mot.append(Q6_Mot.rbc.get())
 YoAns_Mot.append(Q7_Mot.rbc.get())
 YoAns_Mot.append(Q8_Mot.rbc.get())
 ag=0
 l=0
 for ag in range(len(YoAns_Mot)):
  l=l+YoAns_Mot[ag]  
 ag+=1
 P1.setMotLev(l)

 messagebox.showinfo("Tingkat Harapan", "Nilai Tingkat Harapan dan Motivasi anda "+str(P1.getMotLev())+"/32")
 
EnterMot_B=Button(QMot_fr,text="Submit",command=EnMot).grid(row=20,column=6)

#Motivation Questionaire ========= Motivation =========== Motivation ===========

#Agression Questionaire =========== Agression ============= Agression ============
class AgrSet: 
 global dmc
 dmc=StringVar()

 Choice_Agr=["Sangat bukan saya","Bukan sepenuhnya saya","Netral","Cukup mencerminkan saya","Sangat mencerminkan saya"]   
 def __init__(self,r):
     self.dmc=StringVar()
     self.ch=IntVar()
     Opt_Agr=OptionMenu(QAgr_fr, self.dmc, *AgrSet.Choice_Agr)
     Opt_Agr.grid(row=r,column=7,columnspan=6,sticky=W,pady=0)
     self.dmc.set("No."+str(r)) 

ExAgr_L=Label(QAgr_fr,text="Jawab dengan apa yang anda rasakan selama Sebulan ini.",padx=0,pady=0,justify=LEFT).grid(row=0,column=0,columnspan=3,sticky=W)     
Q1Agr_L=Label(QAgr_fr,text="1.Beberapa teman saya berpikir bahwa saya pemarah/suka mengkritik",padx=0,justify=LEFT).grid(row=1,column=0,columnspan=6,sticky=W)     
Q1_Agr=AgrSet(1)
Q2Agr_L=Label(QAgr_fr,text="2.Jika saya harus menggunakan kekerasan untuk melindungi hak saya, akan saya lakukan",padx=0,justify=LEFT).grid(row=2,column=0,columnspan=6,sticky=W)     
Q2_Agr=AgrSet(2)
Q3Agr_L=Label(QAgr_fr,text="3.Saat orang lain baik terhadap saya, saya mencurigai niat mereka",padx=0,justify=LEFT).grid(row=3,column=0,columnspan=6,sticky=W)     
Q3_Agr=AgrSet(3)
Q4Agr_L=Label(QAgr_fr,text="4. Saya secara terbuka bilang ke teman-teman saya, jika saya tidak setuju dengan mereka",padx=0,justify=LEFT).grid(row=4,column=0,columnspan=6,sticky=W)     
Q4_Agr=AgrSet(4)
Q5Agr_L=Label(QAgr_fr,text="5. Saya pernah marah sampai merusak suatu barang",padx=0,justify=LEFT).grid(row=5,column=0,columnspan=6,sticky=W)     
Q5_Agr=AgrSet(5)
Q6Agr_L=Label(QAgr_fr,text="6. Saya seringkali berdebat dengan orang yang tidak setuju dengan saya",padx=0,justify=LEFT).grid(row=6,column=0,columnspan=6,sticky=W)     
Q6_Agr=AgrSet(6)
Q7Agr_L=Label(QAgr_fr,text="7. Saya heran kenapa bisa sebal terhadap beberapa hal",padx=0,justify=LEFT).grid(row=7,column=0,columnspan=6,sticky=W)     
Q7_Agr=AgrSet(7)
Q8Agr_L=Label(QAgr_fr,text="8. Sesekali saya tidak bisa mengendalikan diri sampai dapat melukai orang lain",padx=0,justify=LEFT).grid(row=8,column=0,columnspan=6,sticky=W)     
Q8_Agr=AgrSet(8)
Q9Agr_L=Label(QAgr_fr,text="9. Saya memiliki temper yang buruk",padx=0,justify=LEFT).grid(row=9,column=0,columnspan=6,sticky=W)     
Q9_Agr=AgrSet(9)
Q11Agr_L=Label(QAgr_fr,text="11.Saya pernah mengancam orang yang saya kenal",padx=0,justify=LEFT).grid(row=10,column=0,columnspan=6,sticky=W)     
Q10_Agr=AgrSet(10)
Q11Agr_L=Label(QAgr_fr,text="12.Saya mudah marah, tetapi juga mudah padam",padx=0,justify=LEFT).grid(row=11,column=0,columnspan=6,sticky=W)     
Q11_Agr=AgrSet(11)
Q12Agr_L=Label(QAgr_fr,text="13.Saat diprovokasi sampai ke batas, saya dapat memukul orang lain",padx=0,justify=LEFT).grid(row=12,column=0,columnspan=6,sticky=W)     
Q12_Agr=AgrSet(12)
Q13Agr_L=Label(QAgr_fr,text="14.Saat saya tergangggu oleh seseorang, saya mengatakan apa yang saya rasakan kepada mereka",padx=0,justify=LEFT).grid(row=13,column=0,columnspan=6,sticky=W)     
Q13_Agr=AgrSet(13)
Q14Agr_L=Label(QAgr_fr,text="17.Saya kesulitan mengendalikan emosi",padx=0,justify=LEFT).grid(row=14,column=0,columnspan=6,sticky=W)     
Q14_Agr=AgrSet(14)
Q15Agr_L=Label(QAgr_fr,text="18.Saat Frustrasi, saya menunjukkannya ke luar",padx=0,justify=LEFT).grid(row=15,column=0,columnspan=6,sticky=W)     
Q15_Agr=AgrSet(15)
Q16Agr_L=Label(QAgr_fr,text="19.Terkadang, saya merasa/saya tahu bahwa orang lain membicarakan saya dari belakang",padx=0,justify=LEFT).grid(row=16,column=0,columnspan=6,sticky=W)     
Q16_Agr=AgrSet(16)
Q17Agr_L=Label(QAgr_fr,text="21.Jika seseorang menyerang saya, saya menyerang balik",padx=0,justify=LEFT).grid(row=17,column=0,columnspan=6,sticky=W)     
Q17_Agr=AgrSet(17)
Q18Agr_L=Label(QAgr_fr,text="22.Ada orang-orang yang menekan saya sehingga kami berselisih",padx=0,justify=LEFT).grid(row=18,column=0,columnspan=6,sticky=W)     
Q18_Agr=AgrSet(18)
Q19Agr_L=Label(QAgr_fr,text="24.Terkadang saya lepas kendali tanpa alasan tertentu",padx=0,justify=LEFT).grid(row=19,column=0,columnspan=6,sticky=W)     
Q19_Agr=AgrSet(19)
Q20Agr_L=Label(QAgr_fr,text="25.Saya sering terlibat perkelahian/konflik dibandingkan dengan orang pada biasanya",padx=0,justify=LEFT).grid(row=20,column=0,columnspan=6,sticky=W)     
Q20_Agr=AgrSet(20)

global YoAns_Agr
YoAns_Agr=[]
global TotAns_Agr
TotAns_Agr=[]    
def EnAgr():
    YoAns_Agr.clear()
    TotAns_Agr.clear()
    YoAns_Agr.append(Q1_Agr.dmc.get())
    YoAns_Agr.append(Q2_Agr.dmc.get())
    YoAns_Agr.append(Q3_Agr.dmc.get())
    YoAns_Agr.append(Q4_Agr.dmc.get())
    YoAns_Agr.append(Q5_Agr.dmc.get())
    YoAns_Agr.append(Q6_Agr.dmc.get())
    YoAns_Agr.append(Q7_Agr.dmc.get())
    YoAns_Agr.append(Q8_Agr.dmc.get())
    YoAns_Agr.append(Q9_Agr.dmc.get())
    YoAns_Agr.append(Q10_Agr.dmc.get())
    YoAns_Agr.append(Q11_Agr.dmc.get())
    YoAns_Agr.append(Q12_Agr.dmc.get())
    YoAns_Agr.append(Q13_Agr.dmc.get())
    YoAns_Agr.append(Q14_Agr.dmc.get())
    YoAns_Agr.append(Q15_Agr.dmc.get())
    YoAns_Agr.append(Q16_Agr.dmc.get())
    YoAns_Agr.append(Q17_Agr.dmc.get())
    YoAns_Agr.append(Q18_Agr.dmc.get())
    YoAns_Agr.append(Q19_Agr.dmc.get())
    YoAns_Agr.append(Q20_Agr.dmc.get())
    ag=0
    sm=0
    l=0
    for ag in range(len(YoAns_Agr)):
      l=sm+ag
      d=YoAns_Agr[l]
      if (d==AgrSet.Choice_Agr[0]):
        TotAns_Agr.append(1)
      elif (d==AgrSet.Choice_Agr[1]):
        TotAns_Agr.append(2)  
      elif (d==AgrSet.Choice_Agr[2]):
        TotAns_Agr.append(3)  
      elif (d==AgrSet.Choice_Agr[3]):
        TotAns_Agr.append(4)  
      elif (d==AgrSet.Choice_Agr[4]):
        TotAns_Agr.append(5)        
    ag+=1
    
    lg=0
    a=0
    for lg in range(len(TotAns_Agr)):
     a=a+TotAns_Agr[lg]  
    lg+=1
    P1.setAgrLev(a)
    messagebox.showinfo("Tingkat Agresi", "Nilai Tingkat Agresi anda "+str(P1.getAgrLev())+"/100")

EnterAgr_B=Button(QAgr_fr,text="Submit",command=EnAgr,justify=RIGHT).grid(row=20,column=16,sticky=NE,padx=30)

#Agression Questionaire =========== Agression ============= Agression ============

#Panic Questionaire =========== Panic ============ Panic ====================
class PanSet:
 global rbc
 rbc=IntVar()
 
 def __init__(self,r):
     self.rbc=IntVar()
     global A_Pan
     global B_Pan
     global C_Pan
     global D_Pan
     A_Pan=Radiobutton(QPan_fr,text="Tidak pernah",variable=self.rbc,value=0,padx=10)
     B_Pan=Radiobutton(QPan_fr,text="Terkadang",variable=self.rbc,value=1,padx=10)
     C_Pan=Radiobutton(QPan_fr,text="Lumayan",variable=self.rbc,value=2,padx=10)
     D_Pan=Radiobutton(QPan_fr,text="Sering",variable=self.rbc,value=3,padx=10)
     E_Pan=Radiobutton(QPan_fr,text="Setiap waktu",variable=self.rbc,value=4,padx=10)
     A_Pan.grid(row=r,column=0)
     B_Pan.grid(row=r,column=1)
     C_Pan.grid(row=r,column=2)
     D_Pan.grid(row=r,column=3)
     E_Pan.grid(row=r,column=4)

ExPan_L=Label(QPan_fr,text="Jawab dengan apa yang anda rasakan selama Seminggu ini.",padx=0,justify=LEFT).grid(row=0,column=0,columnspan=3,sticky=W)
Q1Pan_L=Label(QPan_fr,text="1.Merasakan suatu ketakutan atau kengerian secara tiba-tiba tanpa sebab",padx=0,justify=LEFT).grid(row=1,column=0,columnspan=6,sticky=W)
Q1_Pan=PanSet(2)
Q2Pan_L=Label(QPan_fr,text="2.Merasa Tidak yakin, khawatir, atau gugup soal mengalami Kepanikan lebih banyak lagi",padx=0,justify=LEFT).grid(row=3,column=0,columnspan=6,sticky=W)
Q2_Pan=PanSet(4)
Q3Pan_L=Label(QPan_fr,text="3.Berpikiran tentang lepas kendali diri, meninggal, menjadi gila, atau hal buruk lain karena Panik Mendadak",padx=0,justify=LEFT).grid(row=5,column=0,columnspan=6,sticky=W)
Q3_Pan=PanSet(6)
Q4Pan_L=Label(QPan_fr,text="4.Merasakan detak jantung yang cepat, berkeringat, sulit bernafas, pingsan, atau gemetar",padx=0,justify=LEFT).grid(row=7,column=0,columnspan=6,sticky=W)
Q4_Pan=PanSet(8)
Q5Pan_L=Label(QPan_fr,text="5.Merasa Otot Tegang, terasa terpojok atau terburu-buru, atau kesulitan rileks atau kesulitan tidur",padx=0,justify=LEFT).grid(row=9,column=0,columnspan=6,sticky=W)
Q5_Pan=PanSet(10)
Q6Pan_L=Label(QPan_fr,text="6.Menghindari situasi yang dapat menyebabkan Panik Mendadak",padx=0,justify=LEFT).grid(row=11,column=0,columnspan=6,sticky=W)
Q6_Pan=PanSet(12)
Q7Pan_L=Label(QPan_fr,text="7.Meninggalkan suatu situasi lebih awal atau berpartisipasi secara minimal, karena panik",padx=0,justify=LEFT).grid(row=13,column=0,columnspan=6,sticky=W)
Q7_Pan=PanSet(14)
Q8Pan_L=Label(QPan_fr,text="8.Menghabiskan banyak waktu atau menunda-nunda dalam mempersiapkan suatu situasi yang mungkin terjadi Panik Mendadak.",padx=0,justify=LEFT).grid(row=15,column=0,columnspan=6,sticky=W)
Q8_Pan=PanSet(16)
Q9Pan_L=Label(QPan_fr,text="9.Mengalihkan perhatian diri untuk mengindari pemikiran yang membuat panik",padx=0,justify=LEFT).grid(row=17,column=0,columnspan=6,sticky=W)
Q9_Pan=PanSet(18)
Q10Pan_L=Label(QPan_fr,text="10.Membutuhkan suatu bantuan untuk mengatasi Kepanikan (misal: Alkohol, Narkotika, benda keramat, orang lain,dsb.)",padx=0,justify=LEFT).grid(row=19,column=0,columnspan=6,sticky=W)
Q10_Pan=PanSet(20)

YoAns_Pan=[]
def EnPan():
 YoAns_Pan.clear()
 YoAns_Pan.append(Q1_Pan.rbc.get())
 YoAns_Pan.append(Q2_Pan.rbc.get())
 YoAns_Pan.append(Q3_Pan.rbc.get())
 YoAns_Pan.append(Q4_Pan.rbc.get())
 YoAns_Pan.append(Q5_Pan.rbc.get())
 YoAns_Pan.append(Q6_Pan.rbc.get())
 YoAns_Pan.append(Q7_Pan.rbc.get())
 YoAns_Pan.append(Q8_Pan.rbc.get())
 YoAns_Pan.append(Q9_Pan.rbc.get())
 YoAns_Pan.append(Q10_Pan.rbc.get())
 ag=0
 l=0
 for ag in range(len(YoAns_Pan)):
  l=l+YoAns_Pan[ag]  
 ag+=1
 P1.setPanLev(l)
 messagebox.showinfo("Tingkat Panik", "Nilai Tingkat Kepanikan anda "+str(P1.getPanLev())+"/40")
 
EnterPan_B=Button(QPan_fr,text="Submit",command=EnPan).grid(row=20,column=6)

#Panic Questionaire =========== Panic ============ Panic ====================

root.mainloop()