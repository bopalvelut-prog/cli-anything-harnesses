from setuptools import setup
setup(
    name='cli-anything-fission',
    version='1.0.0',
    packages=['cli_anything.fission'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fission=cli_anything.fission:cli']},
)
