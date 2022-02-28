from pathlib import Path
from pytest_mock import MockerFixture

from cleaner.cleaner import prep, clean, main, filter_by_name, index


def test_filter_by_name():
    test_paths = [
        Path('/home/user/test/test1'),
        Path('/home/user/test/asdf'),
        Path('/home/user/test/test2'),
    ]
    assert filter_by_name(test_paths, 'asdf') == [test_paths[1]]


def test_index(mocker: MockerFixture):
    mocker.patch('os.walk', return_value = [
        ('/home/user/test', ['asdf', 'zxcv'], ['test1', 'test2']),
        ('/home/user/test/asdf', [], ['test1', 'test2']),
        ('/home/user/test/zxcv', [], []),
    ])
    assert index('/home/user/test') == [
        Path('/home/user/test/zxcv'),
    ]


def test_prep(mocker: MockerFixture):
    mocker.patch('os.walk', return_value = [
        ('/home/user/test', ['asdf', 'zxcv'], ['test1', 'test2']),
        ('/home/user/test/asdf', [], ['test1', 'test2']),
        ('/home/user/test/zxcv', [], []),
    ])
    
    empties = prep('asdf','zxcv')
    assert empties == [
        Path('/home/user/test/zxcv'),
    ]

def test_clean(mocker: MockerFixture):
    mocker.patch('pathlib.Path.rmdir', return_value = None)
    
    clean([
        Path('/home/user/test/zxcv'),
    ])

def test_main(mocker: MockerFixture):
    mocker.patch('cleaner.cleaner.index', return_value = [
        Path('/home/user/test/zxcv'),
    ])
    mocker.patch('cleaner.cleaner.filter_by_name', return_value = [
        Path('/home/user/test/zxcv'),
    ])
    mocker.patch('pathlib.Path.rmdir', return_value = None)
    mocker.patch('builtins.input', return_value = 'y')
    
    main('asdf', 'asdf')

def test_main_abort(mocker: MockerFixture):
    mocker.patch('cleaner.cleaner.index', return_value = [
        Path('/home/user/test/zxcv'),
    ])
    mocker.patch('cleaner.cleaner.filter_by_name', return_value = [
        Path('/home/user/test/zxcv'),
    ])
    mocker.patch('pathlib.Path.rmdir', return_value = None)
    mocker.patch('builtins.input', return_value = 'n')
    
    main('asdf', 'asdf')