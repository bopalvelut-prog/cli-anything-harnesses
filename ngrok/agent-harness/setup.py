from setuptools import setup
setup(
    name='cli-anything-ngrok',
    version='1.0.0',
    packages=['cli_anything.ngrok'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ngrok=cli_anything.ngrok:cli']},
)
