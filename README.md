# NORGAL

## About
Norgal takes NGS sequencing reads as input (currently only Illumina paired end reads are supported) and tries to assemble the mitochondrial genome using kmer frequencies.

## Dependencies and requirements
You need:
- Python2.7+ or Python3 (it's written for python3, but should work for 2.7 as well)
- Java
- matplotlib

Mac is not supported yet, as some binaries are Linux-only. I'm working on alternatives.

Memory requirements scale with the size of your input data.
Norgal has been tested on 16gb, 32gb and 64 gb machines. If you have a desktop computer, it might work as long as your data is not too big.
In other words, if your reads are only a few gb in size it should work, but if your reads are for example 12gb each, and you have 12gb of RAM in your computer, it most likely will not work, and you'll have to run it on a node or similar.

## Installation
Download the program like this:
> git clone https://github.com/kosaidtu/norgal.git

The script norgal.py is the main executable. That's it. You can add the norgal folder to your path for ease of use. Or you can symlink it to your bin-folder:

> ln -s NORGAL/norgal.py ~/bin

> python norgal.py -h

or you can just call it directly:
> python norgal/norgal.py -h

If the help-message shows up, it's most likely installed correctly.

## How to run
Will have tutorial here for later. In general, if you have paired end data f.fq and r.fq, you run it like this:
> python norgal.py -i f.fq r.fq -o norgal_output

## How to cite
Manuscript in preparation.
