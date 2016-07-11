import os
import sys
import time
import pdb
import subprocess
from random import randint

ps = subprocess.Popen( 'git log --pretty=format:"%h" -n 7 '.split(), stdout=subprocess.PIPE)
output = subprocess.check_output("tail -n 7".split(), stdin=ps.stdout)

commits = [ i.strip('"') for i in output.split()]


for  commit in reversed(commits):
    get_branch_cmds = "git rev-parse --abbrev-ref HEAD".split()
    branch_name = subprocess.check_output(get_branch_cmds).rstrip()

    cmd = "git push origin {commit_md5}:{branch_name}".format(
        commit_md5=commit,
        branch_name=branch_name
        )
    print(cmd)
    sleep_time = randint(1000, 1880)
    os.system(cmd)
    print(sleep_time)
    time.sleep(sleep_time)
