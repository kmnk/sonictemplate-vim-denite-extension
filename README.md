# sonictemplate-vim-denite-extension
[denite.nvim][denite] source and kind of [sonictemplate-vim][sonictemplate]

## Requirements
- [Neovim][neovim]
- [denite.nvim][denite]
- [sonictemplate-vim][sonictemplate]

## Install by dein
Add `kmnk/sonictemplate-vim-denite-extension` repository to your `dein.toml` file.

```
[[plugins]]
repo = 'kmnk/sonictemplate-vim-denite-extension'
depends = ['mattn/sonictemplate-vim']
```

## Usage
Execute `:Denite` command with source name `sonictemplate` .
And select template name you want to apply.

```
:Denite sonictemplate
```

[neovim]:https://neovim.io/
[denite]:https://github.com/Shougo/denite.nvim
[sonictemplate]:https://github.com/mattn/sonictemplate-vim
