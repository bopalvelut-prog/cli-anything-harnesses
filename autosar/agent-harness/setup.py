from setuptools import setup
setup(
    name='cli-anything-autosar',
    version='1.0.0',
    packages=['cli_anything.autosar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autosar=cli_anything.autosar:cli']},
)
