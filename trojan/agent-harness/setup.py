from setuptools import setup
setup(
    name='cli-anything-trojan',
    version='1.0.0',
    packages=['cli_anything.trojan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trojan=cli_anything.trojan:cli']},
)
