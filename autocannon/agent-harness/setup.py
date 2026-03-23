from setuptools import setup
setup(
    name='cli-anything-autocannon',
    version='1.0.0',
    packages=['cli_anything.autocannon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autocannon=cli_anything.autocannon:cli']},
)
