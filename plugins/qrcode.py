"""
✘ Commands Available -
•`{i}size <reply to media>`
   To get size of it.
•`{i}resize <number> <number>`
   To resize image on x, y axis.
   eg. `{i}resize 690 960`
"""

from . import *


@ultroid_cmd(pattern="size$")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "`Reply To image`")
    k = await eor(e, "`Processing...`")
    if hasattr(r.media, "document"):
        img = await ultroid_bot.download_media(r, thumb=-1)
    else:
        img = await ultroid_bot.download_media(r.media)
    im = Image.open(img)
    x, y = im.size
    await k.edit(f"Dimension Of This Image Is\n`{x} x {y}`")
    os.remove(img)


@ultroid_cmd(pattern="resize ?(.*)")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "`Reply To image`")
    sz = e.pattern_match.group(1)
    if not sz:
        return await eod(f"Give Some Size To Resize, Like `{HNDLR}resize 720 1080` ")
    k = await eor(e, "`Processing...`")
    if hasattr(r.media, "document"):
        img = await ultroid_bot.download_media(r, thumb=-1)
    else:
        img = await ultroid_bot.download_media(r.media)
    sz = sz.split()
    if not len(sz) == 2:
        return await eod(f"Give Some Size To Resize, Like `{HNDLR}resize 720 1080` ")
    x, y = int(sz[0]), int(sz[1])
    im = Image.open(img)
    ok = im.resize((x, y))
    ok.save(img, format="PNG", optimize=True)
    await ultroid_bot.send_file(e.chat_id, img)
    os.remove(img)
    await k.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})