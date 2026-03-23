from setuptools import setup
setup(
    name='cli-anything-cap',
    version='1.0.0',
    packages=['cli_anything.cap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cap=cli_anything.cap:cli']},
)
