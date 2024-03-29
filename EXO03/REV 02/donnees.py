    from .app import app, db

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_name = db.Column(db.String(45))
        user_firstname = db.Column(db.String(45))
        user_surname = db.Column(db.String(45))
        user_surname = db.Column(db.Text)
        user_password_hash = db.Column(db.Text)
        user_birthyear = db.Column(db.DateTime)
        user_promotion_date = db.Column(db.String(45))
        user_description = db.Column(db.Text)
        user_last_seen = db.Column(db.DateTime)
        user_linkedin = db.Column(db.Text)
        user_github = db.Column(db.Text)
        user_inscription_time = db.Column(db.DateTime)

        cvs = db.relationship('CV', backref='user', lazy=True)
        sent_messages = db.relationship('Message', backref='sender', lazy=True, foreign_keys='Message.expediteur_id')
        received_messages = db.relationship('Message', backref='recipient', lazy=True, foreign_keys='Message.destinataire_id')
        followers = db.relationship('followers', foreign_keys='followers.followed_id', backref=db.backref('followed', lazy='joined'), lazy='dynamic',cascade='all, delete-orphan')
        followed = db.relationship('followers', foreign_keys='followers.follower_id', backref=db.backref('follower', lazy='joined'), lazy='dynamic',cascade='all, delete-orphan')
        skills = db.relationship('skills', backref='user', lazy=True)

    class skills(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        competence_id = db.Column(db.Integer, db.ForeignKey('competences.id'), nullable=False)

    class competences(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        competence_label = db.Column(db.String(45))
        skills = db.relationship('skills', backref='competences', lazy=True)

    class Post(db.Model):
        post_id = db.Column(db.Integer, primary_key=True)
        post_titre = db.Column(db.String(45))
        post_message = db.Column(db.Text)
        post_date = db.Column(db.DateTime)
        post_indexation = db.Column(db.String(45))
        html = db.Column(db.Text)
        post_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))

    class Followers(db.Model):
        follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
        followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    class CV(db.Model):
        cv_id = db.Column(db.Integer, primary_key=True)
        cv_nom = db.Column(db.Text)
        cv_nom_employeur = db.Column(db.Text)
        cv_ville = db.Column(db.String(45))
        cv_annee_debut = db.Column(db.Integer)
        cv_annee_fin = db.Column(db.Integer)
        cv_description_poste = db.Column(db.Text)

        cv_utilisateur = db.Column(db.Integer, db.ForeignKey('user.id'))

    class Comment(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        comment_message = db.Column(db.Text)
        comment_html = db.Column(db.Text)
        comment_date = db.Column(db.DateTime)
        comment_post = db.Column(db.Integer)
        comment_auteur = db.Column(db.Integer)

    class Message(db.Model):
        message_id = db.Column(db.Integer, primary_key=True)
        message_message = db.Column(db.Text)
        message_html = db.Column(db.Text)
        message_date = db.Column(db.DateTime)
        expediteur_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        destinataire_id = db.Column(db.Integer, db.ForeignKey('user.id'))
