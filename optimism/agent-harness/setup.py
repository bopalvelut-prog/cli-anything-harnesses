from setuptools import setup
setup(
    name='cli-anything-optimism',
    version='1.0.0',
    packages=['cli_anything.optimism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-optimism=cli_anything.optimism:cli']},
)
