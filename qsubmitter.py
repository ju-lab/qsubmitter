#!/home/users/cjyoon/anaconda3/bin/python
''' 
Dec 13 2017 Chris Yoon (cjyoon@kaist.ac.kr)
script that will create a qsub submission script and submit jobs
'''

import sys
import os
import subprocess
import argparse
import re
import shlex

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', nargs='*', required=True, help='Command line to be executed')
    parser.add_argument('-q', '--que', default='long', help='Que type')
    parser.add_argument('-n', '--nodes', default='1', help='Nodes to reserve')
    parser.add_argument('-m', '--mem', default='4gb', help='Memory to reserve')
    parser.add_argument('-p', '--ppn', default='1', help='Number of processors to use')
    parser.add_argument('-e', '--email', default='julab.job@gmail.com', help='Email for alerts')
    parser.add_argument('-s', '--script_dir', default=os.getcwd(), help='directory to write qsub script')
    parser.add_argument('-i', '--script_name', default='submission.sh', help='name for submitter script')
    parser.add_argument('-d', '--dryrun', default=0, type=int,  help='Create script, but do not execute')
    parser.add_argument('-l', '--log_dir', default=os.path.join(os.getcwd(), 'log'), help='directory to store output logs')

    args = vars(parser.parse_args())
        
    return args['command'], args['que'], args['nodes'], args['mem'], args['ppn'], args['email'], args['script_dir'], args['script_name'], args['dryrun'], args['log_dir']

def createDirectory(directory):
    '''create a new directory it it does not already exist'''
    if not os.path.isdir(directory):
        os.mkdir(directory)

    return 0


def submission_header(que, nodes, mem, ppn, email, script_name, log_dir): 
    '''creates string for the header PBS options'''
    logfile = script_name + '.log' 
    absolute_logfile = os.path.abspath(os.path.join(log_dir, logfile))
    header = f'#!/bin/bash\n#PBS -l nodes={nodes}:ppn={ppn},mem={mem}\n#PBS -M {email}\n#PBS -m abe\n#PBS -j oe\n#PBS -q {que}\n#PBS -o {absolute_logfile}\ncd $PBS_O_WORKDIR\n'
    return header
 

def main():
    command, que, nodes, mem, ppn, email, script_dir, script_name, dryrun, log_dir = argument_parser()
    script_path = os.path.join(script_dir, script_name)
    
    #create script  directory
    createDirectory(script_dir)
    
    #create output log directory
    createDirectory(log_dir)
    
    # stdout / stderr added Jan 30 2018
    stdoutfile = os.path.join(log_dir, os.path.basename(script_name) + '.stdout')
    stderrfile = os.path.join(log_dir, os.path.basename(script_name) + '.stderr') 

    # create scripts
    with open(script_path, 'w') as f:
        header = submission_header(que, nodes, mem, ppn, email, script_name, log_dir)
        f.write(header)
        f.write(' '.join(command))
        if re.search(string=' '.join(command), pattern='>') != None: # if output is already redirected finish writing script
            pass
        else:
            f.write(f' 1> {stdoutfile} 2> {stderrfile}')


    if not dryrun:
        submission = subprocess.Popen(shlex.split('qsub ' + script_path))
        submission.wait()
        print(f'{script_path} submitted')


if __name__ == "__main__":
    main()
 
