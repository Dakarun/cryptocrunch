from setuptools import setup, find_packages

version = '0.0.1'
install_requires = [
    'Flask==2.0.2',
    'Flask-APScheduler==1.12.2',
    'requests==2.26.0'
]

setup(
    name='CryptoCrunch',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
