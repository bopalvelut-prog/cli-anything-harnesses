from setuptools import setup
setup(
    name='cli-anything-vuln',
    version='1.0.0',
    packages=['cli_anything.vuln'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vuln=cli_anything.vuln:cli']},
)
