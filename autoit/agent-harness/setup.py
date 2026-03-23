from setuptools import setup
setup(
    name='cli-anything-autoit',
    version='1.0.0',
    packages=['cli_anything.autoit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autoit=cli_anything.autoit:cli']},
)
