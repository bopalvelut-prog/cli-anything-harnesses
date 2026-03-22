from setuptools import setup
setup(
    name='cli-anything-ssl_cert',
    version='1.0.0',
    packages=['cli_anything.ssl_cert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ssl_cert=cli_anything.ssl_cert:cli']},
)
