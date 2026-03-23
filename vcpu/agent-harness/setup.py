from setuptools import setup
setup(
    name='cli-anything-vcpu',
    version='1.0.0',
    packages=['cli_anything.vcpu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vcpu=cli_anything.vcpu:cli']},
)
