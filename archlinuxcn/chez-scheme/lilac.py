#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()
  add_into_array('conflicts', ['mit-scheme'])
  try:
    os.unlink('build')
  except FileNotFoundError:
    return

def post_build():
    _G.aur_building_files.remove('build')
    aur_post_build()

if __name__ == '__main__':
  single_main()

