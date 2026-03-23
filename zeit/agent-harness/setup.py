from setuptools import setup
setup(
    name='cli-anything-zeit',
    version='1.0.0',
    packages=['cli_anything.zeit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zeit=cli_anything.zeit:cli']},
)
