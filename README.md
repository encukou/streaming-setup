# My streaming setup

These are mostly notes for myself at this point.

## OBS

...

## Planck EZ macropad

Custom QMK firmware is in `macropad/stream2`; after setting up QMK
compile and flash with `mk flash -kb planck/ez/glow -km stream2`.

Relegendable keycaps `macropad/key-legends.svg`

The stream layer is activated by the bottom left key (`○`).

The recording/streaming indicator is powered by OBS scripts
(these need to be added in order):

- `macropad/hid.py`
- `macropad/macropad_obs_plugin.py`


## Pointout

Currently a separate repository.
