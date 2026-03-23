from setuptools import setup
setup(
    name='cli-anything-volttron',
    version='1.0.0',
    packages=['cli_anything.volttron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volttron=cli_anything.volttron:cli']},
)
