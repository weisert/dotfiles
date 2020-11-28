" ---------------------------------- OPTIONS ---------------------------------
" Show line numbers
set number

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
map <F3> "ay
map <F4> "ap
map <F5> "by
map <F6> "bp

" Use magic regex syntax by default
nnoremap / /\v

" Tab related keys
noremap <M-Up> :tabr<CR>
noremap <M-Down> :tabl<CR>
noremap <M-Left> :tabp<CR>
noremap <M-Right> :tabn<CR>

" --------------------------------- AUTO COMMANDS ----------------------------

let g:help_in_tabs = 1

" Open help full screen
augroup HelpInTabs
    autocmd!
    autocmd BufEnter *.txt call HelpInNewTab()
augroup END

"Only apply to help files...
function! HelpInNewTab ()
    if &buftype == 'help' && g:help_in_tabs
        "Convert the help window to a tab...
        execute "normal \<C-W>T"
    endif
endfunction

