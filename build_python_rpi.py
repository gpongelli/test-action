import json
import argparse
import os
import subprocess
import shutil
import tarfile
import wget
import sys
import tempfile
from pathlib import Path


if __name__ == '__main__':
    _links = {}
    with open('python_links.json', mode='r') as fp:
        _links = json.load(fp)
    print(_links)
    _fname = wget.download(_links['3.11'], '.')
    print(f'Downloaded file {_fname}')
    with tempfile.TemporaryDirectory(dir='.') as _tmp:
        _j = os.path.join(_tmp, _fname)
        build_temp = os.path.abspath(_j)
        print(build_temp)
        #sys.exit(0)

        tgz = tarfile.open(_fname)
        tgz.extractall(path=_tmp)
        import time
        # time.sleep(50)

        build_temp = os.path.abspath(os.path.join(_tmp, Path(_fname).stem))
        os.chdir(build_temp)
        subprocess.run(['./configure', '--enable-optimizations'])
        print("OK")
