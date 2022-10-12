def name ():
    return "Vector"

def author():
    return "José Francisco Chávez Castillo"

def authorNAme():
    return author()

def email():
    return "jfchavezc001@gmail.com"

def description():
    return "vector"

def about():
    return "Vector"

def version():
    return "0.0.1"

def qgisMiniumVersion():
    return "3.0"

def icon():
    return "icon.png"

def category():
    return "vector"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)