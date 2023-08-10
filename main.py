from app.app import CreateApp, web
from routes.routs import routes

app = CreateApp().app_instance
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
