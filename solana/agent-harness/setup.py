from setuptools import setup
setup(
    name='cli-anything-solana',
    version='1.0.0',
    packages=['cli_anything.solana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solana=cli_anything.solana:cli']},
)
