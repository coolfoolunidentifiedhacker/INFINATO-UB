
import re
import time
from datetime import datetime
from math import ceil
from os import remove
from platform import python_version as PyVer

import telethon.events
from git import Repo
from infinatoUserbot import __version__ as UltVer
from support import *
from telethon import Button, __version__
from telethon.tl.types import InputWebDocument

from . import *

# ================================================#
notmine = f"This bot is for {OWNER_NAME}"
INFINATO_PIC = "https://telegra.ph/file/9c22477daacf4ca4a2914.png"
helps = get_string("inline_1")

add_ons = udB.get("ADDONS")
if add_ons == "True" or add_ons is None:
    zhelps = get_string("inline_2")
else:
    zhelps = get_string("inline_3")
if udB.get("INLINE_PIC"):
    _file_to_replace = udB.get("INLINE_PIC")
else:
    _file_to_replace = "resources/extras/cf_inline.png"
# ============================================#


@in_pattern("")
@in_owner
async def e(o):
    if len(o.text) == 0:
        b = o.builder
        uptime = grt(time.time() - start_time)
        header = udB.get("ALIVE_TEXT") if udB.get("ALIVE_TEXT") else "Hey,  I am alive."
        ALIVEMSG = get_string("alive_1").format(
            header,
            OWNER_NAME,
            infinato_version,
            uptime,
            PyVer(),
            __version__,
            Repo().active_branch,
        )
        res = [
            await b.article(
                title="ยซ ๐๐๐๐๐๐๐๐ ยป",
                url="https://t.me/INFINITY_I_i_I_i_I_i_I_i_I_i_I_i",
                description="A Simple Telethon Bot.",
                text=ALIVEMSG,
                thumb=InputWebDocument(INFINATO_PIC, 0, "image/jpeg", []),
            ),
        ]
        await o.answer(res, switch_pm=f"๐ฅ ASSISTANT OF [{OWNER_NAME}](tg://user?id={OWNER_ID})",
                       switch_pm_param="start")


@in_pattern("ultd")
@in_owner
async def inline_handler(event):
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    cmd = len(z)
    bnn = asst.me.username

    @in_pattern("ultd")
    @in_owner
    async def inline_handler(event: telethon.events.InlineQuery.Event):
        z = []
        for x in LIST.values():
            for y in x:
                z.append(y)
        cmd = len(z)
        bnn = asst.me.username
        result = event.builder.photo(
            file=_file_to_replace,
            link_preview=False,
            text=get_string("inline_4").format(
                OWNER_NAME,
                len(PLUGINS),
                len(ADDONS),
                cmd,
            ),
            buttons=[
                [
                    Button.inline("โข Pสแดษขษชษดs", data="hrrrr"),
                    Button.inline("โข Aแดแดแดษดs", data="frrr"),
                ],
                [
                    Button.inline("Oแดกษดแดสโขแดแดแดส๊ฑ", data="ownr"),
                    Button.inline("IษดสษชษดแดโขPสแดษขษชษดs", data="inlone"),
                ],
                [
                    Button.url("โ๏ธSแดแดแดษชษดษขsโ๏ธ", url=f"https://t.me/{bnn}?start=set"),
                ],
                [Button.inline("โขโขCสแด๊ฑแดโขโข", data="close")],
            ],
        )
        await event.answer([result])


@in_pattern("paste")
@in_owner
async def _(event):
    ok = event.text.split(" ")[1]
    link = "https://nekobin.com/"
    result = event.builder.article(
        title="Paste",
        text="Pแดsแดแดแด Tแด Nแดแดแดสษชษด!",
        buttons=[
            [
                Button.url("NekoBin", url=f"{link}{ok}"),
                Button.url("Raw", url=f"{link}raw/{ok}"),
            ],
        ],
    )
    await event.answer([result])


@callback("ownr")
@owner
async def setting(event):
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    cmd = len(z)
    await event.edit(
        get_string("inline_4").format(
            OWNER_NAME,
            len(PLUGINS),
            len(ADDONS),
            cmd,
        ),
        file=_file_to_replace,
        link_preview=False,
        buttons=[
            [
                Button.inline("โขPษชษดษขโข", data="pkng"),
                Button.inline("โขUแดแดษชแดแดโข", data="upp"),
            ],
            [
                Button.inline("โขRแดsแดแดสแดโข", data="rstrt"),
                Button.inline("โขUแดแดแดแดแดโข", data="doupdate"),
            ],
            [Button.inline("ยซ Bแดแดแด", data="open")],
        ],
    )


