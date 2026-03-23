from setuptools import setup
setup(
    name='cli-anything-cert_manager',
    version='1.0.0',
    packages=['cli_anything.cert_manager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cert_manager=cli_anything.cert_manager:cli']},
)
