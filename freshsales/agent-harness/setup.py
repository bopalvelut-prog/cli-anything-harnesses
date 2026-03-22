from setuptools import setup
setup(
    name='cli-anything-freshsales',
    version='1.0.0',
    packages=['cli_anything.freshsales'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freshsales=cli_anything.freshsales:cli']},
)
