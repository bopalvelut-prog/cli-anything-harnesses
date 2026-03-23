from setuptools import setup
setup(
    name='cli-anything-succeed',
    version='1.0.0',
    packages=['cli_anything.succeed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-succeed=cli_anything.succeed:cli']},
)