@callback("doupdate")
@owner
async def _(event):
    check = await updater()
    if not check:
        return await event.answer(
            "You Are Already On Latest Version", cache_time=0, alert=True
        )
    repo = Repo.init()
    ac_br = repo.active_branch
    changelog, tl_chnglog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    changelog_str = changelog + f"\n\nClick the below button to update!"
    if len(changelog_str) > 1024:
        await event.edit(get_string("upd_4"))
        file = open(f"infinato_updates.txt", "w+")
        file.write(tl_chnglog)
        file.close()
        await event.edit(
            get_string("upd_5"),
            file="infinato_updates.txt",
            buttons=[
                [Button.inline("โข Uแดแดแดแดแด Nแดแดก โข", data="updatenow")],
                [Button.inline("ยซ Bแดแดแด", data="ownr")],
            ],
        )
        remove(f"infinato_updates.txt")
        return
    else:
        await event.edit(
            changelog_str,
            buttons=[
                [Button.inline("Update Now", data="updatenow")],
                [Button.inline("ยซ Bแดแดแด", data="ownr")],
            ],
            parse_mode="html",
        )


@callback("pkng")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    pin = f"๐Pษชษดษข = {ms}ms"
    await event.answer(pin, cache_time=0, alert=True)


@callback("upp")
async def _(event):
    uptime = grt(time.time() - start_time)
    pin = f"๐Uแดแดษชแดแด = {uptime}"
    await event.answer(pin, cache_time=0, alert=True)


@callback("inlone")
@owner
async def _(e):
    button = [
        [
            Button.switch_inline(
                "Pสแดส Sแดแดสแด Aแดแดs",
                query="app telegram",
                same_peer=True,
            ),
            Button.switch_inline(
                "Mแดแดแดแดแด Aแดแดs",
                query="mods minecraft",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "Sแดแดสแดส Oษด Gแดแดษขสแด",
                query="go INFINATO",
                same_peer=True,
            ),
            Button.switch_inline(
                "Sแดแดสแดส Oษด Yแดสแดแด",
                query="yahoo INFINATO",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "WสษชSแดแดส",
                query="msg username wspr Hello",
                same_peer=True,
            ),
            Button.switch_inline(
                "YแดแดTแดสแด Dแดแดกษดสแดแดแดแดส",
                query="yt Ed Sheeran Perfect",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "CสษชแดAสแด Sแดแดสแดส",
                query="clipart frog",
                same_peer=True,
            ),
            Button.switch_inline(
                "OสแดษดษขแดFแดx๐ฆ",
                query="ofox beryllium",
                same_peer=True,
            ),
        ],
        [
            Button.inline(
                "ยซ Bแดแดแด",
                data="open",
            ),
        ],
    ]
    await e.edit(buttons=button, link_preview=False)


@callback("hrrrr")
@owner
async def on_plug_in_callback_query_handler(event):
    xhelps = helps.format(OWNER_NAME, len(PLUGINS))
    buttons = page_num(0, PLUGINS, "helpme", "def")
    await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)


@callback("frrr")
@owner
async def addon(event):
    halp = zhelps.format(OWNER_NAME, len(ADDONS))
    if len(ADDONS) > 0:
        buttons = page_num(0, ADDONS, "addon", "add")
        await event.edit(f"{halp}", buttons=buttons, link_preview=False)
    else:
        await event.answer(
            f"โข Tสแดแด `{HNDLR}setredis ADDONS True`\n Tแด ษขแดแด แดแดแดแดษดs แดสแดษขษชษดs",
            cache_time=0,
            alert=True,
        )


@callback("rstrt")
@owner
async def rrst(ult):
    await restart(ult)


