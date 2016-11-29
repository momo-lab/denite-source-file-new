# FILE: filter_file_new.py
# AUTHOR: momotaro <momotaro.n@gmail.com>
# License: MIT license

from .base import Base
from os.path import join

class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'filter_file_new'
        self.description = 'filter for file_new source'

    def filter(self, context):
        if context['input'] == '':
            return []

        for candidate in context['candidates']:
            if candidate['word'] == context['input']:
                return []

        return [{
                'word': "%s %s (%s)" % (context['__prompt'], 
                    context['input'], context['__dir']),
                'action__path': join(context['__dir'], context['input']) }]
