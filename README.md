# debug-later: Store Python traceback for later debugging

`debug-later` writes the traceback of an exception that you can later load in
a Python debugger. `debug-later` works with `pdb`, `pudb`, `ipdb` and `pdbpp`.

You can use the generated file to debug on a different machine (assuming the
environment is the same), without having access to the source code.

## Installation

```sh
pip install debug-later
```

## Example

```
```

## Motivation

The [Ploomber team](https://github.com/ploomber/ploomber) develops tools for
data analysis. When data analysis code executes non-interactively
(example: a daily cron job that generates a report), it becomes hard to debug
since logs are often insufficient, forcing data practitioners to re-run the
code from scratch, which can take a lot of time.

`debug-later` can be used for any use case to facilitate post-mortem debugging.

## Use cases

* Debug long-running code (e.g., crashed Machine Learning job)
* Debug multiprocessing code (generate one dump file for each process)

## Credits

This project is a fork of [Eli Finer's pydump](https://github.com/elifiner/pydump).