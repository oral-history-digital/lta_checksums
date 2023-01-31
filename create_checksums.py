#!/usr/bin/env python3

"""Standalone script for recursively creating SHA256 checksums."""

from pathlib import Path
from hashlib import sha256
from argparse import ArgumentParser

VERSION = '0.1.2'

def file_checksum(file, hash_method):
    """Return checksum of a file with the specified algorithm."""

    hash = hash_method()

    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)

    digest = hash.hexdigest()
    return digest


def save_checksum(file, checksum):
    with open(file, 'w') as f:
        f.write(f'{checksum}\n')


def treat_path(path):
    """Treat path recursively."""
    if path.is_file() and path.suffix != '.sha256':
        checksum = file_checksum(path, sha256)
        checksum_path = path.with_suffix(f'{path.suffix}.sha256')
        save_checksum(checksum_path, checksum)
    elif path.is_dir():
        for subpath in path.iterdir():
            treat_path(subpath)


def create_checksums(path):
    """Create checksums beginning at path."""

    if not path.exists():
        print(f'{str(path)} does not exist')
    elif path.is_file() or path.is_dir():
        treat_path(path)
    else:
        print(f'{str(path)} is neither file nor directory')


def cli():
    """Command line interface."""
    parser = ArgumentParser(description='Recursively create SHA256 checksums.')
    parser.add_argument('paths', metavar='PATHS', type=str, nargs='+',
                        help='files or directories')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    args = parser.parse_args()

    paths = args.paths

    for path in paths:
        create_checksums(Path(path))


if __name__ == "__main__":
    cli()
