from setuptools import setup
setup(
    name='cli-anything-dish',
    version='1.0.0',
    packages=['cli_anything.dish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dish=cli_anything.dish:cli']},
)
