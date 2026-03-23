from setuptools import setup
setup(
    name='cli-anything-kill',
    version='1.0.0',
    packages=['cli_anything.kill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kill=cli_anything.kill:cli']},
)
