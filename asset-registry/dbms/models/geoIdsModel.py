from dbms import db
from datetime import datetime


class GeoIds(db.Model):
    __tablename__ = 'geo_ids'

    id = db.Column(db.Integer, primary_key=True, index=True)
    geo_id = db.Column(db.String(), unique=True)
    authority_token = db.Column(db.String())
    geo_data = db.Column(db.JSON)
    s2_cell_tokens = db.relationship('S2CellTokens', secondary='cells_geo_ids', backref='geo_ids')
    country = db.Column(db.String(), nullable=True)
    boundary_type = db.Column(db.String(), nullable=True, default='manual')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, geo_id, geo_data, authority_token, country, boundary_type):
        self.geo_id = geo_id
        self.geo_data = geo_data
        self.authority_token = authority_token
        self.country = country
        self.boundary_type = boundary_type

    def __repr__(self):
        return '<id {}>'.format(self.id)
