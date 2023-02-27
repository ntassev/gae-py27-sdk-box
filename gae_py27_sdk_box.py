import zipfile
import sys
import os
import tempfile
import shutil


def unbox_and_add_to_path():
    zip_path = os.path.join(sys.prefix, 'gae-py27-sdk-box/py27-gae-sdk-stipped.zip')
    target_path = tempfile.mkdtemp()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_path)

    py27_gae_sdk_path = os.path.join(target_path, 'py27-gae-sdk')
    sys.path.append(py27_gae_sdk_path)

    return target_path


def recycle_box(target_path):
    shutil.rmtree(target_path)
