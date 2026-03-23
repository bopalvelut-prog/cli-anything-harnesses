from setuptools import setup
setup(
    name='cli-anything-onedata',
    version='1.0.0',
    packages=['cli_anything.onedata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-onedata=cli_anything.onedata:cli']},
)
