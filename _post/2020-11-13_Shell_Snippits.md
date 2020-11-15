---
blog_heading: Shell Snippits
blog_subheading: 
blog_author: David Lutton
blog_publish_date: 2020/11/14
---
``` bash
find -iname "*.ext" - exec grep -Hi -C 5 'term' "{}" \;
# find ext and grep term, showing filename and 5 lines above and below match

find . -name "\$*" -delete
# find and delete Microsoft Office style temporary files

find . -name "Thumbs.db" -delete
# find and delete Thumbs.db files

qrencode -t UTF8 'String to encode'
# Encode string to QR code

function ..(){ cd .. ; }
function ...(){ cd ../.. ; }
function ....(){ cd ../../.. ; }
function .....(){ cd ../../../.. ; }


function qr(){ qrencode -t ANSI "$@" ; }

# rdfind

function title(){ echo -ne "\033]0;$@\007" ; }
function bashrc(){ . ~/.bashrc }
function avahi(){ avahi-browse -at "$@" }


function gh(){ git clone "git://github.com/$@" }

function lh(){ ls -lhs ; }

function mkcd(){
# mkdir, cd into it
mkdir -p "$*"
cd "$*"
}
function mkdircd(){ mkdir -p $@ && cd $@ ; }
function sayit(){ echo $@ | espeak -s 140 -v en-uk-rp --stdout | paplay -n espeak ; }

"sudo btrfs subvolume snapshot / /btrfs_$(date +%Y-%m-%d_%H-%M)"


function dum(){ du -h | grep ^[0-9.]*M | sort -rn | head -n 20 ; }
# SRC="https://raymii.org/s/snippets/Arch-bash-pacman-bashrc-tips.html"

function syslogtail() { tail -f -n 50 /var/log/syslog ; }
find . -size 0 -type f  -exec rm \"{}\" -rfv  \;" # Delete zero size files
function dum(){
	du -h | grep ^[0-9.]*M | sort -rn | head -n 20
	# SRC="https://raymii.org/s/snippets/Arch-bash-pacman-bashrc-tips.html"
}

mvprefix(){ mv $1 $2$1 ; }
mvsuffix(){ mv $1 $1$2 ; }


function deup(){
	OUTF=rem-duplicates.sh;
	echo "#! /bin/sh" > $OUTF;
	find "$@" -type f -printf "%s\n" | sort -n | uniq -d |
		xargs -I@@ -n1 find "$@" -type f -size @@c -exec md5sum {} \; |
		sort --key=1,32 | uniq -w 32 -d --all-repeated=separate |
		sed -r 's/^[0-9a-f]*( )*//;s/([^a-zA-Z0-9./_-])/\\\1/g;s/(.+)/#rm \1/' >> $OUTF;
	chmod a+x $OUTF
	ls -l $OUTF
	# SRC="http://elonen.iki.fi/code/misc-notes/remove-duplicate-files/"
}

```

``` bash


#BBLUE='\[\033[1;34m\]'

#BLUE='\[\033[0;34\]'
#NORMAL='\[\033[00m\]'

A='\[\033[0;37m\]' # Gray
B='\[\033[0;36m\]' # Light Blue

Y='\[\033[1;33m\]' # Bright Yellow
G='\[\033[1;32m\]' # Green
R='\[\033[1;31m\]' # Red

N='\[\033[00m\]'
L='─'
U='┌'
D='└'
C="●"
P="$L$L$L$L$L$L$L"
PS1="$B$U$L$N[$R~\u$N]$B$L$N[$Y@\h$N]$B$L$N[$A\T$N]$B$P$N[$Y\w$N]\n$B$D$G>$N"

```

