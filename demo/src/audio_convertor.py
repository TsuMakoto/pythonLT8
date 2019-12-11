# -*- coding: utf-8 -*-
import os
from os.path import join, dirname, abspath, splitext, basename
from contextlib import closing
import sys
from boto3 import Session


class Execute:
    def __init__(self, voice_id, logging):
        self.voice_id = voice_id
        self.lexicon_name = os.environ.get('LEXICON_NAME')
        session = Session(profile_name=os.environ.get('PROFILE_NAME'))
        self.polly = session.client("polly")
        self.logging = logging

    def convert(self, guide_file_path, output_format='mp3'):
        input_file_name = basename(guide_file_path)
        file_name = splitext(input_file_name)[0]
        output_file_name = "{}.{}".format(file_name, output_format)
        guide_contents = self._load_guide_data(guide_file_path)

        self.logging.info(
            "start convert {} >>>>>> {}"
            .format(input_file_name, output_file_name))

        print(self.lexicon_name)
        # Request speech synthesis
        response = self.polly.synthesize_speech(
            Engine=os.environ.get('ENGINE'),
            LanguageCode=os.environ.get('LANGUAGE_CODE'),
            LexiconNames=[
                self.lexicon_name,
            ],
            TextType=os.environ.get('TEXT_TYPE'),
            Text=guide_contents,
            OutputFormat=output_format,
            VoiceId=self.voice_id)

        if 'AudioStream' in response:
            self.logging.info('OK')
            with closing(response["AudioStream"]) as stream:
                output = join(
                    dirname(abspath(__file__)), '..', 'tmp', output_file_name)
                self.logging.info('writing {}'.format(output))
                try:
                    with open(output, 'wb') as file:
                        file.write(stream.read())
                        self.logging.info('OK')
                except IOError as error:
                    self.logging.error("write error: {} ... NG".format(error))
                    sys.exit(-1)
        else:
            self.logging.error("response error: Could not stream audio ... NG")
            sys.exit(-1)

# private

    def _load_guide_data(self, file_path):

        self.logging.info("loading {}".format(file_path))
        try:
            with open(file_path) as file:
                data = file.read()
                self.logging.info('OK')
        except IOError as error:
            self.logging.error("load error: {} ... NG".format(error))
            sys.exit(-1)

        return data
