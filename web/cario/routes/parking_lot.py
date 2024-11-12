from flask import Blueprint, render_template

bp = Blueprint('parking_lot', __name__)

@bp.route('/parking-lot')
def parking_lot():
    # 주차장 목록을 가져오는 로직을 추가 (예: DB에서 조회)
    return render_template('index.html', title="Parking Lot")
