from setuptools import setup
setup(
    name='cli-anything-gold',
    version='1.0.0',
    packages=['cli_anything.gold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gold=cli_anything.gold:cli']},
)
