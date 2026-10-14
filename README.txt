9DL LEGENDS V4 — Registration, Ranks & Live Events

DEPLOY ON CLOUDFLARE PAGES (BACKEND REQUIRED)
1. Extract this ZIP and upload the source folder to a GitHub repository.
2. In Cloudflare Dashboard > Workers & Pages > Create Pages project > Connect to Git, choose the repository. Framework preset: None. Build command: blank. Output directory: / (repository root).
3. Create a Workers KV namespace.
4. Pages project > Settings > Bindings > Add KV namespace binding: Variable name CONTENT; select your KV namespace.
5. Pages project > Settings > Variables and Secrets > Add encrypted secret ADMIN_PASSWORD with a long unique password. Never place the password in source code.
6. Redeploy after binding and secret changes.
7. Visit the website. Members submit applications under JOIN 9DL. R5 logs in at COMMAND PANEL using ADMIN_PASSWORD.
8. The admin can search applications, approve/reject, set website ranks R1-R5, add members by nickname, and view a recent audit log. Member applications and audit logs are private behind the admin password.
9. To update the event calendar, add a confirmed event with a UTC date/time; save. Vault 2's time can remain blank until decided.

LIMITATIONS AND SECURITY
- Ranks assigned here are WEBSITE RECORDS ONLY. Police Chief in-game ranks cannot be changed by this site.
- No in-game account verification: anyone can submit a nickname. Verify players in Police Chief before approval.
- No member accounts/passwords; registration is an application form, not authentication.
- The public registration endpoint has a basic 10-minute per-IP KV throttle and honeypot, not robust bot protection. For a large public site, add Cloudflare Turnstile, WAF rules, and monitoring.
- Cloudflare KV is eventually consistent; concurrent writes to the same member may overwrite each other. Suitable for a small alliance roster, not a financial/security-critical system.
- Admin password is transmitted only over HTTPS to the Pages Function, but is held temporarily in the browser tab while editing. Keep it private and use Cloudflare's HTTPS.
- No automatic sync with Police Chief. Event countdown uses the visitor device clock. No invented Vault 2 schedule.
- A simple ZIP direct upload may not deploy Pages Functions. Use Git integration or Wrangler for server functionality.
- If the backend is not configured, registration and admin are disabled (no fake shared persistence).
- Existing V3 demo localStorage event edits may still appear in the same browser until backend KV is configured.
- The site is independent and not affiliated with the game's developers.

Discord: https://discord.gg/MTtEBF9cD2
