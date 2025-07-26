# app/services/code_executor.py
import subprocess
import time
from typing import Tuple, List, Dict

def execute_python_code(code: str, test_cases: List[Tuple[str, str]], time_limit: float = 2.0) -> Dict:
    results = {
        "status": "Pending",
        "execution_time": None,
        "score": 0,
        "details": []
    }
    
    total_execution_time = 0
    passed_test_cases = 0

    for i, (test_input, expected_output) in enumerate(test_cases):
        start_time = time.time()
        try:
            process = subprocess.run(
                ['python', '-c', code],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=time_limit,
                check=False
            )
            
            execution_time = time.time() - start_time
            total_execution_time += execution_time
            
            output = process.stdout.strip()
            
            if process.returncode != 0:
                results["details"].append({
                    "test_case": i + 1,
                    "status": "Runtime Error",
                    "output": process.stderr.strip(),
                    "expected": expected_output.strip()
                })
                continue

            if output == expected_output.strip():
                passed_test_cases += 1
                results["details"].append({
                    "test_case": i + 1,
                    "status": "Accepted",
                    "output": output,
                    "expected": expected_output.strip()
                })
            else:
                results["details"].append({
                    "test_case": i + 1,
                    "status": "Wrong Answer",
                    "output": output,
                    "expected": expected_output.strip()
                })

        except subprocess.TimeoutExpired:
            total_execution_time += time_limit
            results["details"].append({
                "test_case": i + 1,
                "status": "Time Limit Exceeded",
                "output": "",
                "expected": expected_output.strip()
            })
        except Exception as e:
            results["details"].append({
                "test_case": i + 1,
                "status": "Execution Error",
                "output": str(e),
                "expected": expected_output.strip()
            })

    results["execution_time"] = round(total_execution_time, 4)
    
    if len(test_cases) > 0:
        if passed_test_cases == len(test_cases):
            results["status"] = "Accepted"
            results["score"] = 100
        elif passed_test_cases > 0:
            results["status"] = "Partially Accepted"
            results["score"] = int((passed_test_cases / len(test_cases)) * 100)
        else:
            main_status = "Wrong Answer"
            if results["details"]:
                main_status = results["details"][0]["status"]
            results["status"] = main_status
            results["score"] = 0
    else:
        results["status"] = "Accepted"
        results["score"] = 100

    return results