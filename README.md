# 🔓 PDF Unlocker

<p align="center">
  <img src="logo.jpg" alt="PDF Unlocker Logo" width="400"/>
</p>

> 🚀 A lightning-fast Python tool that batch unlocks password-protected PDFs while keeping your originals safe.

## ✨ Features

- 🔍 Smart detection of encrypted PDFs
- 🔐 Interactive password prompting
- ⚡ Parallel processing with progress tracking
- ✅ Built-in unlock verification
- 🛡️ Original files remain untouched
- 📁 Clean file organization with `.unlocked.pdf` suffix

## 🛠️ Installation

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

## 📝 Usage

Just point it to your PDF directory:

```bash
python main.py /path/to/pdf/folder
```

## 🎯 Example

```bash
$ python main.py ~/Documents/protected-pdfs
2023-08-15 10:30:15 - INFO - Processing: document.pdf
Enter password: ********
2023-08-15 10:30:20 - INFO - Successfully unlocked: document.unlocked.pdf
```

## 🤝 Contributing

Found a bug or want to contribute? PRs are welcome!

## 📄 License

This project was developed in collaboration with the `claude-3.5-sonnet` AI assistant and is made available under the [MIT License](LICENSE).
