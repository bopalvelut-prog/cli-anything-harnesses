from setuptools import setup
setup(
    name='cli-anything-nikto',
    version='1.0.0',
    packages=['cli_anything.nikto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nikto=cli_anything.nikto:cli']},
)
