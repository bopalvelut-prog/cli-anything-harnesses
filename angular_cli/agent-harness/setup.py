from setuptools import setup
setup(
    name='cli-anything-angular_cli',
    version='1.0.0',
    packages=['cli_anything.angular_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angular_cli=cli_anything.angular_cli:cli']},
)
