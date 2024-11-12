from flask import Blueprint, render_template

bp = Blueprint('spot_status', __name__)

@bp.route('/spot-status')
def spot_status():
    # 주차 공간 상태를 가져오는 로직을 추가 (예: DB에서 조회)
    return render_template('index.html', title="Spot Status")
