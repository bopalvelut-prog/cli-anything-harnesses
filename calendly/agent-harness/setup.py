from setuptools import setup
setup(
    name='cli-anything-calendly',
    version='1.0.0',
    packages=['cli_anything.calendly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calendly=cli_anything.calendly:cli']},
)
