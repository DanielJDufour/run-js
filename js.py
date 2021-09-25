import json
import os
import random
import re
import subprocess
import sys
from types import ModuleType

DEBUG_RUN_JS = os.getenv("DEBUG_RUN_JS", False) in [
    "TRUE",
    "true",
    "True",
    "T",
    "t",
    "1",
]

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

CWD = os.getcwd()


class NodeFunction:
    def __init__(self, function_name, module_name):
        self.module_name = module_name
        self.function_name = function_name

    def __call__(self, *args, **kwargs):
        if DEBUG_RUN_JS:
            print(
                '[js] calling function "'
                + self.function_name
                + '" from module "'
                + self.module_name
                + '"'
            )

        if kwargs:
            raise "[js] run-js does not support keyword arguments"

        boundary = "\n--results-below-" + str(random.randint(1e2, 1e10)) + "--\n"

        data = {
            "module_name": self.module_name,
            "function_name": self.function_name,
            "params": args,
            "boundary": boundary,
        }

        dumped = json.dumps(data)

        file_path = os.path.join(DIR_PATH, "run.js")

        process = subprocess.Popen(
            ["node", file_path],
            shell=False,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            cwd=CWD,
        )
        output, err = process.communicate(dumped, timeout=60)

        if process.returncode != 0:
            print(
                "[run-js] the JavaScript command returned a non-zero exit code, so we are printing the error log, so you can figure out what happened"
            )
            print(err)
            msg = next(
                ln for ln in err.split("\n") if re.match("^([A-Z][a-z]+)?Error:", ln)
            )
            if msg:
                raise Exception(msg)
            raise Exception("[js.py] Command Failed")

        splat = output.split(boundary)

        if len(splat) != 2:
            log = splat[0]
            print(log)
            return None

        log, results = splat
        print(log)
        return json.loads(results)

    def __str__(self):
        return self.module_name + "." + self.function_name


class NodeModule:
    def __init__(self, module_name):
        self.module_name = module_name

        file_path = os.path.join(DIR_PATH, "exists.js")

        # check if need to install module
        process = subprocess.Popen(
            ["node", file_path],
            shell=False,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            cwd=CWD,
        )
        process.communicate(module_name, timeout=60)

        if process.returncode == 1:
            # module_name might include a subpath, so remove that
            if "/" in module_name:
                module_name = module_name.split("/")[0]

            print("it doesn't appear that " + module_name + " is installed")
            print("We will now install it via https://www.npmjs.com/")
            res = input("Press Y (yes) to continue or N (no) to cancel.\n")
            if res.upper() not in ["Y", "YES"]:
                raise Exception(
                    'module by the name "' + module_name + '" is not installed.'
                )

            # validate module_name
            if not re.match(r"^@?[A-Za-z_\-\.\/]+$", module_name):
                raise Exception("invalid module name")

            # create package.json if none exists
            package_json_file_path = os.path.join(CWD, "package.json")
            if not os.path.isfile(package_json_file_path):
                with open(package_json_file_path, mode="w", encoding="utf-8") as f:
                    f.write(json.dumps({"name": "run-js", "private": True}))

            print("installing " + module_name)
            subprocess.call(["npm", "install", module_name], shell=False, cwd=CWD)

    def __getattr__(self, function_name):
        if DEBUG_RUN_JS:
            print(
                '[js] loading function "'
                + function_name
                + '" from module "'
                + self.module_name
                + '"'
            )
        return NodeFunction(function_name=function_name, module_name=self.module_name)

    def __getitem__(self, function_name):
        if DEBUG_RUN_JS:
            print(
                '[js] loading function "'
                + function_name
                + '" from module "'
                + self.module_name
                + '"'
            )
        return NodeFunction(function_name=function_name, module_name=self.module_name)

    def __call__(self, *args):
        return NodeFunction(module_name=self.module_name, function_name="default")(
            *args
        )


class ModuleWrapper(ModuleType):
    __path__ = []

    def __init__(self, module):
        # hack learned from https://github.com/amoffat/sh
        super().__init__(
            name=getattr(module, "__name__", None),
            doc=getattr(module, "__doc__", None),
        )

    def __getitem__(self, key):
        if DEBUG_RUN_JS:
            print('[js] ModuleWrapper getting item "' + key + '"')
        return NodeModule(module_name=key)

    def __getattr__(self, attr):
        if DEBUG_RUN_JS:
            print('[js] ModuleWrapper getting attribute"' + attr + '"')
        return NodeModule(module_name=attr)


if __name__ != "__main__":
    if DEBUG_RUN_JS:
        print("[js] importing " + __name__)
    sys.modules[__name__] = ModuleWrapper(sys.modules[__name__])
