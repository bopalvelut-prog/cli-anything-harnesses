from setuptools import setup
setup(
    name='cli-anything-strength_v2',
    version='1.0.0',
    packages=['cli_anything.strength_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strength_v2=cli_anything.strength_v2:cli']},
)
