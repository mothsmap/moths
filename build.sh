#!/bin/bash

gyp --depth=. --include=3rd/skia/gyp/common.gypi everything.gyp

make BUILDTYPE=Release