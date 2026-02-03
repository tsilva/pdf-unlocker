import os
import argparse
import logging
from getpass import getpass
import pikepdf
from contextlib import contextmanager
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

def try_unlock_with_password(input_path, temp_path, password):
    pdf = pikepdf.open(input_path, password=password)
    pdf.save(temp_path)
    pikepdf.open(temp_path)  # Verify unlock worked
    return True

def process_single_attempt(input_path, temp_path, output_path):
    password = getpass("Enter password: ")
    if not try_unlock_with_password(input_path, temp_path, password):
        return False
    
    os.rename(temp_path, output_path)
    logger.info(f"Successfully unlocked: {os.path.basename(output_path)}")
    return True

def unlock_pdf(input_path, output_path):
    # Try without password first
    try:
        pikepdf.open(input_path)
        return False
    except pikepdf.PasswordError:
        pass

    temp_path = output_path + '.tmp'
    logger.info(f"Processing encrypted file: {os.path.basename(input_path)}")

    while True:
        try:
            if process_single_attempt(input_path, temp_path, output_path):
                return True
        except Exception as e:
            logger.error(f"Failed to unlock: {e}")
            remove_if_exists(temp_path)
            
            if input("Would you like to try again? [Y/n]: ").lower() in ['n', 'no']:
                logger.info("Skipping file at user request")
                return False

def get_pdf_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".pdf")]

def process_pdf(input_dir, pdf_name, pbar):
    input_path = os.path.join(input_dir, pdf_name)
    output_path = os.path.join(input_dir, f"{os.path.splitext(pdf_name)[0]}.unlocked.pdf")
    pbar.set_postfix_str(pdf_name)

    if os.path.exists(output_path):
        logger.info(f"Skipping {pdf_name}: unlocked version already exists")
        return

    unlock_pdf(input_path, output_path)

def batch_remove_password(input_dir):
    pdf_files = get_pdf_files(input_dir)
    with tqdm(pdf_files, desc="Processing PDFs", unit="file") as pbar:
        for pdf in pbar:
            process_pdf(input_dir, pdf, pbar)

def main():
    parser = argparse.ArgumentParser(description='Batch remove passwords from PDF files')
    parser.add_argument('input_dir', help='Directory containing protected PDF files')
    batch_remove_password(parser.parse_args().input_dir)

if __name__ == "__main__":
    main()
