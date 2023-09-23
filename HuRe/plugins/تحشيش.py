import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from HuRe import l313l
from random import choice
from l313l.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



#كـتابة المـلف وتعديل.    :   مودي.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح
rehu = [
    "شكم مره كتلك خلي نفلش الكروب",
    "باع هذا اللوكي شديسوي",
    "** مالك الكروب واحد زباله ويدور بنات **",
    "**اول مره اشوف بنات يدورن ولد 😂 **",
    "**شوف هذا الكرنج دين مضال براسه**",
    "**انته واحد فرخ وتنيج**",
    "** راح اعترفلك بشي طلعت احب اختك 🥺 **",
    "**مالك الكروب والمشرفين وفرده من قندرتك ضلعي**",
    "**هذا واحد غثيث وكلب ابن كلب**",
    "**لتحجي كدامه هذا نغل يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**لو ربك يجي ماتنكشف الهمسه 😂😂**",
]

@l313l.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"🚻 ** ۞︙  المستخدم => • ** [{HuRe}](tg://user?id={user.id}) \n ☑️ **۞︙  تم رفعها مرتك بواسطه  :**{my_mention} 👰🏼‍♀️.\n**۞︙  يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@l313l.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**۞︙  خليه خله ينبح 😂**")

@l313l.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"۞︙ المستخدم [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@l313l.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"۞︙ المستخدم [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه قرد واعطائه موزة 🐒🍌 بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention} \n**۞︙  انت حبي الابدي 😍**")
    
    

@l313l.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه مطي 🐴 بواسطة :** {my_mention} \n**۞︙  تعال حبي استلم  انه **")
    
#كـتابة المـلف وتعديل.    :   مودي.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح


@l313l.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه زوجج بواسطة :** {my_mention} \n**۞︙  يلا حبيبي امشي نخلف 🤤🔞**")
    

