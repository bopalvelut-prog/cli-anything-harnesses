from setuptools import setup
setup(
    name='cli-anything-assembla',
    version='1.0.0',
    packages=['cli_anything.assembla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assembla=cli_anything.assembla:cli']},
)
