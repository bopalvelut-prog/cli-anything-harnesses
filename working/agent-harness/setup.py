from setuptools import setup
setup(
    name='cli-anything-working',
    version='1.0.0',
    packages=['cli_anything.working'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-working=cli_anything.working:cli']},
)
