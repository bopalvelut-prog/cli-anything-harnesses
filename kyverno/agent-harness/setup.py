from setuptools import setup
setup(
    name='cli-anything-kyverno',
    version='1.0.0',
    packages=['cli_anything.kyverno'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kyverno=cli_anything.kyverno:cli']},
)
