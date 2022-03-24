#!/usr/bin/env python3
import json
import subprocess
import tempfile
import os
from ingredient_parser import utils
from ingredient_parser import tokenizer
import pprint as pp

def _exec_crf_test(input_text, model_path):
    with tempfile.NamedTemporaryFile(mode='w') as input_file:
        input_file.write(utils.export_data(input_text))
        input_file.flush()
        return subprocess.check_output(
            ['crf_test', '--verbose=1', '--model', model_path,
             input_file.name]).decode('utf-8')


def _convert_crf_output_to_json(crf_output):
    return utils.import_data(crf_output)
    # return json.dumps(utils.import_data(crf_output), indent=2, sort_keys=True)


def parse_ingredients(ingredient_strs):
    """
    Takes a list of ingredients and returns a json containing the parsed ingredient names, quantities and units
    """
    cwd = os.getcwd()
    model_path = cwd + '/objects/ingredient_parser/model.crfmodel'
    crf_output = _exec_crf_test(ingredient_strs, model_path)
    return(_convert_crf_output_to_json(crf_output.split('\n')))

if __name__ == '__main__':
    ingredient_strs = ['0.75 kg ground beef', '300 pounds eggs']
    parse_ingredients(ingredient_strs)
