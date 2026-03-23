from setuptools import setup
setup(
    name='cli-anything-social',
    version='1.0.0',
    packages=['cli_anything.social'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-social=cli_anything.social:cli']},
)
