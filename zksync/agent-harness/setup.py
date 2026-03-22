from setuptools import setup
setup(
    name='cli-anything-zksync',
    version='1.0.0',
    packages=['cli_anything.zksync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zksync=cli_anything.zksync:cli']},
)
