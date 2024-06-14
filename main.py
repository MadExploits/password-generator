#!/usr/bin/env python3

import requests
import urllib3
from os import system, name
from colorama import Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class pwgen:
    def __init__(self):
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36'
        }

    def hapus_ssl(self, text):
        return text.replace('https', '').replace('http', '').replace('/', '').replace(':', '')

    def pecah_web(self, web_domain):
        text_domain = self.hapus_ssl(web_domain)
        if "." in text_domain:
            _p1 = text_domain.split(".")
            if len(_p1) > 1:
                return _p1[1] if _p1[0] == "www" else _p1[0]
            return _p1[0]
        return text_domain
            
    def satukanweb(self, web_domain):
        text_domain1 = self.hapus_ssl(web_domain)
        if "." in text_domain1:
            _p2 = text_domain1.split(".")
            if len(_p2) > 1:
                return f"{_p2[1]}{_p2[2]}" if _p2[0] == "www" else f"{_p2[0]}{_p2[1]}"
            return f"{_p2[0]}{_p2[1]}"
        return text_domain1

    def passwords(self, websites, usernames):
        username = usernames.strip().split(",")
        passwords = []

        common_passwords = [
            '{}', '{}1', '{}2', '{}3', '{}4', '{}5', '{}6', '{}7', '{}8', '{}9', '{}0', '{}01', '{}02', '{}03', '{}04', 
            '{}05', '{}06', '{}07', '{}08', '{}09', '{}10', '{}11', '{}12', '{}13', '{}14', '{}15', '{}16', '{}17', 
            '{}18', '{}19', '{}20', '{}21', '{}22', '{}23', '{}24', '{}25', '{}26', '{}27', '{}28', '{}29', '{}30', 
            '{}31', '{}32', '{}33', '{}34', '{}35', '{}36', '{}37', '{}38', '{}39', '{}40', '{}41', '{}42', '{}43', 
            '{}44', '{}45', '{}46', '{}47', '{}48', '{}49', '{}50', '{}51', '{}52', '{}53', '{}54', '{}55', '{}56', 
            '{}57', '{}58', '{}59', '{}60', '{}61', '{}62', '{}63', '{}64', '{}65', '{}66', '{}67', '{}68', '{}69', 
            '{}70', '{}71', '{}72', '{}73', '{}74', '{}75', '{}76', '{}77', '{}78', '{}79', '{}80', '{}81', '{}82', 
            '{}83', '{}84', '{}85', '{}86', '{}87', '{}88', '{}89', '{}90', '{}91', '{}92', '{}93', '{}94', '{}95', 
            '{}96', '{}97', '{}98', '{}99', '{}100', '{}101', '{}102', '{}103', '{}104', '{}105', '{}106', '{}107', 
            '{}108', '{}109', '{}110', '{}111', '{}112', '{}113', '{}114', '{}115', '{}116', '{}117', '{}118', '{}119', 
            '{}120', '{}121', '{}122', '{}123', '{}124', '{}125', '{}126', '{}127', '{}128', '{}129', '{}130', '{}131', 
            '{}132', '{}133', '{}134', '{}135', '{}136', '{}137', '{}138', '{}139', '{}140', '{}141', '{}142', '{}143', 
            '{}144', '{}145', '{}146', '{}147', '{}148', '{}149', '{}150', '{}151', '{}152', '{}153', '{}154', '{}155', 
            '{}156', '{}157', '{}158', '{}159', '{}160', '{}161', '{}162', '{}163', '{}164', '{}165', '{}166', '{}167', 
            '{}168', '{}169', '{}170', '{}171', '{}172', '{}173', '{}174', '{}175', '{}176', '{}177', '{}178', '{}179', 
            '{}180', '{}181', '{}182', '{}183', '{}184', '{}185', '{}186', '{}187', '{}188', '{}189', '{}190', '{}191', 
            '{}192', '{}193', '{}194', '{}195', '{}196', '{}197', '{}198', '{}199', '{}200', '{}201', '{}202', '{}203', 
            '{}204', '{}205', '{}206', '{}207', '{}208', '{}209', '{}210', '{}211', '{}212', '{}213', '{}214', '{}215', 
            '{}216', '{}217', '{}218', '{}219', '{}220', '{}221', '{}222', '{}223', '{}224', '{}225', '{}226', '{}227', 
            '{}228', '{}229', '{}230', '{}231', '{}232', '{}233', '{}234', '{}235', '{}236', '{}237', '{}238', '{}239', 
            '{}240', '{}241', '{}242', '{}243', '{}244', '{}245', '{}246', '{}247', '{}248', '{}249', '{}250', '{}251', 
            '{}252', '{}253', '{}254', '{}255', '{}256', '{}257', '{}258', '{}259', '{}260', '{}261', '{}262', '{}263', 
            '{}264', '{}265', '{}266', '{}267', '{}268', '{}269', '{}270', '{}271', '{}272', '{}273', '{}274', '{}275', 
            '{}276', '{}277', '{}278', '{}279', '{}280', '{}281', '{}282', '{}283', '{}284', '{}285', '{}286', '{}287', 
            '{}288', '{}289', '{}290', '{}291', '{}292', '{}293', '{}294', '{}295', '{}296', '{}297', '{}298', '{}299', 
            '{}300', '{}admin', '{}Admin', '{}Password', '{}password', '{}pass123', '{}1234!', '{}12345!', '{}!@', '{}$%^',
            '{}2017', '{}2018', '{}2019', '{}2020', '{}2021', '{}2022', '{}2023', '{}2024', '{}admin@123', '{}#!', '{}@2017!',
            '{}@2018!', '{}@2019!', '{}@2020!', '{}@2021!', '{}@2022!', '{}@2023!', '{}@2024!', 'admin@{}', 'admin@{}123', 
            '{}@{}', '{}@{}123', '{}{}', '{}{}!@', '{}{}123', '{}!', '{}!@', '{}!#', '{}000', '{}01', '{}1', '{}1111', '{}12', 
            '{}123!', '{}1234', '{}12345', '{}123456', '{}321', '{}333', '{}4444', '{}54321', '{}666', '{}@123', '{}@2024', 
            '{}@321', '{}888', '{}999', '{}pass', '{}password', '{}pass123', '{}pass@2021', '{}secure', '{}security', 
            '{}access', '{}login', '{}letmein', '{}welcome', '{}welcome123', '{}changeme', '{}qwerty', '{}asdfgh', '{}zxcvbn', 
            '{}passw0rd', '{}P@ssw0rd', '{}P@ssword!', '{}Admin!', '{}Admin123', '{}User', '{}User123', '{}guest', '{}guest123',
            '{}Default', '{}default123', '{}password!', '{}password1!', '{}qwe123', '{}123abc', '{}1qaz2wsx', '{}abc123', 
            '{}xyz789', '{}monkey', '{}mustang', '{}dragon', '{}baseball', '{}football', '{}master', '{}shadow', '{}superman', 
            '{}iloveyou', '{}sunshine', '{}princess', '{}starwars', '{}rockyou', '{}flower', '{}sunshine', '{}mickey', 
            '{}cheese', '{}computer', '{}internet', '{}network', '{}device', '{}system', '{}secure123', '{}security123', 
            '{}adminpass', '{}root', '{}admin12345', '{}admin1', '{}admin1234!', '{}admin!@#$', '{}12345678', '{}87654321', 
            '{}securepass', '{}mypassword', '{}newpass', '{}mysecurepass', '{}trustno1', '{}letmein123', '{}p@ssw0rd', 
            '{}newpassword', '{}changepassword', '{}myadmin', '{}myadmin123', '{}defaultpass', '{}root123', '{}rootpass'
        ]



        for cp in common_passwords:
            if '{}' in cp and '{}' not in cp.replace('{}', '', 1):
                passwords.append(cp.format(self.satukanweb(websites)))
                passwords.append(cp.format(self.pecah_web(websites)))
        
        if username:
            userpw = [
                '{}', '{}@111', '{}@{}', '{}@{}123', '{}@{}123!', '{}{}', 'admin@{}', 'admin_{}', 'administrator@{}', 
                '{}2017', '{}2018', '{}2019', '{}2020', '{}2021', '{}2022', '{}2023', '{}2024', '{}@2017', '{}@2018', 
                '{}@2019', '{}@2020', '{}@2021', '{}@2022', '{}@2023', '{}@2024', '{}@2017!', '{}@2018!', '{}@2019!', 
                '{}@2020!', '{}@2021!', '{}@2022!', '{}@2023!', '{}@2024!', '{}@2017!#', '{}@2018!#', '{}@2019!#', 
                '{}@2020!#', '{}@2021!#', '{}@2022!#', '{}@2023!#', '{}@2024!#', '{}@2017!#@', '{}@2018!#@', 
                '{}@2019!#@', '{}@2020!#@', '{}@2021!#@', '{}@2022!#@', '{}@2023!#@', '{}@2024!#@', '{}_password', 
                '{}_admin', '{}_admin123', '{}_user', '{}_user123', '{}_pass', '{}_pass123', '{}_secure', 
                '{}_login', '{}_access', '{}_changeme', '{}_qwerty', '{}_asdf', '{}_zxcv', '{}_test', 
                '{}_test123', '{}_12345', '{}_password1', '{}_welcome', '{}_welcome123', '{}{}', '{}1', 
                '{}123', '{}1234', '{}12345', '{}admin!', '{}admin1!', '{}admin1234',
                        ]


            for user in username:
                for up in userpw:
                    if '{}' in up and '{}' not in up.replace('{}', '', 1):
                        passwords.append(up.format(user))
                    elif up.count('{}') == 2:
                        passwords.append(up.format(user, self.satukanweb(websites)))
                        passwords.append(up.format(user, self.pecah_web(websites)))

        with open('wordlists/password.txt', 'r') as r:
            passwords.extend(r.read().split("\n"))

        return passwords

    def genpw(self, website, username):
        user_list = username.strip().split(",")
        print("===================[LIST USER]==================================")
        with open(f"{self.hapus_ssl(website)}-user.txt", 'w+') as wru:
            for user in user_list:
                print("[!] => " + user)
                wru.write(user + "\n")
        print("===================[END]========================================")
        usern = username
        passwrd = self.passwords(website, usern)
        with open(f"{self.hapus_ssl(website)}.txt", 'w+') as wr:
            for pw in passwrd:
                wr.write(pw + "\n")
                print(pw)
            print(f"Saved to [{self.hapus_ssl(website)}.txt]")
        print(f"Saved to [{self.hapus_ssl(website)}-user.txt]")

    def clear_command_line(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def main(self):
        print(Fore.GREEN + f"""
                      __  ____                      
 /'\_/`\             /\ \/\  _`\                    
/\      \     __     \_\ \ \ \L\_\     __    ___    
\ \ \__\ \  /'__`\   /'_` \ \ \L_L   /'__`\/' _ `\  
 \ \ \_/\ \/\ \L\.\_/\ \L\ \ \ \/, \/\  __//\ \/\ \ 
  \ \_\\\\ \_\ \__/.\_\ \___,_\ \____/\ \____\ \_\ \_\\
   \/_/ \/_/\/__/\/_/\/__,_ /\/___/  \/____/\/_/\/_/
                                                    
               {Style.RESET_ALL}                                     
 [+] www.github.com/Madexploits   
 [!] Password Generator For Intruder
 [!] Created By MadExploits      
                        
""")
        website = input("[+] Website: ")
        print("""
[1] => Common Login
[2] => Defaults Login
[3] => Custom
[4] => List User
""")
        choice = input("[n] [Number]: ")
        
        if choice == "1":
            username_def = 'admin,operator,adminweb,users,staff,guest,user,info,administrator,administrators,webadmin,adminweb,pengguna,tamu,admin1,admin2,admin3'
            self.genpw(website, username_def)
        elif choice == "2":
            username_defa = 'admin,admins,users,staff,guest,user,info,administrator,administrators,webadmin,adminweb'
            self.genpw(website, username_defa)
        elif choice == "3":
            usernm = input("Input Your Username: ")
            self.genpw(website, usernm)
        elif choice == "4":
            list_user = input("List Of Users : ")
            with open(list_user, "r") as res:
                read = res.read()
                splt = read.replace("\n", ',').strip(",")
                self.genpw(website, splt)
        else:
            print("Please input number between 1 - 4.")
            exit()

if __name__ == "__main__":
    run = pwgen()
    run.clear_command_line()
    run.main()
