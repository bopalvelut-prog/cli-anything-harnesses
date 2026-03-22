from setuptools import setup
setup(
    name='cli-anything-clamav',
    version='1.0.0',
    packages=['cli_anything.clamav'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clamav=cli_anything.clamav:cli']},
)
