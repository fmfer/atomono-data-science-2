#!/bin/sh
#

cat $2 | sed -n "/振り返り　$1/, /avg/p" | sed -e 's/水野響/3/' -e 's/平田聖/2/' -e 's/大野寛人/6/' -e 's/中山建太/1/' -e 's/FABIAN M. FERNANDEZ/7/' -e 's/Dai Miyahara/5/' -e 's/鈴木真希/4/' | sed -e 's/振り返り/  振り返り/' | sort | sed 's/ [0-9]: //' | grep -v FigJam

cat $2 | sed -n "/振り返り　$1/, /Slack avg/p" | sed -n '/Slack:/, /Slack avg/p' | sed -e 's/Hibiki/3/' -e 's/satoshi.hirata/2/' -e 's/Ohno/6/' -e 's/Nakayama/1/' -e 's/FABIAN/7/' -e 's/Dai/5/' -e 's/鈴木真希/4/' | sed -e 's/Slack:/  Slack/' | sort | sed 's/ [0-9]: //' | grep -v FigJam
