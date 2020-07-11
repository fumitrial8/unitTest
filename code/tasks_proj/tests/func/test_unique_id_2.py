import pytest
from tasks import Task
import tasks

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    uid = tasks.unique_id()
    assert uid not in ids