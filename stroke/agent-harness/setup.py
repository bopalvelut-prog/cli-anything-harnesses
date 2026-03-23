from setuptools import setup
setup(
    name='cli-anything-stroke',
    version='1.0.0',
    packages=['cli_anything.stroke'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stroke=cli_anything.stroke:cli']},
)
