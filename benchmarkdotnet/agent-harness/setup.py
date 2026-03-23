from setuptools import setup
setup(
    name='cli-anything-benchmarkdotnet',
    version='1.0.0',
    packages=['cli_anything.benchmarkdotnet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-benchmarkdotnet=cli_anything.benchmarkdotnet:cli']},
)
