from setuptools import setup
setup(
    name='cli-anything-arweave',
    version='1.0.0',
    packages=['cli_anything.arweave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arweave=cli_anything.arweave:cli']},
)
