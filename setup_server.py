"""Non-destructive Discord server setup for State 157 (discord.py 2.x)."""
import os
import asyncio
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN', '').strip()
GUILD_ID = os.getenv('DISCORD_GUILD_ID', '').strip()
if not TOKEN or not GUILD_ID.isdigit():
    raise SystemExit('Fill DISCORD_BOT_TOKEN and numeric DISCORD_GUILD_ID in .env first.')

ROLE_SPECS = [
    ('Administrator', 0xE74C3C),
    ('State Moderator', 0x3498DB),
    ('NAP 10 Council', 0xF1C40F),
    ('Alliance Leader', 0x9B59B6),
    ('Alliance Officer', 0x1ABC9C),
    ('9DL | LEGENDS', 0xE67E22),
    ('State Member', 0x95A5A6),
]

SECTIONS = [
    ('📌 START HERE', [
        ('👋・welcome', 'Welcome to State 157. Start here.'),
        ('📜・server-rules', 'Community guidelines and server rules.'),
        ('✅・verification', 'Verification instructions and assistance.'),
        ('🌍・select-language', 'Choose your language; translation tools are coming soon.'),
        ('📢・announcements', 'Official State 157 announcements.'),
    ], 'public'),
    ('🌐 STATE COMMUNITY', [
        ('💬・general-chat', 'Community discussion for all alliances.'),
        ('🌎・international-chat', 'International communication across State 157.'),
        ('🏰・alliance-recruitment', 'Alliance recruitment and applications.'),
        ('📸・media-sharing', 'Share screenshots and achievements.'),
        ('💡・suggestions', 'Suggest improvements to our community.'),
    ], 'public'),
    ('🛡️ NAP 10 INFORMATION', [
        ('📜・nap10-rules', 'Official approved NAP 10 regulations.'),
        ('📢・nap10-announcements', 'NAP 10 public updates.'),
        ('⚖️・report-violations', 'How to report an alleged NAP violation privately.'),
    ], 'public'),
    ('👑 NAP 10 COUNCIL', [
        ('💬・council-chat', 'Private NAP 10 council discussion.'),
        ('🗳️・council-voting', 'Private council votes.'),
        ('🤝・diplomacy', 'Private diplomatic coordination.'),
        ('📋・council-records', 'Private council decisions and records.'),
    ], 'council'),
    ('⚔️ STATE EVENTS', [
        ('📅・event-schedule', 'Upcoming events and schedules.'),
        ('🏆・capitol-war', 'Capitol event information and coordination.'),
        ('🎯・event-coordination', 'Event planning and participation.'),
    ], 'public'),
    ('🛠️ STAFF ONLY', [
        ('🛡️・staff-chat', 'Private moderation discussion.'),
        ('📋・moderation-logs', 'Private moderation records.'),
        ('🎫・support-tickets', 'Private staff support coordination.'),
    ], 'staff'),
]

POSTS = {
    '👋・welcome': ('🌍 **WELCOME TO STATE 157 | OFFICIAL COMMUNITY**\n'
        'A neutral community for every alliance and player in State 157. '
        'Please read the rules, introduce yourself, and respect fellow players. '
        'The NAP 10 Council has its own private section.'),
    '📜・server-rules': ('📜 **COMMUNITY RULES**\n'
        '1. Respect everyone. No harassment, hate speech, or threats.\n'
        '2. No spam, scams, impersonation, or malicious links.\n'
        '3. Keep discussions in the correct channels.\n'
        '4. Do not share private information or confidential Council messages.\n'
        '5. Follow Discord rules and moderator instructions.\n'
        '6. Game disputes should be documented and handled respectfully.'),
    '📜・nap10-rules': ('🛡️ **NAP 10 — OFFICIAL RULES**\n'
        'The NAP 10 agreement has been approved by participating leaders. '
        '**The complete ratified rules must be posted here by the Council before members rely on this channel.** '
        'Do not treat summaries or drafts as the final charter.'),
    '⚖️・report-violations': ('⚖️ **REPORTING NAP VIOLATIONS**\n'
        'Do not post sensitive evidence or personal details publicly. '
        'Contact an authorized Council representative or moderator privately. '
        'Include in-game names, alliance tags, time, and screenshots when available.'),
    '🌍・select-language': ('🌍 **LANGUAGE SUPPORT**\n'
        'English is the server language. Multilingual translation support is planned, '
        'but is not active until a translation bot is installed and tested.'),
    '✅・verification': ('✅ **VERIFICATION**\n'
        'Please contact a moderator with your in-game name and alliance tag. '
        'Leadership and Council roles are assigned manually after confirmation.'),
}

class SetupClient(discord.Client):
    async def on_ready(self):
        try:
            guild = self.get_guild(int(GUILD_ID))
            if guild is None:
                print('Bot is not in that server, or the server ID is incorrect.')
                return
            me = guild.me
            if not me.guild_permissions.manage_channels or not me.guild_permissions.manage_roles:
                print('Bot needs Manage Channels and Manage Roles permissions.')
                return
            print(f'Setting up: {guild.name} ({guild.id})')
            roles = {}
            for name, color in ROLE_SPECS:
                role = discord.utils.get(guild.roles, name=name)
                if role is None:
                    role = await guild.create_role(name=name, colour=discord.Colour(color),
                                                   reason='State 157 initial setup')
                    print('Created role:', name)
                roles[name] = role
            everyone = guild.default_role
            staff = [roles['Administrator'], roles['State Moderator']]
            council = roles['NAP 10 Council']
            for category_name, channels, access in SECTIONS:
                category = discord.utils.get(guild.categories, name=category_name)
                if category is None:
                    overwrites = {}
                    if access != 'public':
                        overwrites[everyone] = discord.PermissionOverwrite(view_channel=False)
                        for role in staff + ([council] if access == 'council' else []):
                            overwrites[role] = discord.PermissionOverwrite(view_channel=True,
                                                                           send_messages=True,
                                                                           read_message_history=True)
                    category = await guild.create_category(category_name,
                        overwrites=overwrites, reason='State 157 initial setup')
                    print('Created category:', category_name)
                for name, topic in channels:
                    channel = discord.utils.get(category.text_channels, name=name)
                    if channel is None:
                        # Explicit channel permissions so restricted rooms stay private.
                        overrides = {}
                        if access != 'public':
                            overrides[everyone] = discord.PermissionOverwrite(view_channel=False)
                            for role in staff + ([council] if access == 'council' else []):
                                overrides[role] = discord.PermissionOverwrite(view_channel=True,
                                    send_messages=True, read_message_history=True)
                        channel = await guild.create_text_channel(name, category=category,
                            topic=topic, overwrites=overrides,
                            reason='State 157 initial setup')
                        print('Created channel:', name)
                        if name in POSTS:
                            await channel.send(POSTS[name])
                    else:
                        print('Exists, unchanged:', name)
            print('\nSETUP COMPLETE. Review all role/channel permissions before inviting members.')
            print('Translation, tickets, and automatic verification are NOT installed.')
        except discord.Forbidden:
            print('Missing Discord permissions. Check bot role position and permissions.')
        except discord.HTTPException as exc:
            print('Discord API error:', exc)
        finally:
            await self.close()

async def main():
    intents = discord.Intents.default()
    client = SetupClient(intents=intents)
    await client.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
