from setuptools import setup
setup(
    name='cli-anything-terrascan',
    version='1.0.0',
    packages=['cli_anything.terrascan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terrascan=cli_anything.terrascan:cli']},
)
