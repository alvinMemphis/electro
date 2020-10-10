from app import db






class Posts(db.Model):
    __tablename__ = 'posts'
    name =db.Column(db.String(20))
    id = db.Column(db.Integer,primary_key=True)
    candidates = db.relationship('Candidates',backref = 'posts',lazy= 'dynamic')
class Party(db.Model):

    __tablename__ = 'party'
    name = db.Column(db.String(20),unique = True)
    
    id = db.Column(db.Integer,primary_key=True)
    candidates = db.relationship('Candidates', backref = 'party',lazy= 'dynamic')



class District(db.Model):

    
    __tablename__ = 'district'
    name = db.Column(db.String(20),unique = True)
    
    id = db.Column(db.Integer,primary_key=True)

    counties = db.relationship('County',backref = 'district',lazy= 'dynamic')

class Candidates(db.Model):
    
    __tablename__ = 'candidate'
    name = db.Column(db.String(20))
    id = db.Column(db.Integer,primary_key=True)
    party_id = db.Column(db.String(20),db.ForeignKey('party.id'))
    post_id = db.Column(db.String(20),db.ForeignKey('posts.id'))
class SubCounty(db.Model):

     __tablename__ = 'subcounty'
     name = db.Column(db.String(20),unique = True)
     id = db.Column(db.Integer,primary_key=True)

     parishes = db.relationship('Parish',backref= 'subcounty',lazy= 'dynamic')
     county_id = db.Column(db.Integer,db.ForeignKey('county.id'))
class County(db.Model):
     __tablename__ = 'county'
     name = db.Column(db.String(20),unique = True)
     id = db.Column(db.Integer,primary_key = True)
     subcounties = db.relationship('SubCounty',backref='county',lazy= 'dynamic')
     district_id = db.Column(db.String(20),db.ForeignKey('district.id'))
    

class Village(db.Model):
      
    __tablename__ = 'village'
    name = db.Column(db.String(20),unique = True)
    id = db.Column(db.Integer,primary_key = True)
    parish_id = db.Column(db.String(20),db.ForeignKey('parish.id'))
    


class Parish(db.Model):

    __tablename__ = 'parish'
    name = db.Column(db.String(20),unique = True)
    id = db.Column(db.Integer,primary_key = True)
    villages = db.relationship('Village',backref = 'parish',lazy= 'dynamic')
    subcounty_id = db.Column(db.Integer,db.ForeignKey('subcounty.id'))

