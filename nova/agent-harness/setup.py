from setuptools import setup
setup(
    name='cli-anything-nova',
    version='1.0.0',
    packages=['cli_anything.nova'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nova=cli_anything.nova:cli']},
)
