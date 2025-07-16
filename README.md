# 🟢 Envío Automatizado de Mensajes por WhatsApp Web con Python + Selenium

Este script automatiza el envío de mensajes de WhatsApp a múltiples números utilizando WhatsApp Web, con ayuda de Selenium y el navegador Chrome.

---

## ⚙️ Requisitos

- Python 3.6 o superior
- Google Chrome
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible con tu versión de Chrome
- Librerías de Python:
  - `selenium`

Instalación de dependencias:
```bash
pip install selenium
```

---

## 📁 Estructura

- `script.py`: Script principal para enviar los mensajes.
- `numeros.txt`: Archivo de texto con una lista de números (sin espacios ni guiones). Uno por línea. Ejemplo:

```
2611234567
2647654321
```

---

## 💬 Mensaje

Podés modificar el contenido del mensaje directamente en el script, en esta línea:

```python
mensaje = "Hola, te consulto tenes alojamiento disponible para 4 personas para este jueves 17?..."
```

---

## ▶️ Cómo usar

1. Asegurate de tener `numeros.txt` con los números destino.
2. Ejecutá el script:

```bash
python script.py
```

3. Se abrirá WhatsApp Web. Escaneá el código QR con tu celular.
4. El script enviará el mensaje automáticamente a cada número.

---

## ❗ Advertencias

- El script **recarga WhatsApp Web por cada número**, lo que puede ser lento.
- Usar automatizaciones en WhatsApp puede estar en contra de sus términos de servicio. Úsalo bajo tu responsabilidad.
- Asegurate de no enviar spam. WhatsApp puede suspender tu cuenta si detecta uso abusivo.

---

## 📌 Notas adicionales

- Los números se formatean automáticamente con el prefijo `549` (Argentina).
- No se guarda historial de envíos, ni se controla si el número tiene WhatsApp activo.
- Si un número no es válido o no tiene cuenta de WhatsApp, el script lo informa en consola.

---

## 🧠 Autor

Desarrollado con fines educativos por [tu nombre o alias acá].
