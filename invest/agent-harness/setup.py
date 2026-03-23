from setuptools import setup
setup(
    name='cli-anything-invest',
    version='1.0.0',
    packages=['cli_anything.invest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-invest=cli_anything.invest:cli']},
)
