from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='iso',
        version='0.0.1',
        url='https://github.com/cervantesjairo/ISO',
        author='Jairo Hernando Cervantes Garcia',
        emai='muiscaenergy@gmail.com',
        description='ISO/RTO data',
        long_description=open('README.md').read(),
        license='MIT license',
        packages=find_packages(),
        zip_safe=False,
        install_requires=[],
    )
