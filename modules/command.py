import subprocess

def run(**args):
    
    
    print "[*] In command module."
    try:
        cmd_output = subprocess.check_output(args['command'], shell=True)
    except Exception, e:
        cmd_output = e
    return cmd_output
