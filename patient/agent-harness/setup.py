from setuptools import setup
setup(
    name='cli-anything-patient',
    version='1.0.0',
    packages=['cli_anything.patient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-patient=cli_anything.patient:cli']},
)
