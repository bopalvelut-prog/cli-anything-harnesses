from setuptools import setup
setup(
    name='cli-anything-keda',
    version='1.0.0',
    packages=['cli_anything.keda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keda=cli_anything.keda:cli']},
)
