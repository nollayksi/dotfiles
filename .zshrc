# Enable colors and change prompt:
autoload -U colors && colors	# Load colors
PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}$%b "

# Defaults 
export VISUAL=nvim
export EDITOR=nvim
export BROWSER=firefox

# setopt no_list_ambiguous
# setopt MENU_COMPLETE


# Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh/.histfile
HISTSIZE=10000
SAVEHIST=10000
setopt autocd extendedglob nomatch notify
unsetopt beep
bindkey -v
stty stop undef		# Disable ctrl-s to freeze terminal.
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/vili/.zshrc' 

autoload -Uz compinit
# Basic case-insensitive auto/tab complete:
# zstyle ':completion:*'  menu select matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' menu select matcher-list 'm:{a-z}={A-Z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/shortcutrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/shortcutrc"
[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/aliasrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/aliasrc"
[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/zshnameddirrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/zsh/zshnameddirrc"

# Fix ctrl + arrow and del char 
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "^[[3~" delete-char
bindkey "^[[3;5~" delete-word
bindkey "^H" backward-delete-word
bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line


# Load syntax highlighting; should be last.
source /usr/share/zsh/plugins/fsh/fast-syntax-highlighting.plugin.zsh 2>/dev/null
