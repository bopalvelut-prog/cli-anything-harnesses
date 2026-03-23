from setuptools import setup
setup(
    name='cli-anything-projector',
    version='1.0.0',
    packages=['cli_anything.projector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-projector=cli_anything.projector:cli']},
)
