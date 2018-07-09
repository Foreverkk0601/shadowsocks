from flask import Flask,Blueprint
import json

def create_app(traffic_stats):


    traffic_manager = Blueprint("traffic", __name__)


    @traffic_manager.route("/show", methods=['GET'])
    def show():
        return traffic_stats.get_all_count()

    @traffic_manager.route("/show/<ip>", methods=['GET'])
    def show_ip(ip):
        return traffic_stats.get_special_count(ip)

    app = Flask(__name__)

    app.register_blueprint(traffic_manager)

    return app
