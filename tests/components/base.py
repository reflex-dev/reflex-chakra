import pytest
import reflex as rx


def test_deprecated_props(capsys):
    """Assert that deprecated underscore suffix props are translated.

    Args:
        capsys: Pytest fixture for capturing stdout and stderr.
    """

    class C1(rx.Component):
        tag = "C1"

        type: rx.Var[str]
        min: rx.Var[str]
        max: rx.Var[str]

    # No warnings are emitted when using the new prop names.
    c1_1 = C1.create(type="type1", min="min1", max="max1")
    out_err = capsys.readouterr()
    assert not out_err.err
    assert not out_err.out

    c1_1_render = c1_1.render()
    assert 'type={"type1"}' in c1_1_render["props"]
    assert 'min={"min1"}' in c1_1_render["props"]
    assert 'max={"max1"}' in c1_1_render["props"]

    # Deprecation warning is emitted with underscore suffix,
    # but the component still works.
    c1_2 = C1.create(type_="type2", min_="min2", max_="max2")
    out_err = capsys.readouterr()
    assert out_err.out.count("DeprecationWarning:") == 3
    assert not out_err.err

    c1_2_render = c1_2.render()
    assert 'type={"type2"}' in c1_2_render["props"]
    assert 'min={"min2"}' in c1_2_render["props"]
    assert 'max={"max2"}' in c1_2_render["props"]

    class C2(rx.Component):
        tag = "C2"

        type_: rx.Var[str]
        min_: rx.Var[str]
        max_: rx.Var[str]

    # No warnings are emitted if the actual prop has an underscore suffix
    c2_1 = C2.create(type_="type1", min_="min1", max_="max1")
    out_err = capsys.readouterr()
    assert not out_err.err
    assert not out_err.out

    c2_1_render = c2_1.render()
    assert 'type={"type1"}' in c2_1_render["props"]
    assert 'min={"min1"}' in c2_1_render["props"]
    assert 'max={"max1"}' in c2_1_render["props"]