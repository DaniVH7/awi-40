import web
from datetime import datetime
from http import cookies

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

class Index:
    def GET(self):
        # Obtener cookie existente o crear una nueva
        cookie = web.cookies().get('visit')
        if not cookie:
            cookie = cookies.SimpleCookie()
            cookie["visit"] = "1"
            cookie["username"] = "dani"
            cookie["date"] = datetime.now().strftime("%d-%b-%Y")
            cookie["time"] = datetime.now().strftime("%H:%M:%S")
        else:
            # Actualizar el número de visitas
            cookie["visit"] = str(int(cookie["visit"].value) + 1)
            cookie["date"] = datetime.now().strftime("%d-%b-%Y")
            cookie["time"] = datetime.now().strftime("%H:%M:%S")
        
        # Obtener nombre de usuario de la URL (si existe)
        username = web.input().get('username')
        if username:
            cookie["username"] = username
        
        # Establecer la fecha de expiración de la cookie (opcional)
        cookie["visit"]["expires"] = 30
        cookie["username"]["expires"] = 30
        cookie["date"]["expires"] = 30
        cookie["time"]["expires"] = 30
        
        # Enviar la cookie al navegador
        web.setcookie("visit", cookie["visit"].value, expires=30)
        web.setcookie("username", cookie["username"].value, expires=30)
        web.setcookie("date", cookie["date"].value, expires=30)
        web.setcookie("time", cookie["time"].value, expires=30)
        
        # Mostrar información almacenada en la cookie
        return "No. de visitas: " + cookie["visit"].value + "<br>" + \
               "Nombre de usuario: " + cookie["username"].value + "<br>" + \
               "Fecha de la visita: " + cookie["date"].value + "<br>" + \
               "Hora de la visita: " + cookie["time"].value

if __name__ == "__main__":
    app.run()

