# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import random
import re
import time
from datetime import datetime
from math import ceil
from platform import python_version as PyVer

from git import Repo
from pyUltroid import __version__ as UltVer
from support import *
from telethon import Button, __version__
from telethon.tl.types import InputWebDocument

from . import *

# ================================================#
notmine = f"This bot is for {OWNER_NAME}"
ULTROID_PIC = "https://telegra.ph/file/eae11a10fe0d71b59e8ef.jpg"
helps = get_string("inline_1")

add_ons = udB.get("ADDONS")
if add_ons == "True" or add_ons is None:
    zhelps = get_string("inline_2")
else:
    zhelps = get_string("inline_3")
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
            ultroid_version,
            UltVer,
            uptime,
            PyVer(),
            __version__,
            Repo().active_branch,
        )
        res = [
            await b.article(
                title="TG-Troid Userbot",
                url="https://t.me/danumabots",
                description="Userbot | Telethon ",
                text=ALIVEMSG,
                thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                buttons=[
                    [Button.url(text="Support Group", url="t.me/danuma01")],
                    [
                        Button.url(
                            text="Repo",
                            url="https://github.com/SLdevilX/TG-Troid",
                        ),
                    ],
                ],
            ),
        ]
        await o.answer(res, switch_pm=f"???? TG-Troid PORTAL", switch_pm_param="start")


