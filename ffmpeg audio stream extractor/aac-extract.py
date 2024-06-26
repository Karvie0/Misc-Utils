#!/usr/bin/python3
import os
import argparse


# To-Do:
# - add wildcards to stream selection
# - default to selecting all streams
# - batch file input

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("input", help="input file\n- batch file input not supported")
parser.add_argument("-o", "--output", help="output file base name\n- stream number and file extension are added automatically\n- defaults to input filename")
parser.add_argument("-s", "--streams", type=str, help="comma separated list of stream indices\n- defaults to 0")

args = parser.parse_args()



# edit args
if args.streams is not None:
    args.streams = [s.strip() for s in args.streams.split(",")]
else:
    args.streams = ["0"]

if args.output is None:
    args.output = os.path.splitext(args.input)[0]

args.input = args.input.replace(" ", "\\ ")
args.output = args.output.replace(" ", "\\ ")



# generate command
command = "ffmpeg -i " + str(args.input)

for s in args.streams:
    command += " -map 0:a:" + str(s) + " -c:a copy " + str(args.output) + "_" + str(s) + ".aac"



# execute
os.system(command)
