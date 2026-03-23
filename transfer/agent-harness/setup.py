from setuptools import setup
setup(
    name='cli-anything-transfer',
    version='1.0.0',
    packages=['cli_anything.transfer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transfer=cli_anything.transfer:cli']},
)
