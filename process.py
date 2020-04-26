# helps us work with child processes
import subprocess
pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]
# variable pl is byte array containing output of this command
print(pl.decode('utf-8'))
