from setuptools import setup
setup(
    name='cli-anything-sdn',
    version='1.0.0',
    packages=['cli_anything.sdn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sdn=cli_anything.sdn:cli']},
)
