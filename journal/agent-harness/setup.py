from setuptools import setup
setup(
    name='cli-anything-journal',
    version='1.0.0',
    packages=['cli_anything.journal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-journal=cli_anything.journal:cli']},
)
