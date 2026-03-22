from setuptools import setup
setup(
    name='cli-anything-alchemy',
    version='1.0.0',
    packages=['cli_anything.alchemy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alchemy=cli_anything.alchemy:cli']},
)
