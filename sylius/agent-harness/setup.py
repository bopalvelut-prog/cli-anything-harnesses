from setuptools import setup
setup(
    name='cli-anything-sylius',
    version='1.0.0',
    packages=['cli_anything.sylius'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sylius=cli_anything.sylius:cli']},
)
