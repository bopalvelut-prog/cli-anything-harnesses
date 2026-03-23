from setuptools import setup
setup(
    name='cli-anything-pulumi',
    version='1.0.0',
    packages=['cli_anything.pulumi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pulumi=cli_anything.pulumi:cli']},
)