@l313l.on(admin_cmd(pattern="رفع زاحف(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفع المتهم زاحف اصلي بواسطة :** {my_mention} \n**۞︙  ها يلزاحف شوكت تبطل سوالفك حيوان 😂🐍**")

@l313l.on(admin_cmd(pattern="رفع كحبة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفع المتهم كحبة 👙 بواسطة :** {my_mention} \n**۞︙  ها يلكحبة طوبز خلي انيجك/ج**")

@l313l.on(admin_cmd(pattern="رفع فرخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه فرخ الكروب بواسطة :** {my_mention} \n**۞︙  لك الفرخ استر على خمستك ياهو اليجي يزورهاً 👉🏻👌🏻**")

@l313l.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"۞︙ ولك [{tag}](tg://user?id={user.id}) \n۞︙  هيو لتندك بسيادك لو بهاي 👞👈")

@l313l.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـها حاته الكروب 🤤😻 بواسطة :** {my_mention} \n**۞︙  تعاي يعافيتي اريد حضن دافي 😽**")

@l313l.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه المتهم هايشة 🐄 بواسطة :** {my_mention} \n**۞︙  ها يلهايشة خوش بيك حليب تعال احلبك 😂**")

@l313l.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه صاك 🤤 بواسطة :** {my_mention} \n**۞︙  تعال يلحلو انطيني بوسة من رگبتك 😻🤤**")

@l313l.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]*)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ تعال مصه عزيزي ** [{tag}](tg://user?id={user.id})")

@l313l.on(admin_cmd(pattern="سيد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"سماحة مودي علي مطور سورس  زد إي @UI_XB")

@l313l.on(admin_cmd(pattern="رفع ايجة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه ايچة 🤤 بواسطة :** {my_mention} \n**۞︙  ها يلأيچة تطلعين درب بـ$25 👙**")

@l313l.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعـه زبال الكروب 🧹 بواسطة :** {my_mention} \n**۞︙  تعال يلزبال اكنس الكروب لا أهينك 🗑😹**")

@l313l.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعه كواد بواسطة :** {my_mention} \n**۞︙  تعال يكواد عرضك مطشر اصير حامي عرضك ؟😎**")

@l313l.on(admin_cmd(pattern="رفع ديوث(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ المستخدم** [{HuRe}](tg://user?id={user.id}) \n**۞︙  تـم رفعه ديوث الكروب بواسطة :** {my_mention} \n**۞︙  تعال يلديوث جيب اختك خلي اتمتع وياها 🔞**")

@l313l.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ الحلو** 「[{HuRe}](tg://user?id={user.id})」 \n**۞︙  تـم رفعه مميز بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ الحلو** 「[{HuRe}](tg://user?id={user.id})」 \n**۞︙  تـم رفعه ادمن بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ الحلو** 「[{HuRe}](tg://user?id={user.id})」 \n**۞︙  تـم رفعه منشئ بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6509622797:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    HuRe = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙ الحلو** 「[{HuRe}](tg://user?id={user.id})」 \n**۞︙  تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" ** ۞︙  المستخدم => • ** [{HuRe}](tg://user?id={user.id}) \n ☑️ **۞︙  تم رفعه مجنب بواسطه  :**{my_mention} .\n**۞︙  كوم يلمجنب اسبح مو عيب تضرب جلغ 😹** ")

@l313l.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ۞︙  المستخدم => • ** [{HuRe}](tg://user?id={user.id}) \n ☑️ **۞︙  تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**۞︙  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@l313l.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"۞︙ ** لقد تم زواجك/ج من : **[{HuRe}](tg://user?id={user.id}) 💍\n**۞︙  الف الف مبروك الان يمكنك اخذ راحتك ** ")

@l313l.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**۞︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
lMl10l = [1374312239, 393120911, 6509622797, 5564802580]
@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in lMl10l:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == l313l.uid:
           if event.message.message == "منصب؟":
               await event.reply("**يب منصب ✓**")
           elif event.message.message == "منو فخر العرب؟":
               await event.reply("**الأمام علي عليه الصلاة والسلام ❤️**")
           elif event.message.message == "منو تاج راسك":
               await event.reply("** مودي @UP_UO تاج راسي ❤️**")
@l313l.on(admin_cmd(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    HuRe = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    lMl10l = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**۞︙الهمسة من المستخدم [{HuRe}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**۞︙  الهمسة هي : {lMl10l} ** ")
@l313l.on_message(filters.command("اجمد كده", prefixes=f".") & filters.me)
async def agmad(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/78")        

@l313l.on_message(filters.command("يالهوي", prefixes=f".") & filters.me)
async def yalhowe(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/79")      
     
@l313l.on_message(filters.command("احترمي نفسك", prefixes=f".") & filters.me)
async def ehtrmy(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/108")           
     
@l313l.on_message(filters.command("عيب", prefixes=f".") & filters.me)
async def eeeb(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/105")          
     
@l313l.on_message(filters.command("مينفعش", prefixes=f".") & filters.me)
async def maynah(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/97")  

@l313l.on_message(filters.command("مديك قلبي", prefixes=f".") & filters.me)
async def alby(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/91")      
     
@l313l.on_message(filters.command("اهلا بيك", prefixes=f".") & filters.me)
async def ahlnbek(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/92")      
     
@l313l.on_message(filters.command("هعوره", prefixes=f".") & filters.me)
async def hworo(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/82")       
     
@l313l.on_message(filters.command("حفل", prefixes=f".") & filters.me)
async def kfel(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/97")                
     
@l313l.on_message(filters.command("خد نفس", prefixes=f".") & filters.me)
async def nafs(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/83")    
     
@l313l.on_message(filters.command("امال", prefixes=f".") & filters.me)
async def omal(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/88")             
     
@l313l.on_message(filters.command("هتولعو", prefixes=f".") & filters.me)
async def yyleh(c, msg):        
     await msg.reply_voice("https://t.me/UI3I3/106")    
                             
@l313l.on_message(filters.command("انا تعبان", prefixes=f".") & filters.me)
async def taban(c, msg):        
     await msg.reply_voice("https://t.me/UI3I3/101")    
     
@l313l.on_message(filters.command("عملت اي", prefixes=f".") & filters.me)
async def anaemlt(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/104")         
     
@l313l.on_message(filters.command("المخدرات", prefixes=f".") & filters.me)
async def mokde(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/102")       
     
@l313l.on_message(filters.command("يا مرا", prefixes=f".") & filters.me)
async def mrara(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/95")  
     
@l313l.on_message(filters.command("بتحرجني", prefixes=f".") & filters.me)
async def aklak(c, msg):     
     await msg.reply_voice("https://t.me/UI3I3/77")      
     
@l313l.on_message(filters.command("انضف", prefixes=f".") & filters.me)
async def endaf(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/98")      
                                                                                                            
@l313l.on_message(filters.command("هنضحك", prefixes=f".") & filters.me)
async def hantk(c, msg):    
     await msg.reply_voice("https://t.me/UI3I3/100")      
     
@l313l.on_message(filters.command("يا راجل", prefixes=f".") & filters.me)
async def ragel(c, msg):       
     await msg.reply_voice("https://t.me/UI3I3/87")

@l313l.on_message(filters.command("موزه", prefixes=f".") & filters.me)
async def moza(c, msg):       
     await msg.reply_voice("https://t.me/UI3I3/73")          
 
@l313l.on_message(filters.command("انا فين", prefixes=f".") & filters.me)
async def feen(c, msg):       
     await msg.reply_voice("https://t.me/UI3I3/75")

@l313l.on_message(filters.command("خلصانه", prefixes=f".") & filters.me)
async def hossam(c, msg):       
     await msg.reply_voice("https://t.me/UI3I3/74")
