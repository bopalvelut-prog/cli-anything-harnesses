from setuptools import setup
setup(
    name='cli-anything-authentication',
    version='1.0.0',
    packages=['cli_anything.authentication'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authentication=cli_anything.authentication:cli']},
)
