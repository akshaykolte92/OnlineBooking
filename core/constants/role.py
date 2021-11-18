class Role:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    GUEST = {
        "name": "GUEST",
        "description": "A Guest Account",
    }

    CUSTOMER = {
        "name": "CUSTOMER",
        "description": "A CUSTOMER Account",
    }

    HOTEL_ADMIN = {
        "name": "HOTEL_ADMIN",
        "description": "Primary Administrator/Superuser For an HOTEL",
    }

    HOTEL_MANAGER = {
        "name": "HOTEL_MANAGER",
        "description": "Day to Day Administrator of Events For an HOTEL",
    }

    SUPER_ADMIN = {
        "name": "SUPER_ADMIN",
        "description": "Super Administrator of Application Ecosystem",
    }
