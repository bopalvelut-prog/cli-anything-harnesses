from setuptools import setup
setup(
    name='cli-anything-argilla',
    version='1.0.0',
    packages=['cli_anything.argilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-argilla=cli_anything.argilla:cli']},
)
