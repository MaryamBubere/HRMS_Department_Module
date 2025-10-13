from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Department
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def dashboard():
        total = Department.query.count()
        active = Department.query.filter_by(is_active=True).count()
        return render_template('dashboard.html', total=total, active=active)

    @app.route('/departments')
    def departments_list():
        q = request.args.get('q', '')
        if q:
            depts = Department.query.filter(Department.name.ilike(f'%{q}%')).all()
        else:
            depts = Department.query.order_by(Department.id).all()
        return render_template('departments_list.html', depts=depts, q=q)

    @app.route('/departments/add', methods=['GET','POST'])
    def add_department():
        if request.method == 'POST':
            name = request.form['name'].strip()
            description = request.form.get('description','')
            if not name:
                flash('Department name is required', 'danger')
                return redirect(url_for('add_department'))
            existing = Department.query.filter_by(name=name).first()
            if existing:
                flash('Department already exists', 'danger')
                return redirect(url_for('add_department'))
            dept = Department(name=name, description=description)
            db.session.add(dept)
            db.session.commit()
            flash('Department added successfully', 'success')
            return redirect(url_for('departments_list'))
        return render_template('department_form.html', action='Add', dept=None)

    @app.route('/departments/edit/<int:dept_id>', methods=['GET','POST'])
    def edit_department(dept_id):
        dept = Department.query.get_or_404(dept_id)
        if request.method == 'POST':
            name = request.form['name'].strip()
            description = request.form.get('description','')
            if not name:
                flash('Department name is required', 'danger')
                return redirect(url_for('edit_department', dept_id=dept_id))
            other = Department.query.filter(Department.name==name, Department.id!=dept.id).first()
            if other:
                flash('Another department with same name exists', 'danger')
                return redirect(url_for('edit_department', dept_id=dept_id))
            dept.name = name
            dept.description = description
            db.session.commit()
            flash('Department updated successfully', 'success')
            return redirect(url_for('departments_list'))
        return render_template('department_form.html', action='Edit', dept=dept)

    @app.route('/departments/delete/<int:dept_id>', methods=['POST'])
    def delete_department(dept_id):
        dept = Department.query.get_or_404(dept_id)
        dept.is_active = False
        db.session.commit()
        flash('Department marked inactive (soft deleted).', 'warning')
        return redirect(url_for('departments_list'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
