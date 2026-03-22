from setuptools import setup
setup(
    name='cli-anything-loopring',
    version='1.0.0',
    packages=['cli_anything.loopring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loopring=cli_anything.loopring:cli']},
)
