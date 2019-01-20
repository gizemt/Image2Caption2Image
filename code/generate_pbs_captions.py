# This script creates a PBS file that runs one hyperameter setting
# on a single node.

import sys

walltime = sys.argv[1]
jobname = sys.argv[2]
netid = sys.argv[3]

# Change these if your hyperparameters change
file_name = sys.argv[4]

print "#!/bin/bash"
print "#PBS -l nodes=1:ppn=16:xk"
print "#PBS -N {0}".format(jobname)
#print "#PBS -N {0}_{1}".format(jobname,dataset_batch_no) # Change this if your hyperparameters change
print "#PBS -l walltime={0}".format(walltime)
print "#PBS -e $PBS_JOBNAME.$PBS_JOBID.err"
print "#PBS -o $PBS_JOBNAME.$PBS_JOBID.out"
print "#PBS -M {0}@illinois.edu".format(netid)

print "cd ~/bin/deepnn/im2txt"


print ". /opt/modules/default/init/bash"
print "module load bwpy"
print "module load cudatoolkit"
print "pwd"

print "aprun -n 1 -N 1 python bw_captions_script.py {0}".format(file_name)
# print "aprun -n 1 -N 1 python {0} {1}".format(training_file, dataset_batch_no) # Change this if your hyperameters change
