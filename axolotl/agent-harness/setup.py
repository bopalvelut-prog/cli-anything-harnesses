from setuptools import setup
setup(
    name='cli-anything-axolotl',
    version='1.0.0',
    packages=['cli_anything.axolotl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-axolotl=cli_anything.axolotl:cli']},
)
