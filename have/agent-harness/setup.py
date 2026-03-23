from setuptools import setup
setup(
    name='cli-anything-have',
    version='1.0.0',
    packages=['cli_anything.have'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-have=cli_anything.have:cli']},
)
