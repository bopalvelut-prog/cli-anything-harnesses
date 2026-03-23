from setuptools import setup
setup(
    name='cli-anything-trophy',
    version='1.0.0',
    packages=['cli_anything.trophy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trophy=cli_anything.trophy:cli']},
)
