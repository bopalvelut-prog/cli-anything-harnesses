from setuptools import setup
setup(
    name='cli-anything-kucoin',
    version='1.0.0',
    packages=['cli_anything.kucoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kucoin=cli_anything.kucoin:cli']},
)
