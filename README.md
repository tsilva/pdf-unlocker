# pdf-unlocker

<p align="center">
  <img src="logo.jpg" alt="PDF Unlocker Logo" width="400"/>
</p>

A Python command-line tool to batch unlock password-protected PDFs by scanning directories, prompting for passwords, and creating unlocked copies while preserving originals.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tsilva/pdf-unlocker
cd pdf-unlocker
```

2. Create conda environment:
```bash
conda env create -f environment.yml
conda activate pdf-unlocker
```

## Usage

Run the script by providing the directory containing your password-protected PDFs:

```bash
python main.py /path/to/pdf/folder
```

The script will:
- Process all PDF files in the specified directory
- Prompt for passwords when needed
- Create unlocked versions with `.unlocked.pdf` suffix
- Skip already processed files
- Verify successful unlocking

## Example

```bash
$ python main.py ~/Documents/protected-pdfs
2023-08-15 10:30:15 - INFO - Processing: document.pdf
Enter password: ********
2023-08-15 10:30:20 - INFO - Successfully unlocked: document.unlocked.pdf
```

## License

This project was developed in collaboration with the `claude-3.5-sonnet` and is made available under the [MIT License](LICENSE).