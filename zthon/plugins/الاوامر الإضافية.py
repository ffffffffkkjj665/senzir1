from ..core.managers import edit_or_reply
from . import zedub

# الأمر .م30
ZelzalDV_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝐑𝐄𝐅𝐙 - التحديثات الجديدة ](t.me/def_Zoka) 𓆪\n\n"
    "⪼تم اضافه امر .بعصه\n"
    "⪼تم اضافه امر .شطان\n"
    "⪼تم اضافه امر .انطق\n"
    "⪼سيتم اضافه الاوامر الاخرى قريبا\n"
    "\n𓆩 [𐇮 𝙎𓏺𝞝𝙉𝙕𝙄𝙍 الهہـيـٖ͡ـ͢ـبـه 𐇮](t.me/senzir1) 𓆪"
)

@zedub.zed_cmd(pattern="م30")
async def cmd_30(event):
    await edit_or_reply(event, ZelzalDV_cmd)


# الأمر .م31 - رسالة مختلفة
ZelzalDV_cmd_2 = (
    "📢 هذا أمر جديد .م31\n"
    "⪼ يعرض لك معلومات أخرى هنا.\n"
    "⪼ يمكنك تعديله كما تشاء.\n"
    "⪼ شكراً لاستخدامك البوت!"
)

@zedub.zed_cmd(pattern="م31")
async def cmd_31(event):
    await edit_or_reply(event, ZelzalDV_cmd_2)
    
