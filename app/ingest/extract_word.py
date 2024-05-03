
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

import docx2txt

import logging
import os
import os.path

import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

import pandas as pd
from pandas.core.frame import DataFrame
from PyPDF2 import PdfReader

import settings


INPUT_DIR = "confidential-data"
OUTPUT_DIR = "confidential-output"


def _loop_extract_text_info_word(filename: str) -> str:
    text = docx2txt.process(filename)

    return text