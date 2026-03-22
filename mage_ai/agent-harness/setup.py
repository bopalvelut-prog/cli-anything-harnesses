from setuptools import setup
setup(
    name='cli-anything-mage_ai',
    version='1.0.0',
    packages=['cli_anything.mage_ai'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mage_ai=cli_anything.mage_ai:cli']},
)
