### Hexlet tests and linter status:
[![Actions Status](https://github.com/webAmoeba/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/webAmoeba/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bc1790801cf78248d161/maintainability)](https://codeclimate.com/github/webAmoeba/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/bc1790801cf78248d161/test_coverage)](https://codeclimate.com/github/webAmoeba/python-project-50/test_coverage)

# Gendiff

Welcome to the Gendiff project! This project is designed to help you compare configuration files and see the differences between them. It supports various formats such as JSON, YAML, and YML. The tool provides a clear and structured output, making it easy to understand the changes.

## Requirements

To run this project, you need to have the following software installed:

- Python >=3.12.0
- Uv

## Installation

To set up the project, navigate to the project directory and run the following command:

```bash
make i
```
or
```bash
uv tool install .
```

## Usage

To start using the Brain Games, use the following command:

```bash
gendiff -h
```
```bash
gendiff path/file1.json path/file2.yaml | file.yml
```

[![asciicast](https://asciinema.org/a/784o2u5Nuczc1pYV25jvFEQgc.svg)](https://asciinema.org/a/784o2u5Nuczc1pYV25jvFEQgc)
