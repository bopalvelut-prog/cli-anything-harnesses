from setuptools import setup
setup(
    name='cli-anything-typo3',
    version='1.0.0',
    packages=['cli_anything.typo3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typo3=cli_anything.typo3:cli']},
)
