
"""
✘ Commands Available

• `{i}alive`
    Check if your bot is working.

• `{i}ping`
    Check Infinato's response time.

• `{i}cmds`
    View all plugin names.

• `{i}restart`
    To restart your bot.

• `{i}logs (sys)`
    Get the full terminal logs.

• `{i}logs heroku`
   Get the latest 100 lines of heroku logs.

• `{i}shutdown`
    Turn off your bot.
"""

import time
from datetime import datetime as dt
from platform import python_version as pyver

import heroku3
import requests
from git import Repo
from infinatoUserbot import __version__ as UltVer
from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from . import *

HEROKU_API = None
HEROKU_APP_NAME = None

try:
    if Var.HEROKU_API and Var.HEROKU_APP_NAME:
        HEROKU_API = Var.HEROKU_API
        HEROKU_APP_NAME = Var.HEROKU_APP_NAME
        Heroku = heroku3.from_key(Var.HEROKU_API)
        heroku_api = "https://api.heroku.com"
        app = Heroku.app(Var.HEROKU_APP_NAME)
except BaseException:
    HEROKU_API = None
    HEROKU_APP_NAME = None


@ultroid_cmd(
    pattern="alive$",
)
async def lol(ult):
    pic = udB.get("ALIVE_PIC")
    uptime = grt(time.time() - start_time)
    header = udB.get("ALIVE_TEXT") if udB.get("ALIVE_TEXT") else "Hey,  I am alive."
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    als = (get_string("alive_1")).format(
        header,
        OWNER_NAME,
        infinato_version,
        uptime,
        pyver(),
        __version__,
        kk,
    )
    if pic is None:
        return await eor(ult, als)
    elif pic is not None and "telegra" in pic:
        try:
            await ultroid_bot.send_message(
                ult.chat_id, als, file=pic, link_preview=False
            )
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)
    else:
        try:
            await ultroid_bot.send_message(ult.chat_id, file=pic)
            await ultroid_bot.send_message(ult.chat_id, als, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)


@ultroid_cmd(
    pattern="ping$",
)
async def _(event):
    start = dt.now()
    x = await eor(event, "`Pong !`")
    end = dt.now()
    ms = (end - start).microseconds / 1000
    uptime = grt(time.time() - start_time)
    await x.edit("🏓**Pong !!** - `{}ms`\n⏱**Uptime** - `{}`\n\n**My Master** - [{}](tg://user?id={})".format(ms, uptime, OWNER_NAME, OWNER_ID))


@ultroid_cmd(
    pattern="cmds$",
)
async def cmds(event):
    await allcmds(event)


@ultroid_cmd(
    pattern="restart$",
)
async def restartbt(ult):
    if Var.HEROKU_API:
        await eor(ult, "`Restarting..`")
        try:
            await restart(ult)
        except BaseException:
            await bash("pkill python3 && python3 -m infinatoUserbot")
    else:
        await bash("pkill python3 && python3 -m infinatoUserbot")


@ultroid_cmd(pattern="shutdown")
async def shutdownbot(ult):
    if not ult.out:
        if not is_fullsudo(ult.sender_id):
            return await eod(ult, "`This Command Is Sudo Restricted.`")
    try:
        dyno = ult.text.split(" ", maxsplit=1)[1]
    except IndexError:
        dyno = None
    if dyno:
        if dyno not in ["userbot", "vcbot", "web", "worker"]:
            await eor(ult, "Invalid Dyno Type specified !")
            return
        await shutdown(ult, dyno)
    else:
        await shutdown(ult)


@ultroid_cmd(
    pattern="logs",
)
async def get_logs(event):
    try:
        opt = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await def_logs(event)
    if opt == "heroku":
        await heroku_logs(event)
    elif opt == "sys":
        await def_logs(event)
    else:
        await def_logs(event)


async def heroku_logs(event):
    if HEROKU_API is None and HEROKU_APP_NAME is None:
        return await eor(
            event, "Please set `HEROKU_APP_NAME` and `HEROKU_API` in vars."
        )
    await eor(event, "`Downloading Logs...`")
    ok = app.get_log()
    with open("infinato-heroku.log", "w") as log:
        log.write(ok)
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": ok})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    await ultroid_bot.send_file(
        event.chat_id,
        file="infinato-heroku.log",
        thumb="resources/extras/logo_rdm.png",
        caption=f"**INFINATO Heroku Logs.**\nPasted [here]({url}) too!",
    )
    os.remove("infinato-heroku.log")


async def def_logs(ult):
    xx = await eor(ult, "`Processing...`")
    with open("infinato.log") as f:
        k = f.read()
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": k})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    await ultroid_bot.send_file(
        ult.chat_id,
        file="infinato.log",
        thumb="resources/extras/cf1.jpg",
        caption=f"**Infinato Logs.**\nPasted [here]({url}) too!",
    )
    await xx.edit("Done")
    await xx.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})