from time import sleep

import lgpio

CHIP_NUMBER   = 4
CONSUMER_NAME = "skr_lchika"
LINE_R        = 5
LINE_G        = 6
LINE_B        = 13
LINE_COM      = 21
SLEEP_SEC     = 0.5


def run():
    # # GPIO チップが存在するか。無ければ終了。
    # if not lgpio.is_gpiochip_device( CHIP_NAME ):
    #     return

    # GPIO チップを開く。開けなかったら終了。
    handle = lgpio.gpiochip_open( CHIP_NUMBER )
    if 0 > handle:
        return

    # GPIO を開く。1箇所でも開けなかったら終了。
    n = lgpio.gpio_claim_output( handle, LINE_R )
    if lgpio.gpio_claim_output( handle, LINE_G ) or \
       lgpio.gpio_claim_output( handle, LINE_B ) or \
       lgpio.gpio_claim_output( handle, LINE_COM ):
        lgpio.gpiochip_close( handle )
        return

    # 一旦全ての色を消す。
    setValue( handle, [LINE_R, LINE_G, LINE_B, LINE_COM], 1 )

    # メインループ。
    while True:
        lighting( handle )


def setValue(
        handle,
        gpios,
        level
):
    for g in gpios:
        lgpio.gpio_write( handle, g, level )


def lighting(
        handle
):
    # RgB
    lgpio.gpio_write( handle, LINE_R, 0 )
    lgpio.gpio_write( handle, LINE_G, 1 )
    sleep( SLEEP_SEC )
    # Rgb
    lgpio.gpio_write( handle, LINE_B, 1 )
    sleep( SLEEP_SEC )
    # RGb
    lgpio.gpio_write( handle, LINE_G, 0 )
    lgpio.gpio_write( handle, LINE_B, 1 )
    sleep( SLEEP_SEC )
    # rGb
    lgpio.gpio_write( handle, LINE_R, 1 )
    sleep( SLEEP_SEC )
    # rGB
    lgpio.gpio_write( handle, LINE_B, 0 )
    lgpio.gpio_write( handle, LINE_R, 1 )
    sleep( SLEEP_SEC )
    # rgB
    lgpio.gpio_write( handle, LINE_G, 1 )
    sleep( SLEEP_SEC )



