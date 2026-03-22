from setuptools import setup
setup(
    name='cli-anything-rescuetime',
    version='1.0.0',
    packages=['cli_anything.rescuetime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rescuetime=cli_anything.rescuetime:cli']},
)
