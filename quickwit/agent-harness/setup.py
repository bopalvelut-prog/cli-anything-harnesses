from setuptools import setup
setup(
    name='cli-anything-quickwit',
    version='1.0.0',
    packages=['cli_anything.quickwit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quickwit=cli_anything.quickwit:cli']},
)
