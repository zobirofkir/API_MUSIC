from base import Base
from models import *
##################################----Category----###################################
class music_Category(Base):
    pop :str
    rock :str
    hip_Hop_Rap :str
    electronic_Dance :str
    jazz :str
    blues :str
    country :str
    classical :str
    r_B_Soul :str
    reggae :str
    metal :str
    folk :str
    gospel :str
    latin :str
    world_International :str
    new_Age_Ambient :str
    funk :str
    punk :str
    experimental_Avant_garde :str

class pop(Base):
    
    Pop_Rock :str
    Dance_Pop :str
    Synthpop:str
    Contemporary:str
    Electropop:str

    
class rock(Base):
    
    Classic_Rock :str
    Alternative_Rock:str
    Indie_Rock:str
    Hard_Rock:str
    Punk_Rock:str


    
class hip_Hop_Rap(Base):
    
    Trap= Column(Integer, primary_key=True)
    Gangsta_Rap= Column(Integer, primary_key=True)
    Old_School_Hip_Hop= Column(Integer, primary_key=True)
    Conscious_Hip_Hop= Column(Integer, primary_key=True)
    RB_Hip_Hop= Column(Integer, primary_key=True)

class electronic_Dance(Base):
    
    House :str
    Techno:str
    Trance:str
    Dubstep:str
    Drum_and_Bass:str

class jazz(Base): 
    
    Traditional_Jazz :str
    Swing:str
    Bebop:str
    Cool_Jazz:str
    Fusion:str

class blues(Base):
    
    Delta_Blues :str
    Chicago_Blues =Column(String, nullable=False)
    Electric_Blues=Column(String, nullable=False)
    Modern_Blues=Column(String, nullable=False)

class country(Base):
    
    Traditional_Country  :str
    Country_Pop:str
    Bluegrass:str
    Country_Rock:str
    Outlaw_Country:str

class classical(Base):
    
    Symphony :str
    Concerto:str
    Opera:str
    Chamber_Music:str
    Choral:str


class rb_Soul(Base):
    
    Soul :str
    Funk:str
    Neo_Soul:str
    Motown:str
    Contemporary_RB:str


class reggae(Base):
    
    Roots_Reggae :str
    Dancehall:str
    Dub:str
    Ska:str



class metal(Base):
    
    Heavy_Metal :str
    Thrash_Metal:str
    Death_Metal:str
    Black_Metal:str
    Power_Metal:str



class folk(Base):
    
    Traditional_Folk :str
    Contemporary_Folk:str
    World_Folk:str

class gospel(Base):
    
    Traditional_Gospel :str
    Contemporary_Gospel :str


class latin(Base):
    
    Salsa :str
    Bachata:str
    Reggaeton:str
    Cumbia:str
    Merengue:str

class blues(Base):
    
    Gospel :str
    Swing:str

class world_International(Base):
    
    African :str
    Indian:str
    Middle_Eastern:str
    Celtic:str


class new_Age_Ambient(Base):
    
    Meditation :str
    Relaxation=Column(String, nullable=False)
    Space_Music=Column(String, nullable=False)

class funk(Base):
    
    Acid_Jazz = Column(Integer, primary_key=True)
    Funk_Rock :str

class punk(Base):
    
    Pop_Punk :str
    Hardcore_Punk:str


class experimental_Avant_garde(Base):
    
    Noise :str
    Abstract :str

##################################----Publisher----###################################
class Publisher(Base):
    name :str
    location :str


class MusicInformation(Base):
    title :str
    artist = Column(String)
    genre = Column(String)
    release_year = Column(Integer)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

##################################----Fin----###################################
