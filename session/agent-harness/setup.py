from setuptools import setup
setup(
    name='cli-anything-session',
    version='1.0.0',
    packages=['cli_anything.session'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-session=cli_anything.session:cli']},
)
