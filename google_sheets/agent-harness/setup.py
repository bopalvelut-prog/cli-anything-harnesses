from setuptools import setup
setup(
    name='cli-anything-google_sheets',
    version='1.0.0',
    packages=['cli_anything.google_sheets'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_sheets=cli_anything.google_sheets:cli']},
)
