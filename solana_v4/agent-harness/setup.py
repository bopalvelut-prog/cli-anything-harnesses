from setuptools import setup
setup(
    name='cli-anything-solana_v4',
    version='1.0.0',
    packages=['cli_anything.solana_v4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solana_v4=cli_anything.solana_v4:cli']},
)
