from core.DB.database import  Base,engine

print("Creating Database .....")

Base.metadata.create_all(engine)