from setuptools import setup
setup(
    name='cli-anything-envoy',
    version='1.0.0',
    packages=['cli_anything.envoy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-envoy=cli_anything.envoy:cli']},
)
