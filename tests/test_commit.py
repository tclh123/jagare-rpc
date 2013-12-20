# coding: utf-8

from jagare_client import Jagare
from ellen.utils import temp_repo


def test_commit(tmpdir):
    path = tmpdir.strpath
    t_repo = temp_repo.create_temp_repo(path, is_bare=False)

    FILE_NAME = 'test_commit_file_name'
    FILE_CONTENT = """test_content
        test_content
        test_content
        test_content
        """

    data = [(FILE_NAME,
             FILE_CONTENT,
             'insert')]
    ret = Jagare.commit(path, branch='master',
                        parent_ref='master',
                        author_name='testuser',
                        author_email='testuser@xxx.com',
                        message='commit msg',
                        reflog=' ',
                        data=data)

    assert ret is True
    assert FILE_NAME in [node['name'] for node in t_repo.ls_tree('master')]
