# -*- coding: utf8 -*-
import discord
from discord.ext import commands
import asyncio


token = 'Nzk3MTQyNDg1NzE3NDgzNTUw.X_iKyg.WXkjvZEf9duMtnNqpi0xzGpju0Y'
bot = commands.Bot(command_prefix = "!")
@bot.event
async def on_ready():
    print('Бот "Game UPS" успешно запущен!')
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game('SCP:Secret Laboratory'))    
@bot.command(pass_context=True)
async def inf(ctx,*args):     
    embed=discord.Embed(title="Информация о командах.", description="Информация о сервере Game UPS\nUbgrade\nPlayer\nStats\nКоманды:\ninf - показать это сообщение.\nrule - Правила нашего сервера Discord\nrule2 - Правила нашего сервера Discord\ninrole - Информация о всех ролях\ninrole2 - Информация о всех направлениях", colour=0xff0000)
    embed.set_author(name="Tix_Fresh#6996")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def rule(ctx,*args):
    embed=discord.Embed(title="Правила нашего сервера.Страница 1", description="правила категории Ч-чат.\nНе мешай другим игрокам общаться в чате,\nне груби, не спамь и тогда всем будет приятно.\n\nЧ1-Запрещенно оскорблять игроков.\nЧ2-Запрещенно спамить.\nПример: Игрок 10 раз подряд пишет:\nГДЕ ПРАВИЛА?\n\nЧ3-запрещенна реклама сторонних проектов.\nпример: Игрок рассказывает, о другом\nдискорд сервере.\n", color=0xff0000)
    embed.set_author(name="Tix_Fresh#6996")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def rule2(ctx,*args):      
    embed = discord.Embed(title="Правила нашего сервера.Страница 2", description="Правило категории О-отношение к игрокам.\nЗнай свои права, не перебивай собеседника, не груби\nи общайся спокойно.\n\nО1-Запрещенно токсичить при беседе с игроками.\nПример: Игрок обзывает других игроков за то-что\nу них нету чего-то.\n\nО2-Запрещенно попрошайничать в любом виде.\nПример: Игрок просит что-бы ему подарили\nдискорд нитро.\n\nО3-запрещенно призывать уйти с сервера нарушать правила и т.д.\nПример: Игрок говорит, о том что здесь все ужасно и привлекает\nигроков нарушать правила и выходить с сервера.\n\nО4-Запрещенно устраивать травлю игроку (неважно личное не личное)\nПример: Игрок оскорбляет и унижает другого\nигрока за то-что он сломал ему дом в майнкрафте.\n\nО5-Запрещенно нарушать правила по просьбе\nдругого игрока.\n\n\nПравила категории П-прочее.\nП1-Запрещенно одновременно подавать сразу больше 1 заявки на роль.", color=0xff0000)
    embed.set_author(name="Tix_Fresh#6996")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def inrole(ctx,*args):
    embed = discord.Embed(title="Информация о ролях", description="Участник - выдается при входе на сервер.\nСотрудник - выдается при входе в коллектив\nСтажер - испытательный срок для нашего сотрудника,\n писать в <#776161259170693170>.\nАдминистратор - следит за выполнением правил на наших серверах,\n писать в <#776161259170693170>.\nКоординатор - следит за администраторами,\n писать в <#776161259170693170>.\nОтдел кадров - принимает заявки, следит за сервером и т.д;\n писать в <#776161259170693170>.\n",color=0xff0000)
    embed.set_author(name="Tix_Fresh#6996")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def inrole2(ctx,*args):
    embed=discord.Embed(title="Информация о направлениях", description="IT-направление - Человек который знает хотябы один язык програмирования.\nIT-python - Человек знающий язык програмирования python.\nIT-skratch - Человек знающий язык програмирования skratch.", color=0xff0000)
    embed.set_author(name="Tix_Fresh#6996")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def Ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mute = discord.utils.get(ctx.message.guild.roles,name="🔇Mute")
    await member.add_roles(mute)
    await asyncio.sleep(20)
    await ctx.send(f'{member.mention} замучен на пол-часа!')
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx,amount = 1000): 
    await ctx.channel.purge(limit=amount)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def стажер(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "стажер")
    await member.add_roles(mod)
    retStr = (f"""```{member} получил роль стажера!```""")
    embed=discord.Embed(title="new role",colour = discord.Colour.red())
    embed.add_field(name="стажер",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def r_стажер(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "стажер")
    await member.remove_roles(mod)
    retStr = (f"""```{member} был снят с роли стажера!```""")
    embed = discord.Embed(title="remove role",colour = discord.Colour.blue())
    embed.add_field(name="remove role",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def администратор(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "администратор")
    await member.add_roles(mod)
    retStr = (f"""```{member} получил роль администратора!```""")
    embed=discord.Embed(title="new role",colour = discord.Colour.red())
    embed.add_field(name="moder",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def r_администратор(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "администратор")
    await member.remove_roles(mod)
    retStr = (f"""```{member} был снят с роли администратора!```""")
    embed = discord.Embed(title="remove role",colour = discord.Colour.blue())
    embed.add_field(name="remove role",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def отдел_кадров(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "отдел кадров")
    await member.add_roles(mod)
    retStr = (f"""```{member} получил роль отдел кадров!```""")
    embed=discord.Embed(title="new role",colour = discord.Colour.red())
    embed.add_field(name="moder",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def r_отдел_кадров(ctx,member:discord.Member):
    await ctx.channel.purge(limit=1)
    mod = discord.utils.get(ctx.message.guild.roles,name = "отдел кадров")
    await member.remove_roles(mod)
    retStr = (f"""```{member} был снят с роли отдел кадров!```""")
    embed = discord.Embed(title="remove role",colour = discord.Colour.blue())
    embed.add_field(name="remove role",value=retStr)
    await ctx.send(embed=embed)
bot.run(token) 