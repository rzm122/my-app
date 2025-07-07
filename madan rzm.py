from requests import post
from time import sleep
from random import choice
import datetime
import sys
from colorama import Fore
from os import system
import time

fruit_passport = str("dfc0778f9d3fa63401c82b3303ae6d9d")
power = "13374000" # قدرت منفعت معدن
capacity = "500000" #ظرفیت معدن
deposit_ask = input('Do you want to deposit money in the bank? (Y or N) >> ') #ذخیره توی بانک؟
deposit_ask = True if deposit_ask.lower() == "y" else False
    
maining_time = int((int(capacity) / (int(power) / 3600)))
    
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A750F Build/QP1A.190711.020)',
    'Host': 'iran.fruitcraft.ir',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'cookie': f'FRUITPASSPORT={fruit_passport}'}

collect_data = "edata=Gk4KXVpRXRJDSEMTfmMXSA%3D%3D"
deposit_data = "edata=Gk4KUEFQQERbUDpPAwkBAVRZRFQ4UB4aWwoEEA5GW05bAlUECgRTQ1JIBVQEUAVdFwhSQAAJCFsDF1BRBVoMBhFJ"

print("\n\n\n")

def collect_gold(data, headers):
    #proxy = {"http" : "http://188.121.103.205:80"}
    collect = post("http://iran.fruitcraft.ir/cards/collectgold",
        data=data,
        headers=headers,
    )

def countdown(seconds):
    """تابع شمارش معکوس در یک خط با فرمت MM:SS"""
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)  # تبدیل به دقیقه و ثانیه
        print(f"{Fore.CYAN}{mins:02d}:{secs:02d}{Fore.RESET}", end="\r")  # چاپ در همان خط
        time.sleep(1)
        seconds -= 1
    print("تکمیل شد!")  # پیام نهایی

def deposit_to_bank(data, headers):
    deposit = post("http://iran.fruitcraft.ir/player/deposittobank",
        data=data,
        headers=headers,
    )

def start():
    done = 0
    lost = 0
    deposit_status = "No"  # مقدار پیشفرض
    
    for i in range(400):
        try:
            collect_gold(collect_data, headers)
            if deposit_ask:
                deposit_to_bank(deposit_data, headers)
                deposit_status = "Yes"  # اگر واریز انجام شد
            done += 1
        except Exception as e:
            print(e)
            lost += 1
        finally:
            sys.stdout.write(
                f"\r• Gold Mine Done: {Fore.GREEN}{done}{Fore.RESET} "
                f"\nGold Mine Lost: {Fore.RED}{lost}{Fore.RESET} "
                f"\nBank Deposit: {deposit_status}\n\n"
            )
            sys.stdout.flush()
            countdown(maining_time)

def main():
    system("clear")
    
    
    start()

if __name__ == "__main__":
    main()