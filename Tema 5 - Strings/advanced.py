# Actividades avanzados


# Has recibido esta información al submit un formulario. Limpiar los datos.
form_data = "    NAME: john doe; EMAIL: John.Doe@EXAMPLE.com   ; PHONE: (123) 456-7890; COMMENT:    I’m very interested in your product! Could you send me more details?    "


#  Sacar los reviews positivos en un lado y negativos por otro
reviews = [
    "  I absolutely LOVE this product!!! It's amazing and works perfectly.   ",
    "Terrible experience. It broke after just ONE day of use. Never buying again!  ",
    "Good value for the price. Nothing extraordinary, but gets the job done.",
    "Awful. Waste of money!!!   Completely disappointed.   ",
    "Highly recommend it! Great quality and very easy to use."
]

# log data de un servidor web
log_data = """
2024-11-24 10:15:32 [INFO] User: johndoe logged in successfully.
2024-11-24 10:17:45 [WARNING] User: janedoe failed to login.
2024-11-24 10:18:10 [INFO] User: johndoe uploaded file: report.pdf.
2024-11-24 10:20:55 [INFO] User: johndoe logged out.
2024-11-24 10:21:03 [INFO] User: janedoe logged in successfully.
2024-11-24 10:22:15 [ERROR] User: johndoe attempted unauthorized access.
2024-11-24 10:23:05 [INFO] User: janedoe uploaded file: presentation.pptx.
2024-11-24 10:25:33 [INFO] User: janedoe logged out.
2024-11-24 10:26:40 [INFO] User: johndoe logged in successfully.
"""

# extraer los datos en un formato leible para tu manager. Incluir datos númericos para resumir, como 5 INFO, 3 ERROR, 1 WARNING.
# Failed Logins: {'janedoe': 1}
# Unauthorized Access Attempts: [{'timestamp': '2024-11-24 10:22:15', 'status': 'ERROR', 'username': 'johndoe', 'action': 'attempted unauthorized access'}]
# Si ha habido muchos 'failed to login' en menos de un minuto, mostrar un mensaje.
# Usar functions
