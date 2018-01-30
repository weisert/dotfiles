alias CDT='export PATH=$PATH:$HOME/projects/chromium/depot_tools'
alias YDT='export PATH=$PATH:$HOME/projects/y_depot_tools'

alias ll='ls -lah'
alias ggrep='git grep -n'
alias gls='git ls-files'

# Chromium build
case "$(uname)" in
   Darwin*) PREFIX="" ;;
   Linux*)  PREFIX="" ;;
   *)       PREFIX="winpty" ;;
esac

alias bc='$PREFIX ninja -C out/debug chrome'
alias bu='$PREFIX ninja -C out/debug unit_tests'
alias bb='$PREFIX ninja -C out/debug browser_tests'
alias ba='$PREFIX ninja -C out/debug chrome browser_tests unit_tests components_unittests components_browsertests'
# End Chromium build
