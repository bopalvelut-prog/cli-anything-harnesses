from setuptools import setup
setup(
    name='cli-anything-communicate',
    version='1.0.0',
    packages=['cli_anything.communicate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-communicate=cli_anything.communicate:cli']},
)
