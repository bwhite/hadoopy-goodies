"""Takes a directory of files and puts them in one large file.

Format: (file_name, file_data) ordered by file_name, field delimited by tabs,
    record delimited by newlines.
    file_name: path removed so './mypath/file.txt' would produce 'file.txt'.
    file_data: complete b64'd contents of the file.

Usage:
python files_to_b64.py <input_path> <output_path>
"""

import base64
import glob
import os
import sys
import time


def main(input_path, output_path):
    with open(output_path, 'w') as out_fp:
        in_fns = sorted(glob.glob(input_path + '/*'))
        ut = st = time.time()
        for num, in_fn in enumerate(in_fns):
            if time.time() - ut > 5.:
                ct = ut = time.time()
                pct_done = num / float(len(in_fns))
                time_left = (ct - st) * (1. / pct_done - 1.)
                print('%d/%d=%f Done in %f sec.' % (num, len(in_fns), pct_done, time_left))
            out_fp.write(os.path.basename(in_fn) + '\t')
            with open(in_fn) as in_fp:
                out_fp.write(base64.b64encode(in_fp.read()))
                out_fp.write('\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    main(*sys.argv[1:])
