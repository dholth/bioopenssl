import pytoml as toml
import enscons
import sys

metadata = dict(toml.load(open("pyproject.toml")))["tool"]["enscons"]

full_tag = "py3-none-any"

env = Environment(
    tools=["default", "packaging", enscons.generate],
    PACKAGE_METADATA=metadata,
    WHEEL_TAG=full_tag,
)

py_source = Glob("bioopenssl/*.py")

sdist = env.SDist(source=FindSourceFiles() + ["PKG-INFO", "setup.py", "README.rst"])
env.NoClean(sdist)
env.Alias("sdist", sdist)

purelib = env.Whl("purelib", py_source, root=".")
whl = env.WhlFile(purelib)

# needed for pep517 / enscons.api to work
env.Default(whl, sdist)
