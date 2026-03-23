from setuptools import setup
setup(
    name='cli-anything-airvpn',
    version='1.0.0',
    packages=['cli_anything.airvpn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-airvpn=cli_anything.airvpn:cli']},
)
