from setuptools import setup
setup(
    name='cli-anything-express',
    version='1.0.0',
    packages=['cli_anything.express'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-express=cli_anything.express:cli']},
)
