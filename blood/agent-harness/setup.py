from setuptools import setup
setup(
    name='cli-anything-blood',
    version='1.0.0',
    packages=['cli_anything.blood'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blood=cli_anything.blood:cli']},
)
