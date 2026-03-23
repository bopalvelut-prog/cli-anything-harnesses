from setuptools import setup
setup(
    name='cli-anything-fossa',
    version='1.0.0',
    packages=['cli_anything.fossa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fossa=cli_anything.fossa:cli']},
)
