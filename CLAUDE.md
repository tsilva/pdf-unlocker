# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pdf-unlocker is a Python tool for batch unlocking password-protected PDFs. The tool processes a directory of PDFs, detects encrypted files, prompts for passwords interactively, and creates unlocked versions with a `.unlocked.pdf` suffix while preserving the original files.

## Core Architecture

This is a single-file Python application (`main.py`) with a straightforward workflow:

1. **PDF Discovery**: Scans directory for `.pdf` files
2. **Encryption Detection**: Attempts to open each PDF without a password using `pikepdf`
3. **Interactive Unlocking**: If encrypted, prompts user for password with retry logic
4. **Safe Output**: Creates `.unlocked.pdf` files with temporary `.tmp` files during processing to ensure atomicity

The application uses `pikepdf` for PDF manipulation and `tqdm` for progress tracking. All unlocking happens in-place within the source directory.

## Development Commands

### Setup
```bash
# Using pip
pip install -r requirements.txt

# Using conda
conda env create -f environment.yml
conda activate pdf-unlocker
```

### Running the Tool
```bash
# Basic usage
python main.py /path/to/pdf/folder

# Example
python main.py ~/Documents/protected-pdfs
```

### Testing Manually
Since this tool requires interactive password input and operates on actual PDF files, manual testing involves:
1. Creating a test directory with password-protected PDFs
2. Running the tool and verifying:
   - Non-encrypted PDFs are skipped
   - Encrypted PDFs prompt for passwords
   - Correct passwords create `.unlocked.pdf` files
   - Incorrect passwords allow retry or skip
   - Original files remain unchanged

## Key Implementation Details

- **Password Handling**: Uses `getpass` for secure password input (not echoed to terminal)
- **Error Recovery**: Failed unlock attempts clean up temporary files and offer retry
- **Idempotency**: Skips PDFs that already have `.unlocked.pdf` versions
- **Verification**: After unlocking, attempts to open the output file to verify success
- **Logging**: Structured logging with timestamps for debugging and monitoring

## Future Roadmap

See TODO.md - the project is planned to be converted into a command-line tool installable via pipx.

## Project Maintenance

README.md must be kept up to date with any significant project changes, including new features, installation methods, or usage patterns.
