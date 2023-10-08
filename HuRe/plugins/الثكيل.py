#ياقائم آل محمد
#ربي اشرح لي صدري
#تمت كتابة الكود من قبل الهيبه مودي @UP_UO
#فريق زد إي @UI_XB
import asyncio
from telethon import events
from HuRe import l313l

mody_enabled = False
ze_enabled = False
ZE_ID = {}

@l313l.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global ze_enabled, ZE_ID
    sender_id = event.sender_id
    if ze_enabled and sender_id in ZE_ID:
        joker_time = ZE_ID[sender_id]
        if joker_time > 0:
            await asyncio.sleep(joker_time)
        await event.mark_read()

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر تعطيل$'))
async def Mody(event):
    global ze_enabled
    ze_enabled = False
    await event.edit('**۞︙ تم تعطيل امر التكبر بنجاح ✅**')

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر (\d+) (\d+)$'))
async def Mody(event):
    global ze_enabled, ZE_ID
    joker_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    ZE_ID[user_id] = joker_time
    ze_enabled = True
    await event.edit(f'**۞︙ تم تفعيل امر التكبر بنجاح مع  {joker_time} ثانية للمستخدم {user_id}**')

@l313l.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def Mody(event):
    global mody_enabled
    if mody_enabled:
        if mody_time > 0:
            await asyncio.sleep(mody_time)
        await event.mark_read()

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر تعطيل$'))
async def Mody(event):
    global mody_enabled
    mody_enabled = False
    await event.edit('**۞︙ تم تعطيل امر التكبر على الجميع بنجاح ✅**')

@l313l.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر (\d+)$'))
async def Mody(event):
    global mody_enabled
    mody_time = int(event.pattern_match.group(1))
    mody_enabled = True
    await event.edit(f'**۞︙ تم تفعيل امر التكبر بنجاح مع  {delay_time} ثانية**')