if asst.me is not None:

    @inline
    @in_owner
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id in sed and query.startswith("tgtd"):
            z = []
            for x in LIST.values():
                for y in x:
                    z.append(y)
            cmd = len(z) + 10
            bnn = asst.me.username
            result = builder.article(
                title="Help Menu",
                description="Help Menu - UserBot | Telethon ",
                url="https://t.me/TheUltroid",
                thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                text=get_string("inline_4").format(
                    OWNER_NAME,
                    len(PLUGINS) - 5,
                    len(ADDONS),
                    cmd,
                ),
                buttons=[
                    [
                        Button.inline("??? P???????????s", data="hrrrr"),
                        Button.inline("??? A???????????s", data="frrr"),
                    ],
                    [
                        Button.inline("O???????????????????????????", data="ownr"),
                        Button.inline("I??????????????P???????????s", data="inlone"),
                    ],
                    [
                        Button.url(
                            "??????S???????????????s??????",
                            url=f"https://t.me/{bnn}?start=set",
                        ),
                    ],
                    [Button.inline("??????C?????????????????", data="close")],
                ],
            )
            await event.answer([result] if result else None)
        elif event.query.user_id in sed and query.startswith("paste"):
            ok = query.split("-")[1]
            link = f"https://nekobin.com/{ok}"
            link_raw = f"https://nekobin.com/raw/{ok}"
            result = builder.article(
                title="Paste",
                text="P???s????????? T??? N???????????????!",
                buttons=[
                    [
                        Button.url("NekoBin", url=f"{link}"),
                        Button.url("Raw", url=f"{link_raw}"),
                    ],
                ],
            )
            await event.answer([result] if result else None)

    @callback("ownr")
    @owner
    async def setting(event):
        await event.edit(
            buttons=[
                [
                    Button.inline("???P?????????", data="pkng"),
                    Button.inline("???U?????????????????", data="upp"),
                ],
                [Button.inline("???R???s??????????????", data="rstrt")],
                [Button.inline("<- B?????????", data="open")],
            ],
        )

    @callback("pkng")
    async def _(event):
        start = datetime.now()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        pin = f"????P?????? = {ms}ms"
        await event.answer(pin, cache_time=0, alert=True)

    @callback("upp")
    async def _(event):
        uptime = grt(time.time() - start_time)
        pin = f"????U?????????????? = {uptime}"
        await event.answer(pin, cache_time=0, alert=True)

    @callback("inlone")
    @owner
    async def _(e):
        button = [
            [
                Button.switch_inline(
                    "S???????? O???????????????? P???????????s",
                    query="send",
                    same_peer=True,
                ),
            ],
            [
                Button.switch_inline(
                    "P??????? S??????????? A??????s",
                    query="app telegram",
                    same_peer=True,
                ),
                Button.switch_inline(
                    "M??????????????? A??????s",
                    query="mods minecraft",
                    same_peer=True,
                ),
            ],
            [
                Button.switch_inline(
                    "S????????????? O?? G?????????????",
                    query="go Danuma group",
                    same_peer=True,
                ),
                Button.switch_inline(
                    "S????????????? O?? Y???????????",
                    query="yahoo Danuma group",
                    same_peer=True,
                ),
            ],
            [
                Button.switch_inline(
                    "Y??????T???????? D????????????????????????",
                    query="yt Ed Sheeran Perfect",
                    same_peer=True,
                ),
            ],
            [
                Button.switch_inline(
                    "C???????A????? S?????????????",
                    query="clipart frog",
                    same_peer=True,
                ),
                Button.switch_inline(
                    "O????????????F???x????",
                    query="ofox beryllium",
                    same_peer=True,
                ),
            ],
            [
                Button.inline(
                    "<- B?????????",
                    data="open",
                ),
            ],
        ]
        await e.edit(buttons=button, link_preview=False)

    @callback("hrrrr")
    @owner
    async def on_plug_in_callback_query_handler(event):
        xhelps = helps.format(OWNER_NAME, len(PLUGINS) - 5)
        buttons = paginate_help(0, PLUGINS, "helpme")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("frrr")
    @owner
    async def addon(event):
        halp = zhelps.format(OWNER_NAME, len(ADDONS))
        if len(ADDONS) > 0:
            buttons = paginate_addon(0, ADDONS, "addon")
            await event.edit(f"{halp}", buttons=buttons, link_preview=False)
        else:
            await event.answer(
                f"??? T???????? `{HNDLR}setredis ADDONS True`\n T??? ???????? ??????????????s ??????????????s",
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
        buttons = paginate_help(current_page_number + 1, PLUGINS, "helpme")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"helpme_prev\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number - 1, PLUGINS, "helpme")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"addon_next\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_addon(current_page_number + 1, ADDONS, "addon")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"addon_prev\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_addon(current_page_number - 1, ADDONS, "addon")
        await event.edit(buttons=buttons, link_preview=False)

    @callback("back")
    @owner
    async def backr(event):
        xhelps = helps.format(OWNER_NAME, len(PLUGINS) - 5)
        current_page_number = int(upage)
        buttons = paginate_help(current_page_number, PLUGINS, "helpme")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("buck")
    @owner
    async def backr(event):
        xhelps = zhelps.format(OWNER_NAME, len(ADDONS))
        current_page_number = int(addpage)
        buttons = paginate_addon(current_page_number, ADDONS, "addon")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("open")
    @owner
    async def opner(event):
        bnn = asst.me.username
        buttons = [
            [
                Button.inline("??? P???????????s ", data="hrrrr"),
                Button.inline("??? A???????????s", data="frrr"),
            ],
            [
                Button.inline("O?????????????T???????????", data="ownr"),
                Button.inline("I??????????????P???????????s", data="inlone"),
            ],
            [
                Button.url(
                    "??????S???????????????s??????",
                    url=f"https://t.me/{bnn}?start={ultroid_bot.me.id}",
                ),
            ],
            [Button.inline("??????C?????????????????", data="close")],
        ]
        z = []
        for x in LIST.values():
            for y in x:
                z.append(y)
        cmd = len(z) + 10
        await event.edit(
            get_string("inline_4").format(
                OWNER_NAME,
                len(PLUGINS) - 5,
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
            buttons=Button.inline("O???????? M??????? M???????? A?????????", data="open"),
        )

    @callback(
        re.compile(
            b"us_plugin_(.*)",
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
        reply_pop_up_alert += "\n?? @TeamUltroid"
        try:
            if event.query.user_id in sed:
                await event.edit(
                    reply_pop_up_alert,
                    buttons=[
                        Button.inline("<- B?????????", data="back"),
                        Button.inline("??????C?????????????????", data="close"),
                    ],
                )
            else:
                reply_pop_up_alert = notmine
                await event.answer(reply_pop_up_alert, cache_time=0)
        except BaseException:
            halps = f"Do .help {plugin_name} to get the list of commands."
            await event.edit(halps)

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
                    help_string = (
                        f"Plugin Name-{plugin_name}\n\n??? Commands Available-\n\n"
                    )
                    help_string += str(CMD_HELP[plugin_name])
            except BaseException:
                try:
                    if plugin_name in LIST:
                        help_string = (
                            f"Plugin Name-{plugin_name}\n\n??? Commands Available-\n\n"
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
        reply_pop_up_alert += "\n?? @TeamUltroid"
        try:
            if event.query.user_id in sed:
                await event.edit(
                    reply_pop_up_alert,
                    buttons=[
                        Button.inline("<- B?????????", data="buck"),
                        Button.inline("??????C?????????????????", data="close"),
                    ],
                )
            else:
                reply_pop_up_alert = notmine
                await event.answer(reply_pop_up_alert, cache_time=0)
        except BaseException:
            halps = f"Do .help {plugin_name} to get the list of commands."
            await event.edit(halps)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 2
    emoji = Redis("EMOJI_IN_HELP")
    if emoji:
        multi, mult2i = emoji, emoji
    else:
        multi, mult2i = "???", "???"
    helpable_plugins = []
    global upage
    upage = page_number
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                random.choice(list(multi)),
                x,
                random.choice(list(mult2i)),
            ),
            data=f"us_plugin_{x}",
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
                    "<- P????????????????s",
                    data=f"{prefix}_prev({modulo_page})",
                ),
                Button.inline("-B?????????-", data="open"),
                Button.inline(
                    "N???x??? ->",
                    data=f"{prefix}_next({modulo_page})",
                ),
            ),
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [(Button.inline("-B?????????-", data="open"),)]
    return pairs


def paginate_addon(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 2
    emoji = Redis("EMOJI_IN_HELP")
    if emoji:
        multi, mult2i = emoji, emoji
    else:
        multi, mult2i = "???", "???"
    helpable_plugins = []
    global addpage
    addpage = page_number
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                random.choice(list(multi)),
                x,
                random.choice(list(mult2i)),
            ),
            data=f"add_plugin_{x}",
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
                    "<- P????????????????s",
                    data=f"{prefix}_prev({modulo_page})",
                ),
                Button.inline("-B?????????-", data="open"),
                Button.inline(
                    "N???x??? ->",
                    data=f"{prefix}_next({modulo_page})",
                ),
            ),
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [(Button.inline("-B?????????-", data="open"),)]
    return pairs
