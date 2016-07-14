import sys
import argparse

args = argparse.ArgumentParser(description='')
args.add_argument('-i', '--input', help='Youd should provide the name of the input file.', required=True)
args.add_argument('-o', '--output', help='Your should provide the name of the output file.', required=True)
args = vars(args.parse_args())

print ''
print '-------------------------------------------------------------------------------------------------------'
print 'Cool, right?! ;)'
print '-------------------------------------------------------------------------------------------------------'

print '======================================================================================================='
print args
print '======================================================================================================='
print ''
