from setuptools import setup
setup(
    name='cli-anything-tawk',
    version='1.0.0',
    packages=['cli_anything.tawk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tawk=cli_anything.tawk:cli']},
)
