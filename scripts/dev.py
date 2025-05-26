from pathlib import Path

import numpy as np
from xlib import console as lib_con
from xlib import face as lib_face
from xlib import path as lib_path
from xlib.file import SplittedFile
from xlib import cv as lib_cv

repo_root = Path(__file__).parent.parent
large_files_list = [ (repo_root / 'modelhub' / 'onnx' / 'S3FD' / 'S3FD.onnx', 48*1024*1024),
                     (repo_root / 'modelhub' / 'onnx' / 'LIA' / 'generator.onnx', 48*1024*1024),
                     (repo_root / 'modelhub' / 'onnx' / 'InsightFaceSwap' / 'inswapper_128.onnx', 48*1024*1024),
                     (repo_root / 'modelhub' / 'onnx' / 'InsightFaceSwap' / 'w600k_r50.onnx', 48*1024*1024),
                     (repo_root / 'modelhub' / 'torch' / 'S3FD' / 'S3FD.pth', 48*1024*1024),
                     (repo_root / 'modelhub' / 'cv' / 'FaceMarkerLBF' / 'lbfmodel.yaml', 34*1024*1024),
                    ]

def merge_large_files(delete_parts=False):
    for filepath, _ in large_files_list:
        print(f'Merging {filepath}...')
        SplittedFile.merge(filepath, delete_parts=delete_parts)
    print('Done')

def split_large_files(delete_original=False):
    for filepath, part_size in large_files_list:
        print(f'Splitting {filepath}...')
        if filepath.exists():
            SplittedFile.split(filepath, part_size=part_size, delete_original=delete_original)
        else:
            print(f'{filepath} not found. Skipping.')

    print('Done')

def extract_FaceSynthetics(inputdir_path : Path, faceset_path : Path):

    if faceset_path.suffix != '.dfs':
        raise ValueError('faceset_path must have .dfs extension.')

    filepaths = lib_path.get_files_paths(inputdir_path)
    fs = lib_face.Faceset(faceset_path, write_access=True, recreate=True)
    for filepath in lib_con.progress_bar_iterator(filepaths, desc='Processing'):
        if filepath.suffix == '.txt':

            image_filepath = filepath.parent / f'{filepath.name.split("_")[0]}.png'
            if not image_filepath.exists():
                print(f'{image_filepath} does not exist, skipping')


            img = lib_cv.imread(image_filepath)
            H,W,C = img.shape

            lmrks = []
            for lmrk_line in filepath.read_text().split('\n'):
                if len(lmrk_line) == 0:
                    continue

                x, y = lmrk_line.split(' ')
                x, y = float(x), float(y)

                lmrks.append( (x,y) )

            lmrks = np.array(lmrks[:68], np.float32) / (H,W)

            flmrks = lib_face.FLandmarks2D.create(lib_face.ELandmarks2D.L68, lmrks)

            uimg = lib_face.UImage()
            uimg.assign_image(img)
            uimg.set_name(image_filepath.stem)

            ufm = lib_face.UFaceMark()
            ufm.set_UImage_uuid(uimg.get_uuid())
            ufm.set_FRect(flmrks.get_FRect())
            ufm.add_FLandmarks2D(flmrks)

            fs.add_UFaceMark(ufm)
            fs.add_UImage(uimg, format='png')

    fs.optimize()
    fs.close()


