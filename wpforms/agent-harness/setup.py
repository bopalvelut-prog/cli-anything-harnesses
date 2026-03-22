from setuptools import setup
setup(
    name='cli-anything-wpforms',
    version='1.0.0',
    packages=['cli_anything.wpforms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wpforms=cli_anything.wpforms:cli']},
)
