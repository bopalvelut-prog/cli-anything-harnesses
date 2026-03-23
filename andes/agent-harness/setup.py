from setuptools import setup
setup(
    name='cli-anything-andes',
    version='1.0.0',
    packages=['cli_anything.andes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-andes=cli_anything.andes:cli']},
)
