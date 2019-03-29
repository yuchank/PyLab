from setuptools import setup, find_packages

setup(
    # name='argparseex',
    name='cello',
    version='1.0.0',
    author='Qing',
    author_email='qing@email.com',
    description='Greet someone',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            # 'greet = cliex.argparseex:main'
            'cello = cliex.clickex:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)