from setuptools import setup
setup(
    name='cli-anything-zenml',
    version='1.0.0',
    packages=['cli_anything.zenml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zenml=cli_anything.zenml:cli']},
)
