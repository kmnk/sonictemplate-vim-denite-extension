# sonictemplate.py
"""
denite.nvim source: sonictemplate
"""

from denite.source.base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sonictemplate'
        self.kind = 'sonictemplate'

    def gather_candidates(self, context):
        '''
        sonicetemplate#complete 関数を介して template の候補を取得し、整形して返す
        '''
        return [{
            'word': v,
            'action__mode': 'n', # source から起動されるので normal mode 固定
            'action__name': v,
        } for v in self.vim.call('sonictemplate#complete', '', '', 0)]

def main(): pass

if __name__ == '__main__': main()
