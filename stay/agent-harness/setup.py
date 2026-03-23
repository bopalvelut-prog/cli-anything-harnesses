from setuptools import setup
setup(
    name='cli-anything-stay',
    version='1.0.0',
    packages=['cli_anything.stay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stay=cli_anything.stay:cli']},
)
