from setuptools import setup
setup(
    name='cli-anything-xray',
    version='1.0.0',
    packages=['cli_anything.xray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xray=cli_anything.xray:cli']},
)
