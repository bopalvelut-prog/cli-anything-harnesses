from setuptools import setup
setup(
    name='cli-anything-candle',
    version='1.0.0',
    packages=['cli_anything.candle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-candle=cli_anything.candle:cli']},
)
