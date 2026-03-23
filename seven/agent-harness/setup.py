from setuptools import setup
setup(
    name='cli-anything-seven',
    version='1.0.0',
    packages=['cli_anything.seven'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seven=cli_anything.seven:cli']},
)
