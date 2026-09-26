import importlib


def try_import(module_name) -> object:
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError:
        return None


def import_dependencies() -> dict:
    deps = {
        'pandas': try_import('pandas'),
        'numpy': try_import('numpy'),
        'matplotlib': try_import('matplotlib'),
        'matplotlib.pyplot': try_import('matplotlib.pyplot'),
        'requests': try_import('requests')
    }
    return deps


def check_depedencies(modules: dict) -> dict:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    versions = {}
    descriptions = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready',
        'requests': 'Network access ready'
    }

    for dep in ['pandas', 'numpy', 'matplotlib', 'requests']:
        module = modules.get(dep)
        if module:
            version = getattr(module, '__version__', 'Unknown version')
            versions[dep] = version
            print(f"[OK] {dep} ({version}) - {descriptions[dep]}")
        else:
            print(f"[MISSING] {dep}")
            versions[dep] = None
    return versions


def show_installation_instructions(missing_deps: list) -> None:
    print("\n" + "="*60)
    print("MISSING DEPENDENCIES DETECTED")
    print("="*60)
    for dep in missing_deps:
        print(f"{dep} is missing.")
    print("\nInstallation with pip:")
    print("  pip install -r requirements.txt")
    print("\nInstallation with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print("="*60 + "\n")


def process_matrix(
        modules: dict,
        size: int = 1000,
        filename: str = 'matrix_analysis.png'
        ) -> None:
    pd = modules.get('pandas')
    np = modules.get('numpy')
    if not pd or not np:
        raise ImportError(
            "NumPy and Pandas are required to generate matrix data."
            )
    data = {
        'x': np.random.rand(size),
        'y': np.random.rand(size)
    }
    df = pd.DataFrame(data)

    print("\nAnalyzing Matrix data...")
    print(f"Data shape: {df.shape}")
    print(f"Data summary:\n{df.describe()}")

    plt = modules.get('matplotlib.pyplot')
    if not plt:
        raise ImportError("Matplotlib is required to create visualizations.")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['x'], df['y'], alpha=0.5)
    plt.title('Generating visualization...')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.savefig(filename)

    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    modules = import_dependencies()
    versions = check_depedencies(modules)
    required_deps = ['pandas', 'numpy', 'matplotlib']
    missing_deps = [dep for dep in required_deps if not versions[dep]]
    if missing_deps:
        show_installation_instructions(missing_deps)
        return
    process_matrix(modules)


if __name__ == "__main__":
    main()
