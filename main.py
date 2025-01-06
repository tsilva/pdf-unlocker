import os
import argparse
import logging
from getpass import getpass
from PyPDF2 import PdfReader, PdfWriter
from contextlib import contextmanager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@contextmanager
def temp_file(path):
    try:
        yield path
    finally:
        if os.path.exists(path):
            os.remove(path)

def unlock_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    if not reader.is_encrypted:
        logger.info("File is not encrypted")
        return True

    temp_path = output_path + '.tmp'
    while True:
        try:
            with temp_file(temp_path):
                reader.decrypt(getpass("Enter password: "))
                
                writer = PdfWriter()
                writer.append_pages_from_reader(reader)
                
                with open(temp_path, "wb") as f:
                    writer.write(f)
                
                if PdfReader(temp_path).is_encrypted:
                    raise ValueError("Verification failed - password might be incorrect")
                
                os.rename(temp_path, output_path)
                return True
                
        except Exception as e:
            logger.error(f"Failed to unlock: {e}")
            if input("Would you like to try again? [Y/n]: ").lower() in ['n', 'no']:
                logger.info("Skipping file at user request")
                return False

def batch_remove_password(input_dir):
    for pdf in (f for f in os.listdir(input_dir) if f.endswith(".pdf")):
        input_path = os.path.join(input_dir, pdf)
        output_path = os.path.join(input_dir, f"{os.path.splitext(pdf)[0]}.unlocked.pdf")

        if os.path.exists(output_path):
            logger.info(f"Skipping {pdf}: unlocked version already exists")
            continue

        logger.info(f"Processing: {pdf}")
        try:
            if unlock_pdf(input_path, output_path):
                logger.info(f"Successfully unlocked: {output_path}")
        except Exception as e:
            logger.error(f"Failed to process {pdf}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Batch remove passwords from PDF files')
    parser.add_argument('input_dir', help='Directory containing protected PDF files')
    batch_remove_password(parser.parse_args().input_dir)

if __name__ == "__main__":
    main()
