from setuptools import setup
setup(
    name='cli-anything-chevereto',
    version='1.0.0',
    packages=['cli_anything.chevereto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chevereto=cli_anything.chevereto:cli']},
)
