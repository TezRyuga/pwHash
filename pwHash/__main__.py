#!/usr/bin/env python3
import hashlib
import click
import sys

@click.command()
@click.argument('stringtohash', nargs=1)
@click.argument('algorithm', nargs=1)
def hashThis(stringtohash, algorithm):

    #if algo not available
    if algorithm not in hashlib.algorithms_guaranteed:
        sys.exit("invalid algorithm. valid list: " + str(hashlib.algorithms_guaranteed))

    #algo is in system
    h = hashlib.new(algorithm)
    h.update(stringtohash.encode('utf-8'))
    print(h.hexdigest())

if __name__ == '__main__':
    hashThis()
