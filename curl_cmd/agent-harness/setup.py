from setuptools import setup
setup(
    name='cli-anything-curl_cmd',
    version='1.0.0',
    packages=['cli_anything.curl_cmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-curl_cmd=cli_anything.curl_cmd:cli']},
)
