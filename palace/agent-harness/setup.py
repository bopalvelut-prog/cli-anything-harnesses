from setuptools import setup
setup(
    name='cli-anything-palace',
    version='1.0.0',
    packages=['cli_anything.palace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-palace=cli_anything.palace:cli']},
)
