from setuptools import setup
setup(
    name='cli-anything-ddclient',
    version='1.0.0',
    packages=['cli_anything.ddclient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ddclient=cli_anything.ddclient:cli']},
)
