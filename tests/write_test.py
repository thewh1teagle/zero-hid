import io
import time
from unittest import mock
from zero_hid import hid



def test_process_with_result_child_completed():
    def target():
        pass

    process = hid.write.ProcessWithResult(target=target, daemon=True)
    process.start()
    process.join()
    result = process.result()
    assert result.was_successful()
    assert hid.write.ProcessResult(return_value=None, exception=None) == result

def test_process_with_result_child_not_completed():

    def target():
        time.sleep(1)

    process = hid.write.ProcessWithResult(target=target, daemon=True)
    process.start()
    # Get the result before the child process has completed.
    assert process.result() is None

    # Clean up the running child process.
    process.kill()

def test_process_with_result_child_exception():

    def target():
        raise Exception('Child exception')

    # Silence stderr while the child exception is being raised to avoid
    # polluting the terminal output.
    with mock.patch('sys.stderr', io.StringIO()):
        process = hid.write.ProcessWithResult(target=target, daemon=True)
        process.start()
        process.join()
    result = process.result()
    assert result.was_successful() == False
    assert hid.write.ProcessResult(return_value=None, exception=mock.ANY) == result
    assert 'Child exception' == str(result.exception)

def test_process_with_result_return_value():

    def target():
        return 'Done!'

    process = hid.write.ProcessWithResult(target=target, daemon=True)
    process.start()
    process.join()
    result = process.result()
    assert result.was_successful()
    assert hid.write.ProcessResult(return_value='Done!', exception=None) == result