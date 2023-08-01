import sys
import functools

import obspython
import hid

vid = 0x3297    # ZSA
pid = 0xc6cf    # Planck EZ Glow

RAW_EPSIZE = 32

print(sys.executable)
print(sys.version_info)

def send(*colors):
    print('send', colors)

    for dev_info in hid.enumerate(vid, pid):
        print(dev_info)
        if dev_info['usage_page'] == 0xFF60 and dev_info['usage'] == 0x61:
            path = dev_info['path']
            break
    else:
        print('Not found...')
        return
    report = (
        b'\0'
        + b''.join(bytes((i, *color)) for i, color in enumerate(colors))
        + b'\xff'
    )

    with hid.Device(path=path) as h:
        summary = '\n'.join([
            f'Path: path.decode()',
            f'Device manufacturer: {h.manufacturer}',
            f'Product: {h.product}',
            f'Serial Number: {h.serial}',
            f'Sent: {report}'
        ])
        print(summary)

        h.write(report.ljust(RAW_EPSIZE, b'\xff'))

def go(*args, **kwargs):
    send(
        (255, 0, 0) if obspython.obs_frontend_recording_active() else (0, 128, 128),
        (255, 0, 0) if obspython.obs_frontend_streaming_active() else (0, 128, 128),
    )

def script_description():
  return "QMK Macropad integration"

def script_properties():
    props = obspython.obs_properties_create()
    obspython.obs_properties_add_button(props, 'report', 'Report!', go)
    return props

def script_load(_props):
    obspython.obs_frontend_add_event_callback(go)
    go()

def script_unload():
    # Reset colours
    send((255, 255, 255), (255, 255, 255))
