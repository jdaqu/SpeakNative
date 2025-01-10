# from sqlalchemy import JSON, Column, Integer, String, Text, ForeignKey, Table, create_engine
# from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# DATABASE_URL = "sqlite:///./app_data.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Base = declarative_base()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Join table for many-to-many relationship between Phrase and Mistake
# phrase_mistakes = Table(
#     "phrase_mistakes",
#     Base.metadata,
#     Column("phrase_id", Integer, ForeignKey("phrases.id"), primary_key=True),
#     Column("mistake_id", Integer, ForeignKey("mistakes.id"), primary_key=True),
# )

# # Topics Table
# class Topic(Base):
#     __tablename__ = "topics"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text, nullable=True)

# # Mistakes Table
# class Mistake(Base):
#     __tablename__ = "mistakes"

#     id = Column(Integer, primary_key=True, index=True)
#     mistake = Column(Text, nullable=False)
#     correct_text = Column(Text, nullable=False)

#     # Back-reference to phrases
#     phrases = relationship("Phrase", secondary=phrase_mistakes, back_populates="mistakes")

# # Phrases Table
# class Phrase(Base):
#     __tablename__ = "phrases"

#     id = Column(Integer, primary_key=True, index=True)
#     original_text = Column(Text, nullable=False)
#     correct_text = Column(Text, nullable=True)
#     topic_to_study = Column(Integer, ForeignKey("topics.id"), nullable=True)

#     # Relationships
#     mistakes = relationship("Mistake", secondary=phrase_mistakes, back_populates="phrases")

# # Vocabulary Table
# class Vocabulary(Base):
#     __tablename__ = "vocabulary"

#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String(100), nullable=False)
#     translation = Column(Text, nullable=True)
#     alternatives = Column(JSON, nullable=True)


# ===================================
# NEW VERSION - NEW ARCHITECTURE
# ===================================

from sqlalchemy import JSON, Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Join table for many-to-many relationship between Phrase and Mistake
# phrase_mistakes = Table(
#     "phrase_mistakes",
#     Base.metadata,
#     Column("phrase_id", Integer, ForeignKey("phrases.id"), primary_key=True),
#     Column("mistake_id", Integer, ForeignKey("mistakes.id"), primary_key=True),
# )

# Topics Table
# class Topic(Base):
#     __tablename__ = "topics"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text, nullable=True)

# Mistakes Table
# class Mistake(Base):
#     __tablename__ = "mistakes"

#     id = Column(Integer, primary_key=True, index=True)
#     mistake = Column(Text, nullable=False)
#     correct_text = Column(Text, nullable=False)

#     # Back-reference to phrases
#     phrases = relationship("Phrase", secondary=phrase_mistakes, back_populates="mistakes")

# TODO: I'm commeting all the models, to start with simply, with only Phrases.
# REMEMBER: I only need to delete de app_data.db and run the script to create again the db

# Phrases Table
class Phrase(Base):
    __tablename__ = "phrases"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    correct_text = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=True)
    # topic_to_study = Column(Integer, ForeignKey("topics.id"), nullable=True)

    # Relationships
    # mistakes = relationship("Mistake", secondary=phrase_mistakes, back_populates="phrases")

# Vocabulary Table
# class Vocabulary(Base):
#     __tablename__ = "vocabulary"

#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String(100), nullable=False)
#     translation = Column(Text, nullable=True)
#     alternatives = Column(JSON, nullable=True)
