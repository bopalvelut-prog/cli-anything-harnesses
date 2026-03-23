from setuptools import setup
setup(
    name='cli-anything-camp',
    version='1.0.0',
    packages=['cli_anything.camp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-camp=cli_anything.camp:cli']},
)
