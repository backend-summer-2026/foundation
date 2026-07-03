

class AuthorizationError(Exception):
    """Exception raised for authorization errors."""
    pass


class AuthenticationError(Exception):
    """Exception raised for authentication errors."""
    pass


class ValidationError(Exception):
    """Exception raised for validation errors."""
    pass


class DatabaseError(Exception):
    """Exception raised for database errors."""
    pass


try:
    # Simulate an authorization error
    pass
except AuthorizationError as e:
    print(f"Authorization error occurred: {e}")
except AuthenticationError as e:
    print(f"Authentication error occurred: {e}")
except ValidationError as e:
    print(f"Validation error occurred: {e}")
except DatabaseError as e:
    print(f"Database error occurred: {e}")
