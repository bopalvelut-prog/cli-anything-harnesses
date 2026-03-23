from setuptools import setup
setup(
    name='cli-anything-pydantic',
    version='1.0.0',
    packages=['cli_anything.pydantic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pydantic=cli_anything.pydantic:cli']},
)
