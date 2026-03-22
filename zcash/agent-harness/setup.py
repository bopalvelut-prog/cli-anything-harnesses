from setuptools import setup
setup(
    name='cli-anything-zcash',
    version='1.0.0',
    packages=['cli_anything.zcash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zcash=cli_anything.zcash:cli']},
)
