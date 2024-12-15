from flask import Flask, jsonify, request, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from datetime import datetime

'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab.db'
app.config['SECRET_KEY'] = 'your-secret-key'
# db = SQLAlchemy(app)
# login_manager = LoginManager()
login_manager.init_app(app)

# class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    collaborators = db.relationship('User', secondary='project_collaborators')

project_collaborators = db.Table('project_collaborators',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        login_user(user)
        return jsonify({"message": "Logged in successfully"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/projects', methods=['GET'])
@login_required
def get_projects():
    search = request.args.get('search', '')
    projects = Project.query.filter(Project.title.contains(search)).all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'content': p.content,
        'author': p.author.username,
        'date_created': p.date_created.isoformat()
    } for p in projects])

@app.route('/project/<int:id>/collaborate', methods=['POST'])
@login_required
def add_collaborator(id):
    project = Project.query.get_or_404(id)
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        project.collaborators.append(user)
        db.session.commit()
        return jsonify({"message": "Collaborator added successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

'''