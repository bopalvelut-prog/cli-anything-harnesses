from setuptools import setup
setup(
    name='cli-anything-abuseipdb',
    version='1.0.0',
    packages=['cli_anything.abuseipdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-abuseipdb=cli_anything.abuseipdb:cli']},
)
