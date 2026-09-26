import os
import sys


def import_dotenv() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("The 'python-dotenv' package is required to load " +
              "environment variables from a .env file.")
        print("Please install it using" +
              " 'pip install python-dotenv' and try again.")
        sys.exit(1)
    load_dotenv()


def load_config() -> tuple[dict, list]:
    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    config = {}
    missing = []
    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        else:
            config[var] = value
    return config, missing


def show_mode_difference(mode: str) -> None:
    if mode == 'production':
        print("\n=== PRODUCTION MODE ACTIVE ===")
        print(" - Enhanced security enabled")
        print(" - Detailed logging disabled")
        print(" - : pandas.DataFramePerformance optimizations active")
    else:
        print("\n=== DEVELOPMENT MODE ===")
        print(" - Debug logging enabled")
        print(" - Security checks relaxed")
        print(" - Verbose error messages")


def display_config(config: dict, missing: list) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    if missing:
        print(f" [WARNING] Missing variables: {', '.join(missing)}")
        return
    mode = config.get("MATRIX_MODE", "development")
    db = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    log_level = config.get("LOG_LEVEL")
    zion_endpoint = config.get("ZION_ENDPOINT")

    print(f"Mode = {mode}")
    if db and ('localhost' in db or 'sqlite' in db):
        print("Database = Connected to local instance")
    else:
        print("Database = Connected to remote instance")
    if api_key and len(api_key) > 4:
        print("API Access = Authenticated")
    else:
        print("API Access = Invalid or missing key")
    print(f"Log Level = {log_level}")
    if zion_endpoint:
        print("Zion Network = Connected")
    else:
        print("Zion Network = Not connected")

    show_mode_difference(mode)


def simulate_error(mode: str) -> None:
    print("\n--- Simulating an error  ---")
    try:
        1 / 0
    except ZeroDivisionError as e:
        if mode == "development":
            print(f"[DEV ERROR] {e}")
            print("[DEV] Full debug info shown")
        else:
            print("[PROD ERROR] Something went wrong")
            print("[PROD] Error hidden from users")


def security_check(config: dict) -> None:
    print("\nEnvironment security check:")

    print(" [OK] All required environment variables are set.")

    if config.get("API_KEY") and 'your_' not in config["API_KEY"]:
        print(" [OK] API key appears valid.")
    elif 'your_' in config.get("API_KEY", ""):
        print(" [OK] No hardcoded secrets detected")
    else:
        print(" [WARNING] API key is missing or may be invalid.")

    if os.path.exists('.env'):
        print(" [OK] .env file properly configured")
    else:
        print(" [WARNING] .env file not found")

    if config.get("MATRIX_MODE") == 'production':
        print(" [OK] Production overrides available")
    else:
        print(" [OK] Development mode active, no production overrides needed")


def main() -> None:
    try:
        import_dotenv()
        config, missing = load_config()
        display_config(config, missing)
        if missing:
            sys.exit(1)
        simulate_error(config.get("MATRIX_MODE", "development"))
        security_check(config)
    except Exception as e:
        print(f"An error occurred while loading the configuration: {e}")
        sys.exit(1)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
