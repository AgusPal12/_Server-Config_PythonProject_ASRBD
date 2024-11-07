
#code util pour l'implementation courant.

from colorama import init, Fore, Back, Style

init()  # Initialize colorama

# Foreground colors
print(Fore.RED + 'some red text')
print(Fore.GREEN + 'some green text')
print(Fore.YELLOW + 'some yellow text')
print(Fore.BLUE + 'some blue text')
print(Fore.MAGENTA + 'some magenta text')
print(Fore.CYAN + 'some cyan text')
print(Fore.WHITE + 'some white text')

# Background colors
print(Back.RED + 'some red background text')
print(Back.GREEN + 'some green background text')
print(Back.YELLOW + 'some yellow background text')
print(Back.BLUE + 'some blue background text')
print(Back.MAGENTA + 'some magenta background text')
print(Back.CYAN + 'some cyan background text')
print(Back.WHITE + 'some white background text')

# Reset color
print(Style.RESET_ALL + 'reset color')

# Bold and italic
print(Style.BRIGHT + 'some bright text')
print(Style.DIM + 'some dim text')
print(Style.NORMAL + 'some normal text')
print(Style.RESET_ALL + 'reset style')

# Combine styles
print(Fore.RED + Style.BRIGHT + 'some bright red text')
print(Fore.GREEN + Style.DIM + 'some dim green text')
print(Fore.YELLOW + Style.NORMAL + 'some normal yellow text')

