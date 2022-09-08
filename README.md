# pycam_bot

[![Tests](https://github.com/natir/pycam_bot/workflows/Tests/badge.svg)](https://github.com/natir/pycam_bot/actions/workflows/ci.yml)
[![Lints](https://github.com/natir/pycam_bot/workflows/Lints/badge.svg)](https://github.com/natir/pycam_bot/actions/workflows/lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A python twitch chat bot for my twitch channel cam_doc

## Requirements

pycam_bot requires Python >=3.10

## Installation

### Pip

Install with `pip`:

```bash
$ python -m pip install --user https://github.com/natir/pycam_bot.git
```

## Run

Create a file `pycam_bot.ini` with content similar to [pycam_bot.example.ini](https://github.com/natir/pycam_doc/blob/main/etc/pycam_bot.example.ini)

Run:
```bash
pycam_bot -c pycam_bot.ini
```
