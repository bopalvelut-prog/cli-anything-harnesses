from setuptools import setup
setup(
    name='cli-anything-invite',
    version='1.0.0',
    packages=['cli_anything.invite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-invite=cli_anything.invite:cli']},
)