``` bash
#!/bin/bash
txtblk='\e[0;30m' # Black - Regular
txtred='\e[0;31m' # Red
txtgrn='\e[0;32m' # Green
txtylw='\e[0;33m' # Yellow
txtblu='\e[0;34m' # Blue
txtpur='\e[0;35m' # Purple
txtcyn='\e[0;36m' # Cyan
txtwht='\e[0;37m' # White
bldblk='\e[1;30m' # Black - Bold
bldred='\e[1;31m' # Red
bldgrn='\e[1;32m' # Green
bldylw='\e[1;33m' # Yellow
bldblu='\e[1;34m' # Blue
bldpur='\e[1;35m' # Purple
bldcyn='\e[1;36m' # Cyan
bldwht='\e[1;37m' # White
unkblk='\e[4;30m' # Black - Underline
undred='\e[4;31m' # Red
undgrn='\e[4;32m' # Green
undylw='\e[4;33m' # Yellow
undblu='\e[4;34m' # Blue
undpur='\e[4;35m' # Purple
undcyn='\e[4;36m' # Cyan
undwht='\e[4;37m' # White
bakblk='\e[40m'   # Black - Background
bakred='\e[41m'   # Red
bakgrn='\e[42m'   # Green
bakylw='\e[43m'   # Yellow
bakblu='\e[44m'   # Blue
bakpur='\e[45m'   # Purple
bakcyn='\e[46m'   # Cyan
bakwht='\e[47m'   # White
txtrst='\e[0m'

SEG[0]="$txtcyn┌$txtrst"
SEG[1]="$bldwht[$txtrst$bldred~\u$txtrst$bldwht]"
SEG[2]="$txtcyn─$txtrst$bldwht[$txtrst$bldylw@\h$txtrst$bldwht]"
SEG[3]="$txtcyn─$txtrst$bldwht[$txtrst$txtcyn\w$txtrst$bldwht]$txtrst$txtcyn$txtcyn─$txtrst="

SEG[4]="$bldwht($txtrst$txtgrn"
SEG[5]='$(ls -1 | wc -l | sed "s: ::g") files, $(ls -lah | grep -m 1 total | sed "s/total //")'
SEG[6]="$txtrst$bldwht)$txtrst"

SEG[7]="$bldcyn─$txtrst$bldwht[$txtrst$(date +%k:%M)$bldwht]$txtrst"
#$bldcyn─$txtrst$bldgrn>$txtrst"
SEG[8]="\n$txtcyn└$bldgrn$txtrst$bldcyn>"
#┌[\u]─[@\h]─[\w]
#└($(CMD))─[\T]─>
#$>

PS1=
for I in $(seq 0 $(( ${#SEG[@]} - 1 )) )
do
	PS1="$PS1${SEG[$I]}\e[0m"
done
```

