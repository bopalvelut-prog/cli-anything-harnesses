from setuptools import setup
setup(
    name='cli-anything-autohotkey',
    version='1.0.0',
    packages=['cli_anything.autohotkey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autohotkey=cli_anything.autohotkey:cli']},
)
