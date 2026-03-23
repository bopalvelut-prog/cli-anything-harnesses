from setuptools import setup
setup(
    name='cli-anything-user',
    version='1.0.0',
    packages=['cli_anything.user'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-user=cli_anything.user:cli']},
)
