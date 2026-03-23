from setuptools import setup
setup(
    name='cli-anything-beego',
    version='1.0.0',
    packages=['cli_anything.beego'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beego=cli_anything.beego:cli']},
)
