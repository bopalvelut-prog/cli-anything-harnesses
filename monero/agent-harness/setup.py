from setuptools import setup
setup(
    name='cli-anything-monero',
    version='1.0.0',
    packages=['cli_anything.monero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-monero=cli_anything.monero:cli']},
)
