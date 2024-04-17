from time import sleep

import gpiod
from gpiod.line import Direction, Value

CHIP_NAME     = "/dev/gpiochip4"
CONSUMER_NAME = "skr_lchika"
LINE_R        = 5
LINE_G        = 6
LINE_B        = 13
LINE_COM      = 21
SLEEP_SEC     = 0.5


def run():
    # GPIO チップが存在するか。無ければ終了。
    if not gpiod.is_gpiochip_device( CHIP_NAME ):
        return

    # ラインを開く。
    request = gpiod.request_lines(
        CHIP_NAME,
        consumer=CONSUMER_NAME,
        config={
            LINE_R: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.ACTIVE
            ),
            LINE_G: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.ACTIVE
            ),
            LINE_B: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.ACTIVE
            ),
            LINE_COM: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.ACTIVE
            ),
        }
    )

    # 一旦全ての色を消す。
    setValue( request, [LINE_R, LINE_G, LINE_B, LINE_COM], Value.ACTIVE )

    # メインループ。
    while True:
        lighting( request )


def setValue(
        request,
        lines,
        value
):
    for l in lines:
        request.set_value( l, value )


def lighting(
        request
):
    # RgB
    request.set_value( LINE_R, Value.INACTIVE )
    request.set_value( LINE_G, Value.ACTIVE )
    sleep( SLEEP_SEC )
    # Rgb
    request.set_value( LINE_B, Value.ACTIVE )
    sleep( SLEEP_SEC )
    # RGb
    request.set_value( LINE_G, Value.INACTIVE )
    request.set_value( LINE_B, Value.ACTIVE )
    sleep( SLEEP_SEC )
    # rGb
    request.set_value( LINE_R, Value.ACTIVE )
    sleep( SLEEP_SEC )
    # rGB
    request.set_value( LINE_B, Value.INACTIVE )
    request.set_value( LINE_R, Value.ACTIVE )
    sleep( SLEEP_SEC )
    # rgB
    request.set_value( LINE_G, Value.ACTIVE )
    sleep( SLEEP_SEC )



