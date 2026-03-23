from setuptools import setup
setup(
    name='cli-anything-finalcut',
    version='1.0.0',
    packages=['cli_anything.finalcut'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-finalcut=cli_anything.finalcut:cli']},
)
