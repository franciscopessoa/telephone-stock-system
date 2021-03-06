import datetime
from app import db, ma

class PhoneNumbers(db.Model):
    __tablename__ = "phone_numbers"

    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value        = db.Column(db.String(25), unique=True, nullable=False)
    monthy_price = db.Column(db.Numeric(15,2), nullable=False)
    setup_price  = db.Column(db.Numeric(15,2), nullable=False)
    currency     = db.Column(db.String(3), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, value, monthy_price, setup_price, currency):
        self.value        = value
        self.monthy_price = monthy_price
        self.setup_price  = setup_price
        self.currency     = currency
        
class PhoneNumbersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'value', 'monthy_price', 'setup_price', 'currency')