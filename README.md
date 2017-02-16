Mosaic
======

A script's repo that makes you think your pictures made from shiny rocks, bricks, little pixels, etc.

## Requirements

Here are the requirements for these scripts:

- Python3.x
- Pillow

## Usage

You can use it by typing

> `python3 mosaic.py --input <PATH_OF_ORIGINAL_PHOTO> --output <PATH_TO_THE_NEW_IMAGE.png> --mask <PATH_TO_ALPHA_MASK_IMAGE> --background "<HEX_CODE_FOR_BACKGROUND>"`

**Notes for arguments**:

- `--input`: required.
- `--output`: required.
- `--mask`: Optional. But if you do not specify a mask, your picture will be pixelized only.
- `--background`: Optional. If you do not specify, it'll use "#FFFFFF".

Note that for `--background` parameter, your color should be start with `#` and must be 6 characters long, exactly. So, you should use `#FFFFFF` instead of `#FFF`


## Some results

![github-logo-transparent](https://cloud.githubusercontent.com/assets/4905664/23026019/9142d8ae-f468-11e6-9527-08bafc108c36.jpg)
![github-out](https://cloud.githubusercontent.com/assets/4905664/23026018/911bd6d2-f468-11e6-83a1-3186c07f9a08.png)
![apple](https://cloud.githubusercontent.com/assets/4905664/23026020/914ecf92-f468-11e6-8fad-0269497b6ec3.jpg)
![apple_out](https://cloud.githubusercontent.com/assets/4905664/23026059/b9d4babc-f468-11e6-8144-57e564b94f71.png)


**Note about a mask:** I used someone's mask for glossy appearance. Thanks for the icon [Gwas10](http://gbrtb.deviantart.com)
