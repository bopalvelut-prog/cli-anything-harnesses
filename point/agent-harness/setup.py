from setuptools import setup
setup(
    name='cli-anything-point',
    version='1.0.0',
    packages=['cli_anything.point'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-point=cli_anything.point:cli']},
)
