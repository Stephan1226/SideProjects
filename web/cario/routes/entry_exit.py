from flask import Blueprint, render_template

bp = Blueprint('entry_exit', __name__)

@bp.route('/entry-exit')
def entry_exit():
    # 입출차 기록을 가져오는 로직을 추가 (예: DB에서 조회)
    return render_template('index.html', title="Entry/Exit")
