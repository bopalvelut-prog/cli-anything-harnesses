from setuptools import setup
setup(
    name='cli-anything-synthetix',
    version='1.0.0',
    packages=['cli_anything.synthetix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-synthetix=cli_anything.synthetix:cli']},
)
