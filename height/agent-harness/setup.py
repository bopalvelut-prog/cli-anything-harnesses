from setuptools import setup
setup(
    name='cli-anything-height',
    version='1.0.0',
    packages=['cli_anything.height'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-height=cli_anything.height:cli']},
)
