from setuptools import find_packages, setup

setup(
    name='converter',
    version='1.0.0',
    description='a simple speecht to text converter',
    author='Tim Gaspard',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'sqlite3',
        'google-cloud-core'
        'google-cloud-speech'
    ],
)