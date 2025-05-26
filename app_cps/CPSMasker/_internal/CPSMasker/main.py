import argparse
import os
import platform
from pathlib import Path

from xlib import appargs as lib_appargs
from xlib import os as lib_os



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    run_parser = subparsers.add_parser( "run", help="Run the application.")
    run_subparsers = run_parser.add_subparsers()

    def run_DeepFaceLive(args):
        userdata_path = Path(args.userdata_dir)
        lib_appargs.set_arg_bool('NO_CUDA', args.no_cuda)

        print('Running CPS Masker...\n')
        print(f"{' ' * 3}{' ' * 1}.d8888b.{' ' * 2}8888888b.{' ' * 3}.d8888b.{' ' * 7}888b{' ' * 5}d888{' ' * 19}888")
        print(f"{' ' * 3}d88P{' ' * 2}Y88b{' ' * 1}888{' ' * 3}Y88b{' ' * 1}d88P{' ' * 2}Y88b{' ' * 6}8888b{' ' * 3}d8888{' ' * 19}888")
        print(f"{' ' * 3}888{' ' * 4}888{' ' * 1}888{' ' * 4}888 Y88b.{' ' * 11}88888b.d88888{' ' * 19}888")
        print(f"{' ' * 3}888{' ' * 8}888{' ' * 3}d88P{' ' * 2}\"Y888b.{' ' * 8}888Y88888P888{' ' * 2}8888b.{' ' * 2}.d8888b{' ' * 2}888{' ' * 2}888{' ' * 2}.d88b.{' ' * 2}888d888")
        print(f"{' ' * 3}888{' ' * 8}8888888P\"{' ' * 6}\"Y88b.{' ' * 6}888{' ' * 1}Y888P{' ' * 1}888{' ' * 5}\"88b{' ' * 1}88K{' ' * 6}888{' ' * 1}.88P{' ' * 1}d8P{' ' * 2}Y8b{' ' * 1}888P\"")
        print(f"{' ' * 3}888{' ' * 4}888{' ' * 1}888{' ' * 14}\"888{' ' * 6}888{' ' * 2}Y8P{' ' * 2}888{' ' * 1}.d888888{' ' * 1}\"Y8888b.{' ' * 1}888888K{' ' * 2}88888888{' ' * 1}888")
        print(f"{' ' * 3}Y88b{' ' * 2}d88P{' ' * 1}888{' ' * 8}Y88b{' ' * 2}d88P{' ' * 6}888{' ' * 4}\"{' ' * 2}888{' ' * 1}888{' ' * 2}888{' ' * 6}X88{' ' * 1}888{' ' * 1}\"88b{' ' * 1}Y8b.{' ' * 5}888")
        print(f"{' ' * 3}{' ' * 1}\"Y8888P\"{' ' * 2}888{' ' * 9}\"Y8888P\"{' ' * 7}888{' ' * 7}888{' ' * 1}\"Y888888{' ' * 2}88888P'{' ' * 1}888{' ' * 2}888{' ' * 2}\"Y8888{' ' * 2}888")
        from apps.DeepFaceLive.DeepFaceLiveApp import DeepFaceLiveApp
        DeepFaceLiveApp(userdata_path=userdata_path).run()

    p = run_subparsers.add_parser('DeepFaceLive')
    p.add_argument('--userdata-dir', default=None, action=fixPathAction, help="Workspace directory.")
    p.add_argument('--no-cuda', action="store_true", default=False, help="Disable CUDA.")
    p.set_defaults(func=run_DeepFaceLive)

    dev_parser = subparsers.add_parser("dev")
    dev_subparsers = dev_parser.add_subparsers()

    def run_split_large_files(args):
        from scripts import dev
        dev.split_large_files()

    p = dev_subparsers.add_parser('split_large_files')
    p.set_defaults(func=run_split_large_files)

    def run_merge_large_files(args):
        from scripts import dev
        dev.merge_large_files(delete_parts=args.delete_parts)

    p = dev_subparsers.add_parser('merge_large_files')
    p.add_argument('--delete-parts', action="store_true", default=False)
    p.set_defaults(func=run_merge_large_files)

    def run_extract_FaceSynthetics(args):
        from scripts import dev

        inputdir_path = Path(args.input_dir)
        faceset_path = Path(args.faceset_path)

        dev.extract_FaceSynthetics(inputdir_path, faceset_path)

    p = dev_subparsers.add_parser('extract_FaceSynthetics')
    p.add_argument('--input-dir', default=None, action=fixPathAction, help="FaceSynthetics directory.")
    p.add_argument('--faceset-path', default=None, action=fixPathAction, help="output .dfs path")
    p.set_defaults(func=run_extract_FaceSynthetics)

    train_parser = subparsers.add_parser( "train", help="Train neural network.")
    train_parsers = train_parser.add_subparsers()

    def train_FaceAligner(args):
        lib_os.set_process_priority(lib_os.ProcessPriority.IDLE)
        from apps.trainers.FaceAligner.FaceAlignerTrainerApp import FaceAlignerTrainerApp
        FaceAlignerTrainerApp(workspace_path=Path(args.workspace_dir), faceset_path=Path(args.faceset_path))

    p = train_parsers.add_parser('FaceAligner')
    p.add_argument('--workspace-dir', default=None, action=fixPathAction, help="Workspace directory.")
    p.add_argument('--faceset-path', default=None, action=fixPathAction, help=".dfs path")
    p.set_defaults(func=train_FaceAligner)

    def bad_args(arguments):
        parser.print_help()
        exit(0)
    parser.set_defaults(func=bad_args)

    args = parser.parse_args()
    args.func(args)

class fixPathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

if __name__ == '__main__':
    main()