@callback(
    re.compile(
        rb"helpme_next\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number + 1, PLUGINS, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"helpme_prev\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number - 1, PLUGINS, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"addon_next\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number + 1, ADDONS, "addon", "add")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"addon_prev\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number - 1, ADDONS, "addon", "add")
    await event.edit(buttons=buttons, link_preview=False)


@callback("back")
@owner
async def backr(event):
    xhelps = helps.format(OWNER_NAME, len(PLUGINS))
    current_page_number = int(upage)
    buttons = page_num(current_page_number, PLUGINS, "helpme", "def")
    await event.edit(
        f"{xhelps}",
        file=_file_to_replace,
        buttons=buttons,
        link_preview=False,
    )


@callback("buck")
@owner
async def backr(event):
    xhelps = zhelps.format(OWNER_NAME, len(ADDONS))
    current_page_number = int(upage)
    buttons = page_num(current_page_number, ADDONS, "addon", "add")
    await event.edit(
        f"{xhelps}",
        file=_file_to_replace,
        buttons=buttons,
        link_preview=False,
    )


@callback("open")
@owner
async def opner(event):
    bnn = asst.me.username
    buttons = [
        [
            Button.inline("โข Pสแดษขษชษดs ", data="hrrrr"),
            Button.inline("โข Aแดแดแดษดs", data="frrr"),
        ],
        [
            Button.inline("OแดกษดแดสโขTแดแดส๊ฑ", data="ownr"),
            Button.inline("IษดสษชษดแดโขPสแดษขษชษดs", data="inlone"),
        ],
        [
            Button.url(
                "โ๏ธSแดแดแดษชษดษขsโ๏ธ",
                url=f"https://t.me/{bnn}?start={ultroid_bot.me.id}",
            ),
        ],
        [Button.inline("โขโขCสแด๊ฑแดโขโข", data="close")],
    ]
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    cmd = len(z) + 10
    await event.edit(
        get_string("inline_4").format(
            OWNER_NAME,
            len(PLUGINS),
            len(ADDONS),
            cmd,
        ),
        buttons=buttons,
        link_preview=False,
    )


@callback("close")
@owner
async def on_plug_in_callback_query_handler(event):
    await event.edit(
        get_string("inline_5"),
        file=_file_to_replace,
        buttons=Button.inline("Oแดแดษด Mแดษชษด Mแดษดแด Aษขแดษชษด", data="open"),
    )


@callback(
    re.compile(
        b"def_plugin_(.*)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = f"Plugin Name - `{plugin_name}`\n"
    try:
        for i in HELP[plugin_name]:
            help_string += i
    except BaseException:
        pass
    if help_string == "":
        reply_pop_up_alert = f"{plugin_name} has no detailed help..."
    else:
        reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n BY INFINATO"
    buttons = [
        [
            Button.inline(
                "ยซ Sแดษดแด Pสแดษขษชษด ยป",
                data=f"sndplug_{(event.data).decode('UTF-8')}",
            )
        ],
        [
            Button.inline("ยซ Bแดแดแด", data="back"),
            Button.inline("โขโขCสแด๊ฑแดโขโข", data="close"),
        ],
    ]
    try:
        if event.query.user_id in sed:
            await event.edit(
                reply_pop_up_alert,
                buttons=buttons,
            )
        else:
            reply_pop_up_alert = notmine
            await event.answer(reply_pop_up_alert, cache_time=0)
    except BaseException:
        halps = f"Do .help {plugin_name} to get the list of commands."
        await event.edit(halps, buttons=buttons)


@callback(
    re.compile(
        b"add_plugin_(.*)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = ""
    try:
        for i in HELP[plugin_name]:
            help_string += i
    except BaseException:
        try:
            for u in CMD_HELP[plugin_name]:
                help_string = f"Plugin Name-{plugin_name}\n\nโ Commands Available-\n\n"
                help_string += str(CMD_HELP[plugin_name])
        except BaseException:
            try:
                if plugin_name in LIST:
                    help_string = (
                        f"Plugin Name-{plugin_name}\n\nโ Commands Available-\n\n"
                    )
                    for d in LIST[plugin_name]:
                        help_string += HNDLR + d
                        help_string += "\n"
            except BaseException:
                pass
    if help_string == "":
        reply_pop_up_alert = f"{plugin_name} has no detailed help..."
    else:
        reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n BY INFINATO"
    buttons = [
        [
            Button.inline(
                "ยซ Sแดษดแด Pสแดษขษชษด ยป",
                data=f"sndplug_{(event.data).decode('UTF-8')}",
            )
        ],
        [
            Button.inline("ยซ Bแดแดแด", data="buck"),
            Button.inline("โขโขCสแด๊ฑแดโขโข", data="close"),
        ],
    ]
    try:
        if event.query.user_id in sed:
            await event.edit(
                reply_pop_up_alert,
                buttons=buttons,
            )
        else:
            reply_pop_up_alert = notmine
            await event.answer(reply_pop_up_alert, cache_time=0)
    except BaseException:
        halps = f"Do .help {plugin_name} to get the list of commands."
        await event.edit(halps, buttons=buttons)


def page_num(page_number, loaded_plugins, prefix, type):
    number_of_rows = 5
    number_of_cols = 2
    emoji = Redis("EMOJI_IN_HELP")
    if emoji:
        multi = emoji
    else:
        multi = "โ"
    helpable_plugins = []
    global upage
    upage = page_number
    for p in loaded_plugins:
        helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                multi,
                x,
                multi,
            ),
            data=f"{type}_plugin_{x}",
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "ยซ Pสแดแด?ษชแดแดs",
                    data=f"{prefix}_prev({modulo_page})",
                ),
                Button.inline("ยซ Bแดแดแด ยป", data="open"),
                Button.inline(
                    "Nแดxแด ยป",
                    data=f"{prefix}_next({modulo_page})",
                ),
            ),
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [(Button.inline("ยซ Bแดแดแด ยป", data="open"),)]
    return pairs