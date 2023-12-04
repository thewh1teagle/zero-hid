from typing import List

from .hid.keyboard import send_keystroke, release_keys
from .hid.keycodes import KeyCodes
from . import defaults
from time import sleep
import json
import operator
from functools import reduce
import pkgutil
import os
import pathlib

class Keyboard:
    
    def __init__(self, dev=defaults.KEYBOARD_PATH) -> None:
        if not hasattr(dev, 'write'): # check if file like object
            self.dev = open(dev, 'ab+')
        else:
            self.dev = dev
        self.set_layout()
    
    def list_layout(self):
        keymaps_dir = pathlib.Path(__file__).parent.absolute() / 'keymaps'
        keymaps = os.listdir(keymaps_dir)
        files = [f for f in keymaps if f.endswith('.json')]
        for count, fname in enumerate(files, 1):
            with open(keymaps_dir / fname , encoding='UTF-8') as f:
                content = json.load(f)
                name, desc = content['Name'], content['Description']
            print(f'{count}. {name}: {desc}') 
        
        
    def set_layout(self,  language='US'):
        self.layout = json.loads( pkgutil.get_data(__name__, f"keymaps/{language}.json").decode() )
    
    def type(self, text, delay=0):
        for c in text:
            key_map = self.layout['Mapping'][c]
            key_map = key_map[0]
            mods = key_map['Modifiers']
            keys = key_map['Keys']
            mods = [KeyCodes[i] for i in mods]
            keys = [KeyCodes[i] for i in keys]
            
            if len(mods) == 1:
                mods = mods[0]
            else:
                mods = reduce(operator.and_, mods, 0)
            send_keystroke(self.dev, mods, keys[0])
            sleep(delay)

    def press(self, mods: List[int], key_code: int = 0, release=True):
        if len(mods) == 1:
            mods = mods[0]
        else:
            mods = reduce(operator.and_, mods, 0)
        send_keystroke(self.dev, mods, key_code, release=release)

    def release(self):
        release_keys(self.dev)
    
            
    def __enter__(self):
        return self


    def _clean_resources(self):
        self.dev.close()    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clean_resources()
        
    
    def close(self):
        self._clean_resources()

