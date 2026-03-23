from setuptools import setup
setup(
    name='cli-anything-mine',
    version='1.0.0',
    packages=['cli_anything.mine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mine=cli_anything.mine:cli']},
)
