# WRITE  BY HuRe
# PLUGIN FOR HuRe 
# @UI_XB

from telethon import events
import random, re
from ..Config import Config

from HuRe.utils import admin_cmd

import asyncio
from HuRe import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [
    "اللّهُم راحه مُستديمه,لا نِهاية لهـا💛🍁",
    "اللهِم  راحة بال وايّـام حلوة💛🍁",
    "اللَّهم صُب آياتِ القرآنِ في صُدورِنا صباً حتّى يُشفى بآثارِها كُل شعورٍ مُر 💛",
    "ويبقى صوت القرآن ، ماءً باردًا نقيًا ينحدر مِن السماء ليُطفئ حُزن قلبِك💛🍁",
    "اللهُـ۾ القـوّه عـند الضُـعـف💛🍁اللهُـ۾ القـوّه عـند الضُـعـف💛🍁ُ",
    "اللهُم اشغلني بذكِرك عن كُل ذكِر💛🍁",
    "اللهم انزع من قلبي حب كل شيء لا تحبه💝ِهِ",
    "‏اللهّم أجبُرني جبرًا يُعوضُ قلبي عن كُل شيءو",
    "- هذِهِ الدُّنيا سَراب بينَ آتٍ ومُودِّع ما خُلِقنَا الله للبقاء نَحنُ للّٰهِ سَنَرجِع .",
    "ماسكن القرآن قلباً إلا قوّاه ونقّاه وثبته .🤍ه",
    "من يترك كل شي في يدِ الله ، سيرى يد الله في كلّ شيءٍ..🤍🪐َّ",
    "من أخفى عن الناس همّه متوكلاً على الله، كفاه الله ما أهمّهُ وأرضاه ❤🌿.",
    "كانَ مهمومًا، ولكنّ قلبهُ يطمئنّ حين يصلّي على النبي ﷺ.🤍ٌ",
    "‏نحن مدينون بالحب لكل من جعلنا نبصر شيئًا جميلًا في أنفسنا حين أوشكنا على الإنطفاء",
    "- حُلمي وإن طالَ المدى سأنالهُ، ما دامَ لي فوقَ السَّماءِ معينُ💜.ه",
    "اللهم إنّا مقصرون وأنت الكريم، ومذنبون وأنت الحليم، وفقراء إليك وأنت الغني عنّا، اللهم تجاوز عنا بعفوك ومغفرتك. 《 ‏-آمين 》",
    "ما ضرك لو أطفأ هذا العالمُ أنوارهُ كلها في وجهك؛ ما دام نورُ اللهِ في قلبِكَ متوهّجًا؟🤍",
    "لعل الله في هذا اليوم يدبر لك شئياً يرضيك به ، شيئاً يجعلك تسجد فرحاً لحدوثه♥️🌿",
]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lMl10l = random.choice(rehu)
        await event.edit(
        f": **⦑ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐈𝐍 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 ⦒**\n☆•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n( `.م1` )  ⦙ **اوامر الادمن**\n( `.م2` )  ⦙ **اوامر المجموعة**\n( `.م3` )  ⦙ **اوامر الترحيب والردود**\n( `.م4` )  ⦙ **حماية خاص والتلكراف**\n( `.م5` )  ⦙ **اوامر المنشن والانتحال**\n( `.م6` )  ⦙ **اوامر التحميل والترجمة**\n( `.م7` )  ⦙ **اوامر المنع و القفل**\n( `.م8` )  ⦙ **اوامر التنظيف والتكرار**\n( `.م9` )  ⦙ **اوامر التخصيص والفارات**\n( `.م10` ) ⦙ **اوامر الوقتي و التشغيل**\n( `.م11` ) ⦙ **اوامر الكشف و الروابط**\n( `.م12` ) ⦙ **اوامر المساعدة والإذاعة** \n( `.م13` ) ⦙ **اوامر الارسال والاذكار**\n( `.م14` ) ⦙ **اوامر المـلصقات وكوكل**\n( `.م15` ) ⦙ **اوامر التسلية والميمز والتحشيش** \n( `.م16` ) ⦙ **اوامر الصيغ والجهات**\n( `.م17` ) ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n( `.م18` ) ⦙ **اوامر الحساب والترفيه**\n( `.م19` ) ⦙ **اوامر الميوزك والتشغيل**\n( `.م20` ) ⦙ **اوامر بصمات الميمز**\n( `.م21` ) ⦙ **اوامر تجميع النقاط وبوت وعد**\n☆•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n **۞︙ {lMl10l} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس  زد إي **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس  زد إي **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n۞︙ اختر احدى هذه الاوامر\n ۞︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n- ( `.بصمات انمي` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر تجميع النقاط و بوت وعد **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التجميع` ) \n- ( `.اوامر وعد` ) \n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"

)
@l313l.ar_cmd(
    pattern="م22$",
    command=("م22", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** اوامر ميمز 1 **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه الاوامر\n\n  1- .عيب\n 2- .اجمد كده\n 3- .يالهوي\n 4- .احترمي نفسك\n 5- .مينفعش\n 6- .مديك قلبي\n 7- .اهلا بيك\n 8- .هعوره\n 9- .خد نفس\n 10- .حفل\n 11- .امال\n 12- .هتولعو\n 13- .انا تعبان\n 14- .عملت اي\n 15- .المخدرات\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"
)
@l313l.ar_cmd(
    pattern="م23$",
    command=("م23", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** اوامر ميمز 2 **:\n ☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n ۞︙ اختر احدى هذه الاوامر\n\n  1- .يا مرا\n 2- .بتحرجني\n 3- .انضف\n 4- .هنضحك\n 5- .يا راجل\n 6- .موزه\n 7- .انا فين\n 8- .خلصانه\n☆•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•☆\n⌔︙CH : @UI_XB"


        )
