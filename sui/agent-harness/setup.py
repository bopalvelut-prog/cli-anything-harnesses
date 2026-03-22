from setuptools import setup
setup(
    name='cli-anything-sui',
    version='1.0.0',
    packages=['cli_anything.sui'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sui=cli_anything.sui:cli']},
)
