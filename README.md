<div align="center">
  <img src="logo.jpg" alt="pdf-unlocker" width="200"/>

  # pdf-unlocker

  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.7+-3776ab.svg)](https://python.org)

  **🔓 Batch unlock password-protected PDFs while keeping your originals safe**

</div>

## Overview

pdf-unlocker is a Python CLI tool that processes directories of password-protected PDFs, prompting for passwords interactively and creating unlocked versions with a `.unlocked.pdf` suffix. Your original files remain untouched.

## Features

- **Batch processing** - Process entire directories of PDFs at once
- **Smart detection** - Automatically identifies encrypted PDFs, skips unprotected ones
- **Safe output** - Creates `.unlocked.pdf` files, preserving originals
- **Idempotent** - Skips files that already have unlocked versions
- **Interactive retry** - Wrong password? Retry or skip without losing progress
- **Progress tracking** - Visual progress bar with tqdm

## Quick Start

```bash
# Clone and install
git clone https://github.com/tsilva/pdf-unlocker.git
cd pdf-unlocker
pip install -r requirements.txt

# Run
python main.py /path/to/pdf/folder
```

## Installation

### Using pip

```bash
git clone https://github.com/tsilva/pdf-unlocker.git
cd pdf-unlocker
pip install -r requirements.txt
```

### Using conda

```bash
git clone https://github.com/tsilva/pdf-unlocker.git
cd pdf-unlocker
conda env create -f environment.yml
conda activate pdf-unlocker
```

## Usage

Point the tool at a directory containing password-protected PDFs:

```bash
python main.py /path/to/pdf/folder
```

### Example Session

```
$ python main.py ~/Documents/protected-pdfs
Processing PDFs: 100%|████████████████| 5/5 [00:15<00:00]
2025-01-15 10:30:15 - INFO - Processing encrypted file: document.pdf
Enter password: ********
2025-01-15 10:30:20 - INFO - Successfully unlocked: document.unlocked.pdf
```

### Output

- Unlocked files are saved as `<original-name>.unlocked.pdf` in the same directory
- Original files are never modified
- Already-unlocked files are skipped automatically

## How It Works

1. Scans the target directory for `.pdf` files
2. Attempts to open each PDF without a password
3. If encrypted, prompts for password (input hidden)
4. Creates unlocked version with `.unlocked.pdf` suffix
5. Verifies the unlocked file can be opened successfully

## Dependencies

- [pikepdf](https://pikepdf.readthedocs.io/) - PDF manipulation
- [tqdm](https://tqdm.github.io/) - Progress bars

## License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with the help of Claude AI</sub>
</div>
