import shutil
import sys


def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)
    print(f"File copied from {source_path} to {destination_path}.")


copy_file(sys.argv[1], sys.argv[2])
# SHOULD BE RUN LIKE THIS:
# python -u "/home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t2.py" /home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t1.py /home/bilal/Documents/UMT/semmester5/code/AI/AI/
# File copied from /home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t1.py to /home/bilal/Documents/UMT/semmester5/code/AI/AI/.
