
import glob
import os

import img2pdf #pip install img2pdf
from natsort import natsorted #pip install natsort


filename = 'ASME B107.17 - Gages and Mandrels for Wrench Openings.pdf'
file_list = glob.glob('*.png')

with open(filename, "wb") as f:
    f.write(img2pdf.convert(natsorted(file_list)))










