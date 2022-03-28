from flask import Flask, render_template

class RouteEntry:
    def __init__(self, name, localPort, remotePort):
        self.localPort, self.remotePort, self.name = localPort, remotePort, name


app = Flask(__name__)
@app.route('/')
@app.route('/loginForm')
def loginForm(name=None):
    return render_template('loginForm.html', name=name)

@app.route('/dashboard')
def index(name=None):
    routeEntries=[RouteEntry("test", 80, 800), RouteEntry("test", 443, 4433), RouteEntry("test", 17, 177)]
    return render_template('dashboard.html', name=name, routeEntries=routeEntries)

if __name__ == "__main__":
    app.run(port=8080, debug=True)