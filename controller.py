#-------------------------------------------------------------------------------
# Name:        CL GUI Controller
# Purpose:     Simulates a basic shell prompt
#
# Author:      Alex
#
# Created:     02/12/2012
# Copyright:   (c) Alex 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import subprocess

class Controller(object):
    def __init__(self):
        pass

    def run(self, text):

        # Run command
        pipe = subprocess.Popen(text.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)

        # Communicate with stdout, stderr pipes
        stdout, stderr = pipe.communicate()

        # Create list of return arguments
        string = ["# " + text]
        if stdout: string.append(stdout)
        if stderr: string.append(stderr)

        # Join list with newlines and turn into string
        return "\n".join(string)

if __name__ == "__main__":
    # If this script is run seperately, just print 'dir'
    print Controller().run('dir')