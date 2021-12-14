" ---------------------------------- OPTIONS ---------------------------------
" Show line numbers
set number

" Set relative line number
set relativenumber

" Show syntax highlighting
syntax enable

" Show ruler at column 80
set colorcolumn=80

" Expand tabs
set expandtab

" tab size
set tabstop=2

" Shift width
set shiftwidth=2

" Highlight search result
set hlsearch

" Incremental search
set incsearch

" Use case insensitive search
set ignorecase

" Use partial sensitivity
set smartcase

" Match all types of brackets by % command
set matchpairs=(:),{:},[:],<:>

" Show position of the file
set ruler

" Set backspace behavior
set backspace=indent,eol,start

" Use of persistent undo
if has('persistent_undo')
    " Save all undo files in a single location (less messy, more risky)...
    set undodir=$HOME/.VIM_UNDO_FILES

    " Save a lot of back-history...
    set undolevels=5000

    " Actually switch on persistent undo
    set undofile

endif

" Filename autocompletion
set wildmode=list:longest,full

" History length
set history=10000

" Allow hidden buffers
set hidden

" Set invisible characters behavior
" Toggle `set list`
nmap <leader>l :set list!<CR>
" Symbols for tabstops and EOLs
set listchars=tab:▸\ ,eol:¬

" Always show status line
set laststatus=2

" --------------------------------- MAPPINGS ---------------------------------
" Hide search highlight
map <F2> :noh<CR>

" PRIMARY (copy-on-select) register mappings
noremap <Leader>Y "*y
noremap <Leader>P "*p

" CLIPBOARD (CTRL-C) register mappings
noremap <Leader>y "+y
noremap <Leader>p "+p

" Replace word under cursor
noremap <Leader>s :%s/\<<C-r><C-w>\>//g<Left><Left>

" One key use of a and b registers
map <Leader><F3> "wy
map <F3> "wp
map <Leader><F4> "xy
map <F4> "xp
map <Leader><F5> "yy
map <F5> "yp
map <Leader><F6> "zy
map <F6> "zp

" One key replay macros
map <F7> @a
map <F8> @b

" Use magic regex syntax by default
nnoremap / /\v
nnoremap ? ?\v

" Tab related keys
noremap <M-Up> :tabr<CR>
noremap <M-Down> :tabl<CR>
noremap <M-Left> :tabp<CR>
noremap <M-Right> :tabn<CR>

" Buffer related commmands
noremap <C-Up> :bfirst<CR>
noremap <C-Down> :blast<CR>
noremap <C-Left> :bprevious<CR>
noremap <C-Right> :bnext<CR>
nmap <leader>Q :bufdo bdelete<CR>

" Faster windows switching
nmap <silent> <C-h> <C-w>h
nmap <silent> <C-j> <C-w>j
nmap <silent> <C-k> <C-w>k
nmap <silent> <C-l> <C-w>l

" Reflect visual selection after indenting
vnoremap < <gv
vnoremap > >gv

" Allow gf to open non-existent files
map gf :edit <cfile><CR>

" Open current file in the default program
nmap <leader>x :!xdg-open %<CR><CR>

" Expand path relatively the file opened in the current buffer
cnoremap <expr> %% getcmdtype() == ':' ? expand('%:h').'/' : '%%'

" Fix & command behavior
nnoremap & :&&<CR>
xnoremap & :&&<CR>

" Toggle nerdtree window
map <Leader>t :NERDTreeToggle<CR>

" Find current file in the filesystem
map <Leader>r :NERDTreeFind<CR>

" --------------------------------- AUTO COMMANDS ----------------------------

let g:help_in_tabs = 1

" Open help full screen
augroup HelpInTabs
    autocmd!
    autocmd BufEnter *.txt call HelpInNewTab()
augroup END

" Only apply to help files...
function! HelpInNewTab ()
    if &buftype == 'help' && g:help_in_tabs
        "Convert the help window to a tab...
        execute "normal \<C-W>T"
    endif
endfunction

" Use F12 to run flake8
autocmd FileType python map <buffer> <F12> :call flake8#Flake8()<CR>

" --------------------------------- PLUGINS ----------------------------------
set nocompatible
filetype plugin on

" Install vim-plug using the following shell command:
" $ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
" >   https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

call plug#begin()
  Plug 'adelarsq/vim-matchit'
  Plug 'avakarev/vim-watchdog'
  Plug 'easymotion/vim-easymotion'
  Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
  Plug 'kana/vim-textobj-entire'
  Plug 'kana/vim-textobj-user'
  Plug 'mg979/vim-visual-multi'
  Plug 'nvie/vim-flake8'
  Plug 'preservim/nerdtree'
  Plug 'tpope/vim-abolish'
  Plug 'tpope/vim-commentary'
  Plug 'tpope/vim-repeat'
  Plug 'tpope/vim-surround'
  Plug 'vim-scripts/ReplaceWithRegister'
  Plug 'vim-scripts/argtextobj.vim'
  Plug 'wincent/terminus'
call plug#end()

