from setuptools import setup
setup(
    name='cli-anything-rifle',
    version='1.0.0',
    packages=['cli_anything.rifle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rifle=cli_anything.rifle:cli']},
)
