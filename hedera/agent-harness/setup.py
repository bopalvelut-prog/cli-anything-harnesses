from setuptools import setup
setup(
    name='cli-anything-hedera',
    version='1.0.0',
    packages=['cli_anything.hedera'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hedera=cli_anything.hedera:cli']},
)
