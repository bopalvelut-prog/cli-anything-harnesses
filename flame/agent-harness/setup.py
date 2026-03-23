from setuptools import setup
setup(
    name='cli-anything-flame',
    version='1.0.0',
    packages=['cli_anything.flame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flame=cli_anything.flame:cli']},
)
