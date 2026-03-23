from setuptools import setup
setup(
    name='cli-anything-yarn',
    version='1.0.0',
    packages=['cli_anything.yarn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yarn=cli_anything.yarn:cli']},
)
