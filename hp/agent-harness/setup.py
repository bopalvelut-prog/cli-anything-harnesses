from setuptools import setup
setup(
    name='cli-anything-hp',
    version='1.0.0',
    packages=['cli_anything.hp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hp=cli_anything.hp:cli']},
)
