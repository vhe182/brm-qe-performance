#! /usr/bin/env python
"""
Contains the code for locating, untaring, prepping, and loading
performance testing data for BRM system.  This test is specifically
for the brm-pipe server.

Note: Coordinate with OPs team for exact location of data drop before
running this command.

"""
import os
import tarfile


IN_DIRECTORY = '/Users/vict0198/tmp/data/in/'
OUT_DIRECTORY = '/Users/vict0198/tmp/data/out/'
DATA_DIRECTORY = '/Users/vict0198/tmp/testbed/'

def locate_data():
  print "locating data..."
  files = [f for f in os.listdir(DATA_DIRECTORY)
           if os.path.isfile(os.path.join(DATA_DIRECTORY, f))]
  cdrfiles = [f for f in files if 'cdr' in f]
  return cdrfiles

def make_directory(cdrfiles):
  print "making directories..."
  directories = []
  for file in cdrfiles:
    file_name = file.replace(".tar.gz","",1)
    directory = DATA_DIRECTORY + file_name
    directories.append(directory)
    if not os.path.exists(directory):
      os.mkdir(directory)
  return directories

def untar_data(files, directories):
  print "untaring archives..."
  i = 0
  for file in files:
    tar = tarfile.open(DATA_DIRECTORY+file, 'r:gz')
    tar.extractall(directories[i])
    i += 1

def rename_files(directories):
  print "renaming files..."
  for directory in directories:
    for filename in os.listdir(directory):
      print filename
      os.rename(filename, filename[:-4] + 'cdr')

def load_files():
  print "loading files..."
  print "TEST START"

def change_pvt():
  """
  change_pvt() needs to execute RPCs in the brm app[1,2,3],
  whichever is being used for testing.
  """
  print "in change_pvt"

def confirm_pvt():
  """
  confirm_pvt() needs to execute RPCs in the brm app[1,2,3],
  whichever is being used for testing.
  """
  print "in confirm_pvt"

def main():

  #change_pvt()
  #confirm_pvt()
  files = locate_data()
  directories = make_directory(files)
  untar_data(files, directories)
  rename_files(directories)
  load_files()

if '__main__' == __name__:
  main()
