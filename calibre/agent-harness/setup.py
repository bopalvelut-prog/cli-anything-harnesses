from setuptools import setup
setup(
    name='cli-anything-calibre',
    version='1.0.0',
    packages=['cli_anything.calibre'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calibre=cli_anything.calibre:cli']},
)
