from flask import Flask
from routes.home import bp as home_bp  # 'home' Blueprint 임포트
from routes.parking_lot import bp as parking_lot_bp  # 'parking_lot' Blueprint 임포트
from routes.entry_exit import bp as entry_exit_bp  # 'entry_exit' Blueprint 임포트
from routes.spot_status import bp as spot_status_bp  # 'spot_status' Blueprint 임포트

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(home_bp)
app.register_blueprint(parking_lot_bp)
app.register_blueprint(entry_exit_bp)
app.register_blueprint(spot_status_bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
