import os
from dotenv import load_dotenv
from snowflake.snowpark import Session
from cryptography.hazmat.primitives import serialization
import base64

def get_session():
    """
    Securely create and return a Snowpark session using environment variables.
    Reads credentials from .env and your private key file.
    """
    # Load environment variables from .env
    load_dotenv()

    # Read and process private key (same approach as working notebook)
    private_key_path = os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH")
    with open(private_key_path, "rb") as key_file:
        private_key_pem = key_file.read()

    # Load the private key and convert to DER format
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,  # If your key has a passphrase, put it here
    )

    # Serialize to DER and encode to base64
    private_key_der = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    private_key_base64 = base64.b64encode(private_key_der).decode('utf-8')

    # Connection parameters - use the key object directly
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        "private_key": private_key  # Use the cryptography key object
    }

    # Create session
    session = Session.builder.configs(connection_parameters).create()
    print("✅ Connected successfully to Snowflake!")
    return session

# Test connection (run only when executing this file directly)
if __name__ == "__main__":
    session = get_session()
    print(session.sql("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA();").collect())
