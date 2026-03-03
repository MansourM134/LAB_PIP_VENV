from art import *
from colorama import Fore, Back, Style


dancing_fonts = text2art("dance",font='dancingfont',chr_ignore=True)
decore = decor("rand",both=True)
aprint("dancing people")
#print(Fore.RED + 'some red text')



print(decore)
print(Fore.LIGHTMAGENTA_EX + dancing_fonts + Style.RESET_ALL)
print(decore)
aprint("dancing people")


