import os
import sys

if __name__ == '__main__':
    dirname = sys.argv[1]
    os.mkdir(dirname)
    open('{0}/output'.format(dirname), 'w').close()
    open('{0}/input'.format(dirname), 'w').close()
    open('{0}/solution'.format(dirname), 'w').close()
    open('{0}/{1}.py'.format(dirname, dirname.replace('-', '_')), 'w').close()
