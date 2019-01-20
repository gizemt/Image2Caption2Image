import subprocess
import sys
training_steps = sys.argv[1]
print "start"
subprocess.call("bw_training_script.sh "+training_steps, shell = True)
print "end"

