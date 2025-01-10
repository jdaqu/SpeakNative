# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Define the database URL for SQLite
# DATABASE_URL = "sqlite:///./app_data.db"

DATABASE_URL = "sqlite:///./../data/app_data.db"

# # Create the database engine
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # Create the base class for models
# Base = declarative_base()

# # Create the SessionLocal class for database sessions
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ===================================
# NEW VERSION - NEW ARCHITECTURE
# ===================================

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
# DATABASE_URL = "sqlite:///../data/app_data.db"
DATABASE_URL = "sqlite:///app/data/app_data.db"



# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base para los modelos
Base = declarative_base()

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
