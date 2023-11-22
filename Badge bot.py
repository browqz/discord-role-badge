import discord
import asyncio

intents = discord.Intents.default()
intents.members = True

TOKEN = 'TON_TOKEN'
client = discord.Client(intents=intents)

async def check_badges():
    await client.wait_until_ready()
    while not client.is_closed():
        await asyncio.sleep(10)

        guild_id = 1168506431964717126
        guild = client.get_guild(guild_id)

        if guild:
            for member in guild.members:
                user_badges = get_badges(member)
                for badge in user_badges:
                    await add_role_by_badge(member, badge)

async def add_role_by_badge(member, badge_name):
    guild = member.guild
    badge_roles = {
        'bug_hunter': ID_ROLE,
        'bug_hunter_level_2': ID_ROLE,
        'hypesquad': ID_ROLE,
        'verified_bot_developer': ID_ROLE,
        'discord_certified_moderator': ID_ROLE,
        'partner': ID_ROLE,
        'early_supporter': ID_ROLE
    }
    if badge_name in badge_roles:
        role_id = badge_roles[badge_name]
        role = guild.get_role(role_id)
        if role:
            await member.add_roles(role)
            print(f"Le rôle {badge_name} a été ajouté à {member.name}")

def get_badges(member):
    badges = []
    flags = member.public_flags

    if flags.early_supporter:
        badges.append('early_supporter')

    if flags.bug_hunter:
        badges.append('bug_hunter')

    if flags.bug_hunter_level_2:
        badges.append('bug_hunter_level_2')

    if flags.hypesquad:
        badges.append('hypesquad')

    if flags.verified_bot_developer:
        badges.append('verified_bot_developer')

    if flags.discord_certified_moderator:
        badges.append('discord_certified_moderator')

    if flags.partner:
        badges.append('partner')

    return badges

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='quelamif.net', url="https://www.twitch.tv/browqz"))
    print('Bot is ready')
    client.loop.create_task(check_badges())

client.run(TOKEN)
