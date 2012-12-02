#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
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

        stdout, stderr = pipe.communicate()

        string = ["# " + text]
        if stdout: string.append(stdout)
        if stderr: string.append(stderr)

        return "\n".join(string)

if __name__ == "__main__":
    print Controller().run('dir')