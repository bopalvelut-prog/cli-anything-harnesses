from setuptools import setup
setup(
    name='cli-anything-wrist',
    version='1.0.0',
    packages=['cli_anything.wrist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrist=cli_anything.wrist:cli']},
)
