from setuptools import setup
setup(
    name='cli-anything-dotnetcore',
    version='1.0.0',
    packages=['cli_anything.dotnetcore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dotnetcore=cli_anything.dotnetcore:cli']},
)
