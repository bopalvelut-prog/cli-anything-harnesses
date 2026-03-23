from setuptools import setup
setup(
    name='cli-anything-equip',
    version='1.0.0',
    packages=['cli_anything.equip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-equip=cli_anything.equip:cli']},
)
