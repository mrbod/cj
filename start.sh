#!/bin/bash
name="$1"

git clone $(dirname $0)/c++ "$name"
cd "$name"
git co -b "$name"
touch input
touch output
git add input output
git ci -m 'init $name'
meson build
