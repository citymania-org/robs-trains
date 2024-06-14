# robs_trains
Rob’s Trains

# Dependencies

[grf-py](https://github.com/citymania-org/grf-py)
[psd-tools](https://github.com/psd-tools/psd-tools)

# Compiling

run 'pip install -r requirements.txt' or manually download dependencies
run generate.py

# PSDLivery

## Definition
PSDLivery has 3 compositing arguments: shading, paint and overlay.
Each can specify either one, many or no layers in PSD file (by layer name).
If more than one layer is specified for the group they're merged between any further processing is done.
Syntax:
0. None: Just omit the argument or use `shading=None`.
1. One: `shading='layer'` or `shading=('layer',)`
2. Many: `shading=('layer1', 'layer2', 'layer3')`

## Paint processing

Palette for paint is read from `compal.png`. 5th column is the main colour. For every pixel of one of the main colours in the paint layer code looks at pixel in the shading layer. If shading pixel is of blue CC range it takes the CC index of that colour and uses it to get corresponding colour from the paint palette (within the same row of main colour).
- First two rows of paint palette must be CC1 and CC2 ranges.
- Any colour of the first two rows (CC colours) can be used in the paint as a main colour. They all act the same as 5th colour. This is done for compatibility with old sprites that have shading in 2CC layer.
- If any non-main colour is used in the paint layer compile will error out.

## Finalising
1. Overlay layers are composed on top of the resulting image.
2. If auto_cc is used colours from CC ranges are converted into mask (CC colours in the game).
3. Alternatively, if cc_replace or cc2_replace are used colours from CC ranges are converted to the specified colour ranges.

## Usage
1. To make 2CC livery do 1CC (blue) sprite in the shading layer and paint some pixels with 5th green CC colour in the paint layer. Use `auto_cc=True` argument.
2. Real world liveries option 1. Same as (1) but use `cc_replace` and `cc2_replace` to change CC colours into real livery colours.
2. Real world liveries option 2. Do 1CC (blue) sprite in the shading layer and do livery in paint layer using colours from 5th coloumn in paint palette.
