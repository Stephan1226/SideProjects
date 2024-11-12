from app import db

# 주차장 모델 정의
class ParkingLot(db.Model):
    __tablename__ = 'parking_lots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    occupied_spots = db.Column(db.Integer, default=0)
    status = db.Column(db.Enum('open', 'close'), default='open')

# 차량 모델 정의
class Car(db.Model):
    __tablename__ = 'cars'
    plate_number = db.Column(db.String, primary_key=True)
    owner_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    car_type = db.Column(db.Enum('sedan', 'SUV', 'truck', 'van'))

# 입출차 기록 모델 정의
class EntryExitLog(db.Model):
    __tablename__ = 'entry_exit_logs'
    id = db.Column(db.Integer, primary_key=True)
    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lots.id'))
    plate_number = db.Column(db.String, db.ForeignKey('cars.plate_number'))
    entry_time = db.Column(db.DateTime, nullable=False)
    exit_time = db.Column(db.DateTime)
    status = db.Column(db.Enum('in', 'out'), nullable=False)

# 주차 공간 모델 정의
class ParkingSpot(db.Model):
    __tablename__ = 'parking_spots'
    id = db.Column(db.Integer, primary_key=True)
    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lots.id'))
    spot_number = db.Column(db.String, nullable=False)
    occupied = db.Column(db.Boolean, default=False)
    car_plate = db.Column(db.String, db.ForeignKey('cars.plate_number'))

# 데이터베이스 테이블 생성 (서버 실행 시 자동으로 실행)
db.create_all()
