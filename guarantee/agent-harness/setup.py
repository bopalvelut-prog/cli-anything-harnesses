from setuptools import setup
setup(
    name='cli-anything-guarantee',
    version='1.0.0',
    packages=['cli_anything.guarantee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guarantee=cli_anything.guarantee:cli']},
)
