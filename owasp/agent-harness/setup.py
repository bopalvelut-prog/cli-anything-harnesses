from setuptools import setup
setup(
    name='cli-anything-owasp',
    version='1.0.0',
    packages=['cli_anything.owasp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-owasp=cli_anything.owasp:cli']},
)
