# sonictemplate.py
"""
denite.nvim kind: sonictemplate
"""

from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sonictemplate'
        self.default_action = 'apply'

    def action_apply(self, context):
        '''
        渡された template を sonictemplate#apply を介して適用する
        '''
        self.vim.call('sonictemplate#apply',
                      context['targets'][0]['action__name'],
                      context['targets'][0]['action__mode'])

def main(): pass

if __name__ == '__main__': main()
