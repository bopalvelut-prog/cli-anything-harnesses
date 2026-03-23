from setuptools import setup
setup(
    name='cli-anything-triple',
    version='1.0.0',
    packages=['cli_anything.triple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-triple=cli_anything.triple:cli']},
)
