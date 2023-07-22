from base import Base, engine
from sqlalchemy import Column, String, Integer, ForeignKey


##################################----Category----###################################
class Music_Category(Base):
    __tablename__ = 'music_category'
    __table_args__ = {'extend_existing': True}  # Add this line
    id = Column(Integer, primary_key=True)
    pop = Column(String, nullable=False)
    rock = Column(String, nullable=False)
    hip_Hop_Rap = Column(String, nullable=False)
    electronic_Dance = Column(String, nullable=False)
    jazz = Column(String, nullable=False)
    blues = Column(String, nullable=False)
    country = Column(String, nullable=False)
    classical = Column(String, nullable=False)
    r_B_Soul = Column(String, nullable=False)
    reggae = Column(String, nullable=False)
    metal = Column(String, nullable=False)
    folk = Column(String, nullable=False)
    gospel = Column(String, nullable=False)
    latin = Column(String, nullable=False)
    world_International = Column(String, nullable=False)
    new_Age_Ambient = Column(String, nullable=False)
    funk = Column(String, nullable=False)
    punk = Column(String, nullable=False)
    experimental_Avant_garde = Column(String, nullable=False)

class Pop(Base):
    __tablename__='p_op'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Pop_Rock = Column(String, nullable=False)
    Dance_Pop = Column(String, nullable=False)
    Synthpop= Column(String, nullable=False)
    Contemporary= Column(String, nullable=False)
    Electropop= Column(String, nullable=False)

    
class Rock(Base):
    __tablename__='rock'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Classic_Rock = Column(String, nullable=False)
    Alternative_Rock= Column(String, nullable=False)
    Indie_Rock= Column(String, nullable=False)
    Hard_Rock= Column(String, nullable=False)
    Punk_Rock= Column(String, nullable=False)


    
class Hip_Hop_Rap(Base):
    __tablename__='Hip_Hop_rap'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Trap= Column(Integer, primary_key=True)
    Gangsta_Rap= Column(Integer, primary_key=True)
    Old_School_Hip_Hop= Column(Integer, primary_key=True)
    Conscious_Hip_Hop= Column(Integer, primary_key=True)
    RB_Hip_Hop= Column(Integer, primary_key=True)

class Electronic_Dance(Base):
    __tablename__='Electronic_dance'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    House = Column(String, nullable=False)
    Techno= Column(String, nullable=False)
    Trance= Column(String, nullable=False)
    Dubstep= Column(String, nullable=False)
    Drum_and_Bass= Column(String, nullable=False)

class Jazz(Base): 
    __tablename__='jazz'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Traditional_Jazz = Column(String, nullable=False)
    Swing= Column(String, nullable=False)
    Bebop= Column(String, nullable=False)
    Cool_Jazz= Column(String, nullable=False)
    Fusion= Column(String, nullable=False)

class Blues(Base):
    __tablename__='blues'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Delta_Blues = Column(String, nullable=False)
    Chicago_Blues =Column(String, nullable=False)
    Electric_Blues=Column(String, nullable=False)
    Modern_Blues=Column(String, nullable=False)

class Country(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__='country'
    id = Column(String, primary_key=True)
    Traditional_Country  = Column(String, nullable=False)
    Country_Pop= Column(String, nullable=False)
    Bluegrass= Column(String, nullable=False)
    Country_Rock= Column(String, nullable=False)
    Outlaw_Country= Column(String, nullable=False)

class Classical(Base):
    __tablename__='classical'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Symphony = Column(String, nullable=False)
    Concerto= Column(String, nullable=False)
    Opera= Column(String, nullable=False)
    Chamber_Music= Column(String, nullable=False)
    Choral= Column(String, nullable=False)


class RB_Soul(Base):
    __tablename__='RB_soul'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Soul = Column(String, nullable=False)
    Funk= Column(String, nullable=False)
    Neo_Soul= Column(String, nullable=False)
    Motown= Column(String, nullable=False)
    Contemporary_RB= Column(String, nullable=False)


class Reggae(Base):
    __tablename__='reggae'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Roots_Reggae = Column(String, nullable=False)
    Dancehall= Column(String, nullable=False)
    Dub= Column(String, nullable=False)
    Ska= Column(String, nullable=False)



class Metal(Base):
    __tablename__='metal'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Heavy_Metal = Column(String, nullable=False)
    Thrash_Metal= Column(String, nullable=False)
    Death_Metal= Column(String, nullable=False)
    Black_Metal= Column(String, nullable=False)
    Power_Metal= Column(String, nullable=False)



class Folk(Base):
    __tablename__='folk'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Traditional_Folk = Column(String, nullable=False)
    Contemporary_Folk= Column(String, nullable=False)
    World_Folk= Column(String, nullable=False)

class Gospel(Base):
    __tablename__='gospel'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Traditional_Gospel = Column(String, nullable=False)
    Contemporary_Gospel = Column(String, nullable=False)


class Latin(Base):
    __tablename__='latin'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Salsa = Column(String, nullable=False)
    Bachata= Column(String, nullable=False)
    Reggaeton= Column(String, nullable=False)
    Cumbia= Column(String, nullable=False)
    Merengue= Column(String, nullable=False)

class BBlues(Base):
    __tablename__='BBlues'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Gospel = Column(String, nullable=False)
    Swing= Column(String, nullable=False)

class World_International(Base):
    __tablename__='World_international'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    African = Column(String, nullable=False)
    Indian= Column(String, nullable=False)
    Middle_Eastern= Column(String, nullable=False)
    Celtic= Column(String, nullable=False)


class New_Age_Ambient(Base):
    __tablename__='New_Age_ambient'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Meditation = Column(String, nullable=False)
    Relaxation=Column(String, nullable=False)
    Space_Music=Column(String, nullable=False)

class Funk(Base):
    __tablename__='funk'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Acid_Jazz = Column(Integer, primary_key=True)
    Funk_Rock = Column(String, nullable=False)

class Punk(Base):
    __tablename__='punk'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Pop_Punk = Column(String, nullable=False)
    Hardcore_Punk= Column(String, nullable=False)


class Experimental_Avant_garde(Base):
    __tablename__='Experimental_Avant_garde'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    Noise = Column(String, nullable=False)
    Abstract = Column(String, nullable=False)

##################################----Publisher----###################################
class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)


class MusicInformation(Base):
    __tablename__ = 'music_information'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String)
    genre = Column(String)
    release_year = Column(Integer)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

##################################----Fin----###################################


Base.metadata.create_all(bind=engine)