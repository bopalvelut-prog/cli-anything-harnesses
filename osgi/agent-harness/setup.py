from setuptools import setup
setup(
    name='cli-anything-osgi',
    version='1.0.0',
    packages=['cli_anything.osgi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-osgi=cli_anything.osgi:cli']},
)
