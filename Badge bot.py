import discord

intents = discord.Intents.default()
intents.members = True

TOKEN = 'MTEyODgzMzI4MTY0Nzk3NjQ2OQ.Gbq2IM.6iqnJpliBOsVkwG_HwjkN42OHDpfBFw9EcfECw'
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='quelamif.net', url="https://www.twitch.tv/browqz"))
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
        'bug_hunter': 1176098368053846057,
        'bug_hunter_level_2': 1176099094704427028,
        'hypesquad': 1176097855174352949,
        'verified_bot_developer': 1176098556562653224,
        'discord_certified_moderator': 1176098941352296520,
        'partner': 1176101875305697280,
        'early_supporter': 1176086073567354920
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

client.run(TOKEN)