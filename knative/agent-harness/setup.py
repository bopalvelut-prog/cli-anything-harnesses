from setuptools import setup
setup(
    name='cli-anything-knative',
    version='1.0.0',
    packages=['cli_anything.knative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knative=cli_anything.knative:cli']},
)
