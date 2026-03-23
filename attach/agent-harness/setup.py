from setuptools import setup
setup(
    name='cli-anything-attach',
    version='1.0.0',
    packages=['cli_anything.attach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-attach=cli_anything.attach:cli']},
)
