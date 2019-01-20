import subprocess
import sys
file_names = sys.argv[1]
print "start"
subprocess.call("bw_captions_script.sh "+file_names, shell = True)
print "end"
