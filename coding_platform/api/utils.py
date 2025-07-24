import sys
import io
import traceback
import contextlib
import threading

def run_with_timeout(func, args=(), kwargs={}, timeout=2):
    result = {}

    def wrapper():
        try:
            result['output'] = func(*args, **kwargs)
        except Exception as e:
            result['error'] = str(e)
            result['trace'] = traceback.format_exc()

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return {"output": "Time Limit Exceeded", "error": "Time limit exceeded"}
    
    return result.get('output', {"output": "", "error": result.get('error'), "trace": result.get('trace')})

def run_user_code(code, test_cases, time_limit=2):
    results = []

    for test in test_cases:
        input_data = test['input']
        expected_output = test['expected_output']

        def run_code():
            with io.StringIO(input_data) as stdin, io.StringIO() as stdout:
                sys.stdin = stdin
                with contextlib.redirect_stdout(stdout):
                    exec(code, {})
                return stdout.getvalue().strip()

        run_result = run_with_timeout(run_code, timeout=time_limit)

        output = run_result if isinstance(run_result, str) else run_result.get('output', '')
        error = run_result.get('error') if isinstance(run_result, dict) else None

        results.append({
            "input": input_data,
            "expected_output": expected_output,
            "user_output": output,
            "passed": output == expected_output,
            "error": error if output != expected_output else None
        })

    return results
