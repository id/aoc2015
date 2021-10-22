#!/usr/bin/env sh

set -x

padded_day=${1:-$(date '+%d')}
day=$((10#$padded_day))
session=$(<.session)
curl -s --cookie "session=${session}" https://adventofcode.com/2015/day/${day}/input -o tests/data/${padded_day}.txt && echo DONE
