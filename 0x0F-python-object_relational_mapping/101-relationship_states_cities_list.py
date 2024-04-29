from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, State

if __name__ == "__main__":
    # Get arguments from command line
    username, password, database_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )

    # Create connection string
    connection_string = f"mysql+pymysql://{username}:{password}@localhost:3306/{database_name}"

    # Create database engine
    engine = create_engine(connection_string)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City objects with state relationship
    cities = (
        session.query(City)
        .join(City.state)
        .order_by(City.id)
        .all()
    )

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} ({city.state.name})")

    # Close session
    session.close()
