9DL LEGENDS V5 — SISTEMA DE CUENTAS Y PANEL R5

ARCHIVOS
index.html, style.css, app.js: web pública (pantalla de acceso primero).
functions/api/[[path]].js: API segura de Cloudflare Pages Functions.
schema.sql: estructura de base de datos D1.
legacy-v4.html: referencia histórica opcional, NO forma parte de la V5 activa.

PUBLICACIÓN (Cloudflare Pages con GitHub)
1. En GitHub abre melazabaez2000/9dl-legends. Sube los archivos nuevos de la V5 en la RAÍZ, reemplazando index.html y app.js anteriores. Añade style.css, schema.sql y functions/api/[[path]].js. Elimina de la carpeta functions/api los endpoints viejos de V4 (apply.js, members.js, auth.js, audit.js, content.js, _helpers.js), para evitar rutas conflictivas. No publiques passwords ni secretos en GitHub.
2. Cloudflare Pages > tu proyecto 9dl-legends > Settings > Bindings > D1 database: crea/vincula una base D1 con el nombre de variable EXACTO DB.
3. En Cloudflare Dashboard > Storage & databases > D1 > selecciona la base > Console, ejecuta el contenido de schema.sql. También puedes usar Wrangler: npx wrangler d1 execute NOMBRE_DE_TU_BASE --remote --file=./schema.sql
4. Pages > Settings > Variables and Secrets: crea un secreto cifrado BOOTSTRAP_SECRET con una frase larga y única (distinta de la contraseña que usarás para entrar). No lo compartas en chat ni lo publiques.
5. Redeploy desde Cloudflare Pages tras configurar el binding y secreto.
6. Abre tu web. Si aún no existe un R5, aparece el formulario de configuración inicial. Introduce apodo Melaza, contraseña segura y BOOTSTRAP_SECRET. Se crea la única cuenta R5 inicial.
7. El resto de jugadores usa Registrarse. Quedan pendientes hasta que Melaza entre a Miembros > Manage > Approved.
8. Para delegar: aprueba a un jugador, asígnale R4 y, en la misma ficha, activa los permisos que quieras (miembros, rangos, permisos, tareas, eventos, anuncios, auditoría). El R5 tiene acceso total.
9. Los miembros editan su biografía y foto mediante URL HTTPS en Mi perfil. El cambio de contraseña cierra sus sesiones.
10. Las tarjetas de liderazgo se crean automáticamente a partir de los R4 y R5 aprobados. No se precrean cuentas ni contraseñas para Horuk, Satanas, OkenosTR, PIKACHU, Karakan, Suderlidi o WelitinhORJ. Cada uno debe registrarse o ser invitado; Melaza los aprueba y les asigna R4.
11. El calendario no inventa eventos futuros. Añade eventos con fecha UTC desde Calendario. Bóveda 2 queda pendiente de votación.

SEGURIDAD Y LIMITACIONES IMPORTANTES
- Passwords: PBKDF2-SHA256 con 210,000 iteraciones y salt aleatorio. No se guardan contraseñas en texto plano.
- Sesiones: token aleatorio en cookie HttpOnly, Secure, SameSite=Lax; 7 días. Las operaciones administrativas se validan en el servidor.
- Los rangos de la web NO modifican los rangos dentro de Police Chief.
- No existe verificación automática de identidad en el juego. Verifica los apodos antes de aprobar.
- Fotos de perfil mediante URL HTTPS; no incluye subida de archivos ni R2.
- Antes de abrir registro al público, se recomienda añadir Cloudflare Turnstile, protección anti-fuerza bruta/rate limiting, recuperación de cuentas, backups D1 y revisar CSP/seguridad de contenido. Esta versión es una base funcional, no una plataforma auditada para producción masiva.
- BOOTSTRAP_SECRET debe mantenerse privado y, tras crear Melaza, puede quitarse del proyecto; el endpoint rechaza otra cuenta R5 cuando ya existe una.
- Si el proyecto está creado como Worker (no Pages), las Pages Functions no se ejecutarán con esta estructura; se necesita un proyecto Pages.
- Es una web de fans independiente; no es una página oficial del juego.

ENLACE DISCORD: https://discord.gg/MTtEBF9cD2
