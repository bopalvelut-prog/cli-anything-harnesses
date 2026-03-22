from setuptools import setup
setup(
    name='cli-anything-planka',
    version='1.0.0',
    packages=['cli_anything.planka'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-planka=cli_anything.planka:cli']},
)
