from sqlalchemy import Table, Column, Integer, ForeignKey,String
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            )
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'
    name =Column(String(20))
    id = Column(Integer,primary_key=True)
    candidates = relationship('Candidates',backref = 'posts',lazy= 'dynamic')
class Party(Base):

    __tablename__ = 'party'
    name = Column(String(20),unique = True)
    
    id = Column(Integer,primary_key=True)
    candidates = relationship('Candidates', backref = 'party',lazy= 'dynamic')



class District(Base):

    
    __tablename__ = 'district'
    name = Column(String(20),unique = True)
    
    id = Column(Integer,primary_key=True)

    counties = relationship('County',backref = 'district',lazy= 'dynamic')

class Candidates(Base):
    
    __tablename__ = 'candidate'
    name = Column(String(20))
    id = Column(Integer,primary_key=True)
    party_id = Column(String(20),ForeignKey('party.id'))
    post_id = Column(String(20),ForeignKey('posts.id'))
class SubCounty(Base):

     __tablename__ = 'subcounty'
     name = Column(String(20),unique = True)
     id = Column(Integer,primary_key=True)

     parishes = relationship('Parish',backref= 'subcounty',lazy= 'dynamic')
     county_id = Column(Integer,ForeignKey('county.id'))
class County(Base):
     __tablename__ = 'county'
     name = Column(String(20),unique = True)
     id = Column(Integer,primary_key = True)
     subcounties = relationship('SubCounty',backref='county',lazy= 'dynamic')
     district_id = Column(String(20),ForeignKey('district.id'))
    

class Village(Base):
      
    __tablename__ = 'village'
    name = Column(String(20),unique = True)
    id = Column(Integer,primary_key = True)
    parish_id = Column(String(20),ForeignKey('parish.id'))
    


class Parish(Base):

    __tablename__ = 'parish'
    name = Column(String(20),unique = True)
    id = Column(Integer,primary_key = True)
    villages = relationship('Village',backref = 'parish',lazy= 'dynamic')
    subcounty_id = Column(Integer,ForeignKey('subcounty.id'))

