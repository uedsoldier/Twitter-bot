# **Twitter-bot**

Ejercicio de programación en Python cuya finalidad (además de aprender y practicar) es publicar en Twitter/X **críticas ácidas, irracionales y 100% necesarias** a la gestión de **Santiago Baños** en el Club América 💛💙

## 🧠 **¿Por qué?**

Porque programar también es una forma de protesta. Este bot representa una mezcla de frustración, código limpio (a veces), y libertad de expresión vía API.  
Además, ¿quién no quiere automatizar su odio deportivo?

## 🔧 **¿Cómo funciona?**

Cada cierto tiempo —específicamente cuatro veces al día—, el bot se despierta, escoge una frase prearmada (o genera una nueva si se le acaban), y publica un tuit bien dirigido a la cabeza del América.  
Y si nadie lo detiene, lo seguirá haciendo... **para siempre**.

- Las frases se gestionan desde Redis
- El historial de publicaciones evita repeticiones (porque la creatividad también es digna)
- Corre dentro de un contenedor Docker, con `cron` como despertador fiel
- Todos los errores se imprimen (con odio) en logs

## 🗃️ **Variables de entorno**

Los datos necesarios tanto para la API de Twitter como para Redis se colocan en un archivo `.env`, que se copia automáticamente al contenedor Docker. Ejemplo:

CONSUMER_KEY=abdef
REDIS_HOST=ghijk
REDIS_PORT=6379
REDIS_PASSWORD=contraseñaultrasecreta

Sí, el `.env` es privado. **No se lo muestres a Baños.**

## 🐳 **Docker**

Todo el proyecto se ejecuta dentro de un contenedor Debian slim con Python 3.13, Redis externo y tareas programadas con `cron`.

## ⏰ **Tareas programadas**

Cada 20 minutos se publica un tweet.

Cada 30 minutos: el bot efectúa un healthcheck confirmar que sigue vivo.

Si el bot no publica por error o si Redis se cae, todo queda registrado.

## 📋 **Frases**
Las frases están en Redis y se rotan constantemente. Algunas son simples. Otras, groseras. Todas absolutamente necesarias.

## **🛠️ En desarrollo**
Francamente creo que cumple y hasta ahí se quedará el veneno. 🐍. Falta un poco de documentación que poco a poco irá apareciendo.

📚 **Tutorial básico**
Si quieres entender cómo montar esto desde cero (o estás aprendiendo), puedes ver este [tutorial básico en YouTube](https://www.youtube.com/watch?v=xsSXL5iuzDg)

## 🤖 **Créditos**

Este proyecto fue realizado en **un solo día** con la asistencia de inteligencia artificial (ChatGPT), lo cual permitió acelerar la escritura del código, automatización y documentación.

Sí, lo odio tanto como para automatizarlo en tiempo récord.

## 🐦 Autor

Sígueme (o mientame la madre) en [Twitter/X](https://x.com/uedsoldier)

## ⚠️ Disclaimer

Este proyecto es de naturaleza satírica y tiene fines educativos, de aprendizaje y humorísticos.  
No busca incitar al odio, acoso o violencia contra ninguna persona o institución.

Todo el contenido generado y publicado por el bot representa una forma de crítica subjetiva y libre expresión sobre temas deportivos.  
**Este repositorio no está afiliado, respaldado ni aprobado por el Club América, Twitter/X ni ninguna figura pública mencionada.**

Si alguien se siente ofendido por el contenido, se recomienda respirar profundo, reírse un poco y seguir con su día.

## ☠️ **Mensaje final**

CHTPM, Santiago Baños.
(Frase institucional del proyecto. No discutimos esta parte.)
