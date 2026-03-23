from setuptools import setup
setup(
    name='cli-anything-adguard',
    version='1.0.0',
    packages=['cli_anything.adguard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adguard=cli_anything.adguard:cli']},
)
