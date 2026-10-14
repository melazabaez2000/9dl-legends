# STATE 157 | OFFICIAL COMMUNITY — Setup

Creates English-language roles, categories, channels, permissions and starter posts for the entire State 157. Does not delete existing channels or roles. Re-running reuses existing names. **Review the plan before running.**

## Windows PC
1. Install Python 3.11+ from https://www.python.org/downloads/ (enable **Add Python to PATH**).
2. Open https://discord.com/developers/applications, create a New Application, open **Bot**, create/reset the bot token and copy it. **Never share the token.**
3. In **Installation** (or OAuth2 URL Generator), invite the bot to your server with scopes `bot` and permissions **Manage Channels**, **Manage Roles**, **View Channels**, **Send Messages**, **Read Message History**. The bot's role must be higher than the roles it will manage. You must own/administer the server.
4. In Discord desktop: User Settings > Advanced > Developer Mode ON; right-click your server icon > **Copy Server ID**.
5. Rename `.env.example` to `.env` and fill in `DISCORD_BOT_TOKEN` and `DISCORD_GUILD_ID`. Never send `.env` to anyone.
6. Open a terminal in this folder and run:

   py -m pip install -r requirements.txt
   py setup_server.py

7. Review permissions in **Server Settings > Roles** and test with a non-admin account before inviting members. Remove the bot or revoke its token if no longer needed.

## Notes
- Only the Founder (server owner) and Administrator role can see staff rooms. NAP 10 Council role can see Council rooms; public members cannot.
- Assign `NAP 10 Council`, `Alliance Leader`, and `Alliance Officer` manually after confirming identities. **Do not grant Administrator permission to council members.**
- The installer does not add translator/ticket bots, automated role selection, or live polls. These need separate services/configuration.
- It does not modify or delete existing content. Channels or roles with the same name are reused; manually review permissions on pre-existing items.
- Discord bot tokens are secret. If exposed, regenerate immediately.