``` bash

#bakblk='\e[40m'   # Black - Background
#bakred='\e[41m'   # Red
#bakgrn='\e[42m'   # Green
#bakylw='\e[43m'   # Yellow
#bakblu='\e[44m'   # Blue
#bakpur='\e[45m'   # Purple
#bakcyn='\e[46m'   # Cyan
#bakwht='\e[47m'   # White
#txtrst='\e[0m'

#SEG[5]="$bldcyn─$txtrst$bldwht[$txtrst$(date +%k:%M | tr -d '\n')$bldwht]"
#$bldcyn─$txtrst$bldgrn>$txtrst"
#SEG[6]="\n$txtcyn└$bldgrn$txtrst$bldcyn>"

##PS1="$txtrst$txtcyn┌$txtrst$bldwht[$txtrst$bldred~\u$txtrst$bldwht]$txtrst$txtcyn─$txtrst$bldwht[$txtrst$bldylw@\h$txtrst$bldwht]$txtrst$txtcyn─$txtrst$bldwht[$txtrst$txtcyn\w$txtrst$bldwht]$txtrst$txtcyn$txtcyn─$txtrst$bldwht($txtrst$txtgrn"'$(ls -1 | wc -l | sed "s: ::g" | tr -d "\n") files, $(ls -lah | grep -m 1 total | sed "s/total //" | tr -d "\n" )'"$bldwht)$txtrst$bldcyn─$txtrst$bldwht[$txtrst"'$(date +%k:%M | tr -d '\n')'"$bldwht]$txtrst\n$txtcyn└$bldgrn$txtrst$bldcyn>$txtrst$txtrst"
#┌[\u]─[@\h]─[\w]
#└($(CMD))─[\T]─>
#$>
##PS1="\[\033[0;36m\]┌─\[\033[00m\][\[\033[1;31m\]~\u\[\033[00m\]]\[\033[0;36m\]─\[\033[00m\][\[\033[1;33m\]@\h\[\033[00m\]]\[\033[0;36m\]─\[\033[00m\][\[\033[0;37m\]\T\[\033[00m\]]\[\033[0;36m\]─\[\033[00m\][\[\033[1;33m\]\w\[\033[00m\]]\n\[\033[0;36m\]└\[\033[1;32m\]>\[\033[00m\]"
#PS1="$txtcyn┌─$[$bldred~\u$txtrst]$txtcyn─$txtrst[$bldylw@\h$txtrst]$txtcyn─$txtrst[$txtwht\T$txtrst]$txtcyn─$txtrst[$bldylw\w$txtrst]\n$txtcyn└$bldgrn>$txtrst"

#PS1="$txtcyn┌─\[\033[00m\][$bldred~\u\[\033[00m\]]$txtcyn─\[\033[00m\][$bldylw@\h\[\033[00m\]]$txtcyn─\[\033[00m\][$txtwht\T\[\033[00m\]]$txtcyn─\[\033[00m\][$bldylw\w\[\033[00m\]]\n$txtcyn└$bldgrn>\[\033[00m\]"



#PS1=''
#for I in $(seq 0 $(( ${#SEG[@]} - 1 )) )
#do
#	PS1="$PS1${SEG[$I]}\e[0m"
#done


#$(git remote -v 2>/dev/null | grep -e '^origin.*(fetch)' | sed 's/^.*\/\(.*\)\.git.*/\1:/')
#$(git branch 2>/dev/null | grep -e '\* ' | sed 's/^..\(.*\)/\1/')'
#$(__git_ps1 "(%s)")


#BBLUE='\[\033[1;34m\]'

#BLUE='\[\033[0;34\]'
#NORMAL='\[\033[00m\]'

#A='\[\033[0;37m\]' # Gray
#B='\[\033[0;36m\]' # Light Blue

#Y='\[\033[1;33m\]' # Bright Yellow
#G='\[\033[1;32m\]' # Green
#R='\[\033[1;31m\]' # Red

#N='\[\033[00m\]'
#L='─'
#U='┌'
#D='└'
#C="●"
#P="$L$L$L$L$L$L$L"
#P="$L"
#PS1="$B$U$L$N[$R~\u$N]$B$L$N[$Y@\h$N]$B$L$N[$A\T$N]$B$P$N[$Y\w$N]\n$B$D$G>$N"


#PS1="$B$U$L$N[$R~\u$N]$B$L$N[$Y@\h$N]$B$L$N[$A\T$N]$B$P$N[$Y\w$N]$B$D$G>$N"
#PS1="\[\033[1;30m\][\[\033[1;34m\]\u\[\033[1;30m\]@\[\033[0;35m\]\h\[\033[1;30m\]] \[\033[0;37m\]\W \[\033[1;30m\]\$\[\033[0m\] " 

#PS1="\`if [ \$? = 0 ]; then echo \[\e[33m\]^_^\[\e[0m\]; else echo \[\e[31m\]O_O\[\e[0m\]; fi\`[\u@\h:\w]\\$ "
#PROMPT_COMMAND='PS1="\[\033[0;33m\][\!]\`if [[ \$? = "0" ]]; then echo "\\[\\033[32m\\]"; else echo "\\[\\033[31m\\]"; fi\`[\u.\h: \`if [[ `pwd|wc -c|tr -d " "` > 18 ]]; then echo "\\W"; else echo "\\w"; fi\`]\$\[\033[0m\] "; echo -ne "\033]0;`hostname -s`:`pwd`\007"'
#PS1="[\[\033[32m\]\w]\[\033[0m\]\n\[\033[1;36m\]\u\[\033[1;33m\]-> \[\033[0m\]"
#PS1='\[\e[1;32m\]\u@\H:\[\e[m\] \[\e[1;37m\]\w\[\e[m\]\n\[\e[1;33m\]hist:\! \[\e[0;33m\] \[\e[1;31m\]jobs:\j \$\[\e[m\] '
#PS1="\n\[\e[30;1m\]\[\016\]l\[\017\](\[\e[34;1m\]\u@\h\[\e[30;1m\])-(\[\e[34;1m\]\j\[\e[30;1m\])-(\[\e[34;1m\]\@ \d\[\e[30;1m\])->\[\e[30;1m\]\n\[\016\]m\[\017\]-(\[\[\e[32;1m\]\w\[\e[30;1m\])-(\[\e[32;1m\]\$(/bin/ls -1 | /usr/bin/wc -l | /bin/sed 's: ::g') files, \$(/bin/ls -lah | /bin/grep -m 1 total | /bin/sed 's/total //')b\[\e[30;1m\])--> \[\e[0m\]"
#PS1="\n\[\e[32;1m\](\[\e[37;1m\]\u\[\e[32;1m\])-(\[\e[37;1m\]jobs:\j\[\e[32;1m\])-(\[\e[37;1m\]\w\[\e[32;1m\])\n(\[\[\e[37;1m\]! \!\[\e[32;1m\])-> \[\e[0m\]"

#if [ -z "$SSH_CLIENT" ]; then
#PS1='\[\e[0;32m\]\u\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\]\$ \[\e[m\]\[\e[0;37m\]'
#else
#PS1='\[\e[0;32m\]\u\[\e[m\]\[\e[1;31m\]@\[\e[m\]\[\e[1;33m\]\h\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\]\$ \[\e[m\]\[\e[0;37m\]'
#fi
#PS1="\n#--[\[\e[1;36m\]\u@\h\[\e[m\]]-[\[\e[1;34m\]\w\[\e[m\]]-[\$(date +%k:%M)]-->\n"
#PS1="\n\[\e[30;1m\](\[\e[34;1m\]\u@\h\[\e[30;1m\])-(\[\e[34;1m\]\t\[\e[30;1m\])-(\[\[\e[32;1m\]\w\[\e[30;1m\])\[\e[30;1m\]\n(jobs:\[\e[34;1m\]\j\[\e[30;1m\])\`if [ \$? -eq 0 ]; then echo \[\e[32m\] \:\-\); else echo \[\e[31m\] \:\-\( ; fi\`\[\e[0m\] $ "

# Background
#local gblack="\[\033[40m\]" # Black


# Background
#local gblack="\[\033[40m\]" # Black
#local gred="\[\033[41m\]" # Red
#local ggreen="\[\033[42m\]" # Green
#local gyellow="\[\033[43m\]" # Yellow
#local gblue="\[\033[44m\]" # Blue
#local gpurple="\[\033[45m\]" # Purple
#local gcyan="\[\033[46m\]" # Cyan
#local gwhite="\[\033[47m\]" # White

# High Intensty
#local hblack="\[\033[0;90m\]" # Black
#local hred="\[\033[0;91m\]" # Red
#local hgreen="\[\033[0;92m\]" # Green
#local hyellow="\[\033[0;93m\]" # Yellow
#local hblue="\[\033[0;94m\]" # Blue
#local hpurple="\[\033[0;95m\]" # Purple
#local hcyan="\[\033[0;96m\]" # Cyan
#local hwhite="\[\033[0;97m\]" # White

# Bold High Intensty
#BIBlack="\[\033[1;90m\]" # Black
#BIRed="\[\033[1;91m\]" # Red
#BIGreen="\[\033[1;92m\]" # Green
#BIYellow="\[\033[1;93m\]" # Yellow
#BIBlue="\[\033[1;94m\]" # Blue
#BIPurple="\[\033[1;95m\]" # Purple
#BICyan="\[\033[1;96m\]" # Cyan
#BIWhite="\[\033[1;97m\]" # White

# High Intensty backgrounds
#On_IBlack="\[\033[0;100m\]" # Black
#On_IRed="\[\033[0;101m\]" # Red
#On_IGreen="\[\033[0;102m\]" # Green
#On_IYellow="\[\033[0;103m\]" # Yellow
#On_IBlue="\[\033[0;104m\]" # Blue
#On_IPurple="\[\033[10;95m\]" # Purple
#On_ICyan="\[\033[0;106m\]" # Cyan
#On_IWhite="\[\033[0;107m\]" # White

#Time12h="\T"
#Time12a="\@"
#PathShort="\w"
#PathFull="\W"
#NewLine="\n"
#Jobs="\j"

#local GRAY="\[\033[1;30m\]"
#local LIGHT_GRAY="\[\033[0;37m\]"
#local CYAN="\[\033[0;36m\]"
#local LIGHT_CYAN="\[\033[1;36m\]"
#local NO_COLOUR="\[\033[0m\]"

#local temp=$(tty)
#local GRAD1=${temp:5}

#PS1="$TITLEBAR\
#$GRAY-$CYAN-$LIGHT_CYAN(\
#$CYAN\u$GRAY@$CYAN\h\
#'$LIGHT_CYAN)$CYAN-$LIGHT_CYAN(\
#$CYAN\#$GRAY/$CYAN$GRAD1\
#$LIGHT_CYAN)$CYAN-$LIGHT_CYAN(\
#$CYAN\$(date +%H%M)$GRAY/$CYAN\$(date +%d-%b-%y)\
#$LIGHT_CYAN)$CYAN-$GRAY-\
#$LIGHT_GRAY\n\
#$GRAY-$CYAN-$LIGHT_CYAN(\
#$CYAN\$$GRAY:$CYAN\w\
#$LIGHT_CYAN)$CYAN-$GRAY-$LIGHT_GRAY " 

local Q="\[\033[0m\]" # Text Reset
local B='30m\]' # Black
local R='31m\]' # Red
local G='32m\]' # Green
local Y='33m\]' # Yellow
local M='34m\]' # Blue
local P='35m\]' # Purple
local C='36m\]' # Cyan
local W='37m\]' # White
# QEIOLKHJHFDSAZXV
local N='\[\033[0;' # Normal color
local B='\[\033[1;' # Bold
local U='\[\033[4;' # Underline 

#local DASH="$N$C─$Q" # OK
local DASH="$B$C─$Q" # OK
#PS1="$N$C┌$Q$DASH[¬\u]$DASH[@\h]$DASH[\w]$DASH[\T]\n$N$C└$Q$N$G>$Q" # OK
#PS1="$N$C┌$Q$DASH[$B$R~\u$Q]$DASH[$B$Y@\h$Q]$DASH[$B$Y\w$Q]$DASH[\T]\n$N$C└$Q$N$G>$Q" # OK
#PS1="$N$C┌$Q$DASH[$B$R~\u$Q]$DASH[$B$Y@\h$Q]$DASH[$B$Y\w$Q]$DASH[\T]\n$N$C└\$(ls -1 | wc -l | sed \"s: ::g\") files, \$(ls -lah | grep -m 1 total | sed \"s/total //\")\$Q$N$G>$Q" # OK
# ✓✗●
#https://wiki.archlinux.org/index.php/Color_Bash_Prompt
PS1="\
$B$C┌$Q$DASH\
[$B$M\u$Q$B$Y@\h$Q]$DASH\
[\$( echo \$? )]$DASH\
[\#]$DASH\
[\$(date +%k:%M.%S)]$DASH\
[$B$Y\w$Q, \$(ls -1 | wc -l | sed \"s: ::g\") files, \$(ls -lah | grep -m 1 total | sed \"s/total //\")]\
$B$G>$Q\
\n$B$C└$Q$B$G>$Q\
"
```