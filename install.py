#!/usr/bin/python
"""Allows to deploy dotfiles to local machines."""

import os
import sys
import json
from datetime import datetime
import shutil
import imp
import uuid

DEFAULT_TIME_FORMAT = "%Y%m%d%H%M%S"

CONFIG_FILE = "config.json"

INSTALL_SCRIPT = "install.py"

INSTALL_METHOD = "install"


def read_config(config_file):
  """Read the config file if it is found in the current dir, exits otherwise.

  Args:
    config_file: name of configuration file in the current directory
  """
  full_config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                       config_file)
  if not os.path.exists(full_config_file_path):
    print "No config file found at '%s'" % full_config_file_path
    sys.exit(1)
  with open(full_config_file_path, "r") as fd:
    return json.load(fd)


def install_link(source, destination, directory="~"):
  """Create a link at directory/destination pointing to source.

  Note:
    - Missing directory will be created
    - If directory/destination exists it is backed up
  Args:
    source: full path to the source file to link
    destination: name of the link to be created, can be partial path
    directory: base directory in which the link will be created, defaults
      to '~'
  """
  full_destination = os.path.expandvars(os.path.join(os.path.expanduser(directory),
                                                     destination))
  full_source = os.path.join(os.path.abspath(os.path.dirname(__file__)), source)
  if not os.path.exists(full_source):
    print "Source '%s' does not exists. Skipping" % full_source
    return
  if not os.path.exists(os.path.dirname(full_destination)):
    os.makedirs(os.path.dirname(full_destination))
  if os.path.exists(full_destination):
    if not os.path.islink(full_destination):
      backup_file = "%s.%s.bak" % (full_destination,
                                   datetime.now().strftime(DEFAULT_TIME_FORMAT))
      print "'%s' exists, creating backup file %s" % (full_destination, backup_file)
      shutil.copy(full_destination, backup_file)
    os.unlink(full_destination)
    print "Unlink %s" % full_destination
  print "Installing '%s' to '%s'" % (full_source, full_destination)
  os.symlink(full_source, full_destination)


def install_sub_module(directory):
  """If a python file named install.py is found in the given directory it will
  be imported and if a method named 'install' is found it will be called."""
  install_script = os.path.abspath(os.path.join(directory, INSTALL_SCRIPT))
  if os.path.isfile(install_script):
    module = imp.load_source("%s.%s" % (install_script, str(uuid.uuid4())),
                             install_script)
    for name in dir(module):
      obj = getattr(module, name)
      if callable(obj) and obj.__name__ == INSTALL_METHOD:
        print "Calling %s:%s" % (install_script, obj.__name__)
        obj()


def install():
  config = read_config(CONFIG_FILE)
  for source, destination in config.iteritems():
    install_link(source, destination)
  for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
      install_sub_module(path)


if __name__ == "__main__":
  install()

