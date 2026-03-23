from setuptools import setup
setup(
    name='cli-anything-perhaps',
    version='1.0.0',
    packages=['cli_anything.perhaps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perhaps=cli_anything.perhaps:cli']},
)
