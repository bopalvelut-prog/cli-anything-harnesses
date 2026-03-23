from setuptools import setup
setup(
    name='cli-anything-struggle',
    version='1.0.0',
    packages=['cli_anything.struggle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-struggle=cli_anything.struggle:cli']},
)
