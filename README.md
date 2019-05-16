# qsubmitter.py
Submits Qsub command with a one-line command line interphase by creating a qsub script, preparing output log folder, and submitting to PBS-TORQUE job scheduler. 

## Usage

```
$ python qsubmitter.py --help
usage: qsubmitter.py [-h] -c [COMMAND [COMMAND ...]] [-q QUE] [-n NODES]
                     [-m MEM] [-p PPN] [-e EMAIL] [-s SCRIPT_DIR]
                     [-i SCRIPT_NAME] [-d DRYRUN] [-l LOG_DIR]

optional arguments:
  -h, --help            show this help message and exit
  -c [COMMAND [COMMAND ...]], --command [COMMAND [COMMAND ...]]
                        Command line to be executed
  -q QUE, --que QUE     Que type
  -n NODES, --nodes NODES
                        Nodes to reserve
  -m MEM, --mem MEM     Memory to reserve
  -p PPN, --ppn PPN     Number of processors to use
  -e EMAIL, --email EMAIL
                        Email for alerts, default= EMAIL variable as the environmental variable. Can set as `export EMAIL=youremail@email.com` 
  -s SCRIPT_DIR, --script_dir SCRIPT_DIR
                        directory to write qsub script
  -i SCRIPT_NAME, --script_name SCRIPT_NAME
                        name for submitter script
  -d DRYRUN, --dryrun DRYRUN
                        Create script, but do not execute
  -l LOG_DIR, --log_dir LOG_DIR
                        directory to store output logs
```

