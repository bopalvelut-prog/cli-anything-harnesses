from setuptools import setup
setup(
    name='cli-anything-enemy',
    version='1.0.0',
    packages=['cli_anything.enemy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enemy=cli_anything.enemy:cli']},
)
