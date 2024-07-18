import pytest
from plumed_tools.plumed import PlumedInput

def test_plumed_input():
    # Create a valid PlumedInput object
    plumed_input = PlumedInput(
        UNITS="kj/mol",
        DISTANCE=[{"ATOMS": [1, 2], "LABEL": "d"}],
        ANGLE=[{"ATOMS": [1, 2, 3], "LABEL": "a"}],
        TORSION=[{"ATOMS": [1, 2, 3, 4], "LABEL": "t"}],
        COORDINATION=[{"ATOMS": [1, 2, 3], "LABEL": "c"}],
        GROUP=[{"ATOMS": [1, 2, 3], "LABEL": "g"}],
        COM=[{"ATOMS": [1, 2, 3], "LABEL": "com"}],
        UPPER_WALLS=[{"ATOMS": [1, 2], "LABEL": "uw", "KAPPA": 1.0, "EXP": 2}],
        LOWER_WALLS=[{"ATOMS": [1, 2], "LABEL": "lw", "KAPPA": 1.0, "EXP": 2}],
        METAD={"LABEL": "metad", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0},
        OPES_METAD={"LABEL": "opes_metad", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0},
        OPES_METAD_EXPLORE={"LABEL": "opes_metad_explore", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0},
        PRINT=[{"ARG": "d", "FORMAT": "%f"}]
    )

    # Assert that the PlumedInput object is valid
    assert plumed_input.UNITS == "kj/mol"
    assert plumed_input.DISTANCE == [{"ATOMS": [1, 2], "LABEL": "d"}]
    assert plumed_input.ANGLE == [{"ATOMS": [1, 2, 3], "LABEL": "a"}]
    assert plumed_input.TORSION == [{"ATOMS": [1, 2, 3, 4], "LABEL": "t"}]
    assert plumed_input.COORDINATION == [{"ATOMS": [1, 2, 3], "LABEL": "c"}]
    assert plumed_input.GROUP == [{"ATOMS": [1, 2, 3], "LABEL": "g"}]
    assert plumed_input.COM == [{"ATOMS": [1, 2, 3], "LABEL": "com"}]
    assert plumed_input.UPPER_WALLS == [{"ATOMS": [1, 2], "LABEL": "uw", "KAPPA": 1.0, "EXP": 2}]
    assert plumed_input.LOWER_WALLS == [{"ATOMS": [1, 2], "LABEL": "lw", "KAPPA": 1.0, "EXP": 2}]
    assert plumed_input.METAD == {"LABEL": "metad", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0}
    assert plumed_input.OPES_METAD == {"LABEL": "opes_metad", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0}
    assert plumed_input.OPES_METAD_EXPLORE == {"LABEL": "opes_metad_explore", "ARG": "d", "SIGMA": 0.1, "HEIGHT": 2.0}
    assert plumed_input.PRINT == [{"ARG": "d", "FORMAT": "%f"}]

    # Add more assertions for other attributes if needed

if __name__ == "__main__":
    pytest.main()