# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pdf-password-remover is a Python CLI tool for batch removing passwords from protected PDFs. The tool processes a directory of PDFs, detects encrypted files, prompts for passwords interactively, and creates unlocked versions with a `.unlocked.pdf` suffix while preserving the original files.

## Core Architecture

This is a Python package with a CLI entry point:

- `pdf_password_remover/cli.py` - Main CLI logic and PDF processing workflow
- `pdf_password_remover/__init__.py` - Package metadata and version

Workflow:
1. **PDF Discovery**: Scans directory for `.pdf` files
2. **Encryption Detection**: Attempts to open each PDF without a password using `pikepdf`
3. **Interactive Unlocking**: If encrypted, prompts user for password with retry logic
4. **Safe Output**: Creates `.unlocked.pdf` files with temporary `.tmp` files during processing to ensure atomicity

The application uses `pikepdf` for PDF manipulation and `tqdm` for progress tracking. All unlocking happens in-place within the source directory.

## Development Commands

### Setup
```bash
# Install with uv (recommended)
uv pip install -e .

# Or install globally with uv tool
uv tool install .

# Or using pip
pip install -e .
```

### Running the Tool
```bash
# After installation
pdf-password-remover /path/to/pdf/folder

# Or run directly with uv
uv run pdf-password-remover /path/to/pdf/folder

# Example
pdf-password-remover ~/Documents/protected-pdfs
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

## Project Maintenance

README.md must be kept up to date with any significant project changes, including new features, installation methods, or usage patterns.
