"""Test that Python stub files (.pyi) are available and functional."""

from pathlib import Path


def test_stub_files_exist():
    """Test that stub files exist for the main sax package."""
    sax_path = Path(__file__).parent.parent / "sax"
    
    # Check main __init__.pyi exists
    assert (sax_path / "__init__.pyi").exists(), "Main sax/__init__.pyi stub file missing"
    
    # Check py.typed marker exists (required for PEP 561)
    assert (sax_path / "py.typed").exists(), "py.typed marker file missing"
    
    # Check some key module stub files exist
    assert (sax_path / "constants.pyi").exists()
    assert (sax_path / "s.pyi").exists()
    assert (sax_path / "utils.pyi").exists()
    assert (sax_path / "backends" / "__init__.pyi").exists()
    assert (sax_path / "models" / "__init__.pyi").exists()
    assert (sax_path / "saxtypes" / "__init__.pyi").exists()


def test_stub_files_are_valid_python():
    """Test that stub files are valid Python syntax."""
    sax_path = Path(__file__).parent.parent / "sax"
    
    # Test main stub file can be read and is valid Python syntax
    main_stub = sax_path / "__init__.pyi"
    content = main_stub.read_text()
    
    # Compile the stub file to check syntax
    try:
        compile(content, str(main_stub), "exec")
    except SyntaxError as e:
        raise AssertionError(f"Stub file has invalid syntax: {e}") from e


def test_type_hints_available():
    """Test that type hints from stubs are accessible."""
    import sax
    
    # Test that key types are available
    assert hasattr(sax, "FloatArray1D")
    assert hasattr(sax, "SDictModel")
    assert hasattr(sax, "SDict")
    assert hasattr(sax, "Model")
    assert hasattr(sax, "Netlist")
