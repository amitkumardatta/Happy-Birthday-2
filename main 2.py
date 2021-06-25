import subprocess, sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "--disable-pip-version-check", "-q", "install", package])


install('pyfiglet')
import pyfiglet

# Text in digital font
out = pyfiglet.figlet_format('     Happy', font="digital")
out1 = pyfiglet.figlet_format('  Birthday', font="digital")
out2 = pyfiglet.figlet_format('Amit Kumar Datta', font="digital")
print(out)
print(out1)
print(out2)
print(" 🕯️" * 4)
for i in range(2):
    print('⏹' * 7)
    print('⬜' * 7)
print("⏹" * 7)