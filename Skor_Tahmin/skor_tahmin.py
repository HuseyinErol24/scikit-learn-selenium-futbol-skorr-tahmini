from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


class  SkorTahmin():
    def __init__(self):
        self.ev_Sahibi = []
        self.deplasman = []
        self.tarayici = webdriver.Firefox()
        self.tarayici.get("https://istatistik.nesine.com/1409407/son-maclari") # => Analiz edilecek maçın istatisitikler sayfasının linkini giriniz 
        time.sleep(5)
        self.tablo_1()
        self.tablo_2()
        self.tarayici.close()
        self.ev_sahibi_Skor = []
        self.deplasman_skor = []
        self.adim1_()
        self.adim_2()
        self.ev_Shabi_tahimi()
        self.deplasman_tahmin()
        self.grafik_evsahibi_deplasman()    
    
    def tablolar_(self):
        return self.tarayici.find_element(By.CLASS_NAME,'e67a6cb121a2998f0608 ')
        

    def tablo_1(self):
        birinci_takim = self.tablolar_()
        birinci_takim = birinci_takim.find_element(By.CSS_SELECTOR,'[data-test-id="LastMatchesTableFirst"]') #ev sahibi takim
        birinci_takim_Adi = birinci_takim.find_element(By.TAG_NAME,"a").get_attribute("text")
        self.ev_Sahibi.append(birinci_takim_Adi)
        skorlar = birinci_takim.find_element(By.CSS_SELECTOR,'[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr')
        for i in skorlar:
            kontrol = i.find_element(By.CSS_SELECTOR,'[data-test-id="TableBodyMatch"]')
            ev_Sahibi = kontrol.find_element(By.CSS_SELECTOR,'[data-test-id="HomeTeam"]').text
            deplasman = kontrol.find_element(By.CSS_SELECTOR,'[data-test-id="AwayTeam"]').text
            skor = kontrol.find_element(By.CSS_SELECTOR,'[data-testid="nsn-button"]').find_element(By.TAG_NAME,"span").text
            if(skor==""):
                continue
            else:
                self.ev_Sahibi.append(f"{ev_Sahibi}/{skor}/{deplasman}")
                
    def tablo_2(self):
       ikinci_takim = self.tablolar_()
       ikinci_takim = ikinci_takim.find_element(By.CSS_SELECTOR,'[data-test-id="LastMatchesTableSecond"]') #deplasman sahibi takim
       ikinci_takim_Adi =ikinci_takim.find_element(By.TAG_NAME,"a").get_attribute("text")
       self.deplasman.append(ikinci_takim_Adi)
       skorlar = ikinci_takim.find_element(By.CSS_SELECTOR,'[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr')
       for i in skorlar:
            kontrol = i.find_element(By.CSS_SELECTOR,'[data-test-id="TableBodyMatch"]')
            ev_Sahibi = kontrol.find_element(By.CSS_SELECTOR,'[data-test-id="HomeTeam"]').text
            deplasman = kontrol.find_element(By.CSS_SELECTOR,'[data-test-id="AwayTeam"]').text
            skor = kontrol.find_element(By.CSS_SELECTOR,'[data-testid="nsn-button"]').find_element(By.TAG_NAME,"span").text
            if(skor==""):
                continue
            else:
                self.deplasman.append(f"{ev_Sahibi}/{skor}/{deplasman}")
    
    def adim1_(self):
        anahtar = "Girona" # => Ev shibi takımın adını giriniz
        for i in self.ev_Sahibi[1:]:
          try:
                ayır = str(i).split("/")
                indexi = ayır.index(anahtar)
                if(indexi==0):
                    t = ayır[1].split("-")
                    t = t[0].strip()
                    self.ev_sahibi_Skor.append(t)
                if(indexi == 2):
                    t = ayır[1].split("-")
                    t = t[1].strip()
                    self.ev_sahibi_Skor.append(t)
          except:
               continue
          
    def adim_2(self):

        anahtar = "Alaves" # => Deplasaman Takiminin Adii Griniz
      
        for i in self.deplasman[1:]:
           try:
                ayır = str(i).split("/")
                indexi = ayır.index(anahtar)
                if(indexi==0):
                    t = ayır[1].split("-")
                    t = t[0].strip()
                    try:
                        t = int(t)
                        self.deplasman_skor.append(t)
                    except:
                        pass

                if(indexi == 2):
                    t = ayır[1].split("-")
                    t = t[1].strip()
                    try:
                         t = int(t)
                         self.deplasman_skor.append(t)
                    except:
                        pass         
           except:
               continue
    
    def ev_Shabi_tahimi(self):
        veri_kumesi = self.ev_sahibi_Skor[::-1]
        veri_kumesi = np.array(veri_kumesi).reshape(-1, 1)
        x = np.arange(len(veri_kumesi)).reshape(-1, 1)

        model = LinearRegression()
        model.fit(x, veri_kumesi)

        gelecekteki_mac_sayisi = len(veri_kumesi) + 1
        tahmin_edilen_gol = model.predict([[gelecekteki_mac_sayisi]])[0][0]
        print(f"Gelecekteki gol tahmini ev sahibi: {tahmin_edilen_gol}")
    
    def deplasman_tahmin(self):
        veri_kumesi = self.deplasman_skor[::-1]
        veri_kumesi = np.array(veri_kumesi).reshape(-1, 1)
        x = np.arange(len(veri_kumesi)).reshape(-1, 1)

        model = LinearRegression()
        model.fit(x, veri_kumesi)

        gelecekteki_mac_sayisi = len(veri_kumesi) + 1
        tahmin_edilen_gol = model.predict([[gelecekteki_mac_sayisi]])[0][0]
        print(f"Gelecekteki gol tahmini deplasman: {tahmin_edilen_gol}")
    
    def grafik_evsahibi_deplasman(self):
        plt.subplot(1,2,1)
        veri_kümesi = self.ev_sahibi_Skor[::-1]
        plt.title("Ev Sahibi Goll", loc = 'left')
        plt.plot(veri_kümesi,color="red",)
        plt.subplot(1,2,2)
        veri_kümesi = self.deplasman_skor[::-1]
        plt.title("Deplamsan Goll", loc = 'left')
        plt.plot(veri_kümesi,color="green")
        plt.show()


if __name__ == "__main__":
    tahmin = SkorTahmin()