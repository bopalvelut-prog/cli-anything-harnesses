from setuptools import setup
setup(
    name='cli-anything-membership',
    version='1.0.0',
    packages=['cli_anything.membership'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-membership=cli_anything.membership:cli']},
)
