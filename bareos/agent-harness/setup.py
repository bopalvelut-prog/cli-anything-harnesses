from setuptools import setup
setup(
    name='cli-anything-bareos',
    version='1.0.0',
    packages=['cli_anything.bareos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bareos=cli_anything.bareos:cli']},
)
