from setuptools import setup
setup(
    name='cli-anything-buzz',
    version='1.0.0',
    packages=['cli_anything.buzz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buzz=cli_anything.buzz:cli']},
)
