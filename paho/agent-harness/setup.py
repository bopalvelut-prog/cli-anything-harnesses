from setuptools import setup
setup(
    name='cli-anything-paho',
    version='1.0.0',
    packages=['cli_anything.paho'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paho=cli_anything.paho:cli']},
)
