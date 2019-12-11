# -*- coding: utf-8 -*-
import glob
import os
from sys import argv
from audio_convertor import Execute
from os.path import dirname, abspath, join
from dotenv import load_dotenv
import logging


def main():
    _load_pr_env()
    # logging
    logging.basicConfig(level=os.environ.get('LOG_LEVEL'))
    logging.info('log level: {}'.format(os.environ.get('LOG_LEVEL')))
    convertor = Execute(os.environ.get('VOICE_ID'), logging)
    guide_files = []

    # コマンドライン引数があった場合、指定されたものだけ実行する
    if len(argv) != 1:
        guide_files += argv[1:len(argv)]
    else:
        guide_file_dir_path = join(dirname(abspath(__file__)),
                                   '..',
                                   'guide_text_data', '*')
        guide_files = glob.glob(guide_file_dir_path)

    logging.info("items: {}".format((guide_files)))
    for guide_file in guide_files:
        logging.info("+++++ execute {} conversion +++++".format(guide_file))
        convertor.convert(guide_file)
        logging.info('complete.')


def _load_pr_env():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


main()
