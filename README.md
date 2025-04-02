# 🔓 pdf-unlocker

<p align="center">
  <img src="logo.jpg" alt="PDF Unlocker Logo" width="400"/>
</p>

> A handy Python tool to batch unlock password-protected PDFs while keeping your originals safe.

## ✨ Features

- 🔍 Detects encrypted PDFs
- 🔐 Interactive password prompting
- ⚡ Progress tracking with a progress bar
- ✅ Unlock verification
- 🛡️ Original files remain untouched
- 📁 Clean file organization with `.unlocked.pdf` suffix

## 🛠️ Installation

```bash
git clone https://github.com/tsilva/pdf-unlocker.git
cd pdf-unlocker
curl -L https://gist.githubusercontent.com/tsilva/258374c1ba2296d8ba22fffbf640f183/raw/venv-install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

```bash
curl -L https://gist.githubusercontent.com/tsilva/8588cb367242e3db8f1b33c42e4e5e06/raw/venv-run.sh -o run.sh && chmod +x run.sh && ./run.sh
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

## 📄 License

This project was developed in collaboration with the `claude-3.5-sonnet` AI assistant and is made available under the [MIT License](LICENSE).
