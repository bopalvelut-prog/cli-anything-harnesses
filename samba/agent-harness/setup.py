from setuptools import setup
setup(
    name='cli-anything-samba',
    version='1.0.0',
    packages=['cli_anything.samba'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-samba=cli_anything.samba:cli']},
)
