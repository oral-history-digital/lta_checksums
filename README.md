# lta-checksums

This is a standalone script to recursively generate SHA256 checksums
used for long term archiving within the
[Oral History.Digital](https://www.oral-history.digital/)
project of Freie Universität Berlin.

The script is standalone so it can be easily copied to the media server
and then executed via SSH. It only uses features of the Python Standard
Library and requires at least Python 3.4.

## Installation

Copy the script `create_checksums.py` to your path.

If your system uses the command `python` instead of `python3` change the first line
of the script to

```bash
#!/usr/bin/env python
```

Make the script executable with

```console
chmod +x create_checksums.py
```

## Usage

```console
$ create_checksums.py FILE1 FILE2 ...
```

```console
$ create_checksums.py DIR1 DIR2 ...
```
