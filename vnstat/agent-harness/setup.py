from setuptools import setup
setup(
    name='cli-anything-vnstat',
    version='1.0.0',
    packages=['cli_anything.vnstat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vnstat=cli_anything.vnstat:cli']},
)
