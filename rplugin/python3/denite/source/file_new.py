# FILE: file_new.py
# AUTHOR: momotaro <momotaro.n@gmail.com>
# License: MIT license

from .base import Base
import os

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'file_new'
        self.kind = 'file'
        self.matchers = ['filter_file_new']

    def on_init(self, context):
        directory = context['args'][0] if len(
            context['args']) > 0 else context['path']
        directory = self.vim.call('expand', directory)
        context['__candidates'] = os.listdir(directory)

    def gather_candidates(self, context):
        candidates = context['__candidates']
        return list(map(
            lambda candidate: {
                'word': os.path.basename(candidate)
            }, candidates))

