from setuptools import setup
setup(
    name='cli-anything-welfare',
    version='1.0.0',
    packages=['cli_anything.welfare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-welfare=cli_anything.welfare:cli']},
)
