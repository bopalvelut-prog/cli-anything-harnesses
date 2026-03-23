from setuptools import setup
setup(
    name='cli-anything-role',
    version='1.0.0',
    packages=['cli_anything.role'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-role=cli_anything.role:cli']},
)
