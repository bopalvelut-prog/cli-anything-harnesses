from setuptools import setup
setup(
    name='cli-anything-klaytn',
    version='1.0.0',
    packages=['cli_anything.klaytn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-klaytn=cli_anything.klaytn:cli']},
)
