from setuptools import setup
setup(
    name='cli-anything-mage',
    version='1.0.0',
    packages=['cli_anything.mage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mage=cli_anything.mage:cli']},
)
