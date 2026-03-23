from setuptools import setup
setup(
    name='cli-anything-clasp',
    version='1.0.0',
    packages=['cli_anything.clasp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clasp=cli_anything.clasp:cli']},
)
