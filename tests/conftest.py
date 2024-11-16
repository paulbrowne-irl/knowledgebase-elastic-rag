import multiprocessing
import os
import random
import pytest
from datetime import datetime

# interesting note - the main source code to see how PyTest works is in the dunder folders...
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen
from rich.console import Console
#from utils.read_config import get_version

console = Console()


# We can set up global values here via a fixture in root conftest.py
@pytest.fixture(scope="session")  # scope not needed as in root conftest.py
def global_value():
    num_cores = multiprocessing.cpu_count()
    #version = get_version()
    #output = f"\n🖥️  VERSION: {version} - pytest.fixture in root conftest.py️"
    output += f"\nYou have {multiprocessing.cpu_count()} cores 🖥️"
    return output


# ----- OUTPUT FILE AND LOCATION -----
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# practically a GUID...
FILENAME = f"./results/report_{report_date}_{random.randint(1_000_000, 9_999_999)}.csv"


# GLOBAL VALUES accessible from request.config.my_global_value in tests
def pytest_configure(config):

    num_cores = multiprocessing.cpu_count()
    config.my_global_value = f"✅ You have {num_cores} cores ✅"


# ----- Command Line Arguments -----
def pytest_addoption(parser):
    parser.addoption(
        "--desc", action="store_true", default=False, help="sort descending"
    )
    parser.addoption("--asc", action="store_true", default=False, help="sort ascending")
    parser.addoption(
        "--folder", action="store_true", default=False, help="sort by folder"
    )
    parser.addoption(
        "--id_desc", action="store_true", default=False, help="sort by test id desc"
    )
    parser.addoption(
        "--id", action="store_true", default=False, help="sort by test id asc"
    )
    parser.addoption("--rnd", action="store_true", default=False, help="randomise")
    parser.addoption(
        "--collect", action="store_true", default=False, help="coolect only"
    )


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # We get the value of the flag passed in the command line. If both are supplied then we sort by the last flag which is --asc.

    # items is in fact 'tests' but not used as this would clash with the 'test' keyword.

    # We have seen that a test has a test nodeid which is a path to the test. We want to sort by the last part of the path, so we split and get the last part.

    # We then sort by the last part of the path. The nodeid uses '::' as a separator.

    # We print out DESC or ASC depending on the flag passed in the command line for illustration.

    # item.nodeid = tests/tests_03_sort_tests/tests_01_sort_by_testname/test_sort_num.py::test_2

    # default
    # sort by test folder
    items.sort(key=lambda item: item.nodeid.split("/")[1])
    # sort test name desc
    if config.option.desc:
        items.sort(key=lambda item: item.nodeid.split("::")[-1], reverse=True)
    # sort test name asc
    if config.option.asc:
        items.sort(key=lambda item: item.nodeid.split("::")[-1])
    # sort by folder
    if config.option.folder:
        items.sort(key=lambda item: item.nodeid.split("/")[1])
    # sort by test id
    if config.option.id:
        items.sort(key=lambda item: item.nodeid.split("::")[-1].split("_")[1])
    # sort by test id desc
    if config.option.id_desc:
        items.sort(
            key=lambda item: item.nodeid.split("::")[-1].split("_")[1], reverse=True
        )
    if config.option.rnd:
        random.shuffle(items)
    if config.option.collect:
        print("----------------- COLLECT ONLY")
        report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # practically a GUID...
        FILENAME = f"./results/collect_{report_date}_{random.randint(1_000_000, 9_999_999)}.csv"
        with open(f"{FILENAME}", "a") as f:
            for test in items:

                # keyword order is:
                # test name - markers - module name - folder - parent folder/grandparent folder - root folder
                # we have no markers in tests_01_collect_tests
                all_keywords = [str(x) for x in test.keywords]
                all_keywords = ("|").join(all_keywords)

                # print(f"KEYWORDS: \n{all_keywords}\n")
                # we can produce a --collect-only type of report of all test that we are going to run
                list_markers = [
                    str(getattr(test.own_markers[j], "name"))
                    for j in range(len(test.own_markers))
                ]
                all_markers = ("-").join(list_markers)
                test_nodeid = test.nodeid
                # bdd tests have a different format
                if "bdd" in test_nodeid:
                    test_id = test.name.split("_")[2]
                else:
                    test_id = test.name.split("_")[1]

                f.write(f"{test_id}|{test.name}|{all_keywords}|{all_markers}\n")
            pytest.exit("Collect finished", returncode=0)


# ========= CSV RESULTS FILE =========
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # item is actual a test.
    # call is an event that is one of setup - call - teardown
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=call#item

    # this hook needs @pytest.hookimpl(hookwrapper=True) as it must run first and yield to other hooks and other hooks may occur inside it.
    # generally we just use the hook function name.

    # Run all other pytest_runtest_makereport non wrapped hooks and yield the outcome
    outcome = yield
    # report = outcome.get_result() # for reference

    # whe is a property that can be  one of setup, call or teardown.
    if call.when == "call":

        # outcomes can be passed, failed, skipped, xfail, xpass, deselected.AttributeError
        outcome = call.excinfo

        try:
            # Access the test outcome (passed, failed, etc.)

            # Access the test duration.
            test_duration = round(call.duration, 6)
            # Access the test ID (nodeid)
            # e.g tests/tests_01_make_report/test_class.py::TestApp::test_class_01_marked_last
            test_nodeid = item.nodeid
            # bdd tests have a different format
            if "bdd" in test_nodeid:
                test_id = item.name.split("_")[2]
            else:
                test_id = item.name.split("_")[1]

            # markers and keywords - see KEYWORDS.md
            # we will get all the markers for each test
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)
            # print(all_markers)

            # we can customise the format and what we ouput to the file
            # test_id is the item.node.id and is full path to the test that we would use in CLI
            # e.g tests/tests_ex01_make_report/test_class.py::TestApp::test_class_01_marked_last
            # I prefer a pipe delimed CSV '|' as it is easier to read and avoid conflicts with any other delimiters

            # we need 'a' as it adds each item an 'w' would overwrite
            # we can log directly to a DB.
            # the output format can be customised - I use '|' (pipe) as it is easier to read

            # print(f"{item.name}|{test_id}|{outcome}|{test_duration}|{all_markers}")

            # ----- TEST RESULT NAME -----
            with open(FILENAME, "a") as f:
                # we don't need to check for SKIPPED tests as they are not run!
                # if outcome is None this means no assert was raised and the test passed.
                if "xfail" in all_markers and outcome is None:
                    outcome = "X-PASSED"
                elif "xfail" in all_markers and outcome is not None:
                    outcome = "X-FAILED PASSED"
                elif outcome is None:
                    outcome = "PASSED"
                elif outcome is not None:
                    outcome = "FAILED"
                else:
                    outcome = outcome

                f.write(
                    f"{test_id}|{item.name}|{test_nodeid}|{outcome}|{test_duration}|{all_markers}\n"
                )

        except Exception as e:
            print("\nERROR:", e)


# ========= PASS/FAIL STATUS =========
# report is report for a single test
# @pytest.hookimpl
def pytest_report_teststatus(report, config):
    # order seems to matter as the xpassed did not work when placed after passed
    # Handle xfailed and xpassed
    # https://github.com/Teemu/pytest-sugar/blob/main/pytest_sugar.py#L221
    if hasattr(report, "wasxfail"):
        if report.skipped:
            # short desc, long desc
            return "xfailed", "x", ("XFAIL ✅")
        elif report.passed:
            return "xpassed", "❌", ("XPASS ✅❌")
        else:
            return "", "", ""
    if report.when in ("setup", "teardown", "call") and report.skipped:
        return report.outcome, "s", "SKIPPED 🙄 "
    if report.when == "call" and report.passed:
        # we can style the text in long formats. Just color and bold no italic
        # does not work for error?
        return report.outcome, "T", ("PASSED!!!! 😊 ✅", {"cyan": True, "bold": True})
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("FAILED ❌")  # changed from recording


# ========== Report Header =========
def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        output = "============================================="
        output += "\n\t📝 🍀 pytest_report_header 📝"
        print(
            boxen(
                output,
                title="[blue]We can add a report header[/] [black on cyan] here... [/]",
                subtitle="pytest_report_header",
                subtitle_alignment="left",
                color="blue",
                padding=1,
            )
        )
        # We can add another item the report header but it is useful to see that we get a return value that automatically gets added to the terminal report
        return [
            f"\n📝 This is in a pytest_report_header hook and it can access the config built in fixture: {config.my_global_value}"
        ]


def pytest_runtest_call(item):
    # Called to run the test for test item (the call phase).
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest%20item#pytest.Item.add_report_section
    item.add_report_section("call", "custom", "content")


# ========= Terminal Summary =========
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    # this holds record_property custom data
    # output = [report.user_properties for report in reports]
    # output2 = [report.sections for report in reports]
    # content is truthy only if record properties have been set
    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    # console.print(content)
    if content:
        # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=record_property#std-fixture-record_property
        terminalreporter.ensure_newline()
        terminalreporter.section("RECORD PROPERTY", sep="-", red=True, bold=True)
        terminalreporter.line(content)
        print("\n")
        terminalreporter.ensure_newline()
        terminalreporter.section(
            f"Our custom test results section with exit status: {exitstatus}",
            sep="=",
            blue=True,
            bold=True,
            fullwidth=None,
        )
    # change from video - this runs regardless of content having a value
    # content may be empty if no record properties have been set so we have moved this out of the `if content
    print("\n")
    passed_tests = len(terminalreporter.stats.get("passed", ""))
    failed_tests = len(terminalreporter.stats.get("failed", ""))
    skipped_tests = len(terminalreporter.stats.get("skipped", ""))
    error_tests = len(terminalreporter.stats.get("error", ""))
    xfailed_tests = len(terminalreporter.stats.get("xfailed", ""))
    xpassed_tests = len(terminalreporter.stats.get("xpassed", ""))

    total_tests = (
        passed_tests
        + failed_tests
        + skipped_tests
        + error_tests
        + xfailed_tests
        + xpassed_tests
    )

    output = f"Total tests: {total_tests}\n"
    output += f"Passed: {passed_tests}\n"
    output += f"Failed: {failed_tests}\n"
    output += f"Skipped: {skipped_tests}\n"
    output += f"Error: {error_tests}\n"
    output += f"xfailed: {xfailed_tests}\n"
    output += f"xpassed: {xpassed_tests}\n"
    print(
        boxen(
            output,
            title="[green]START OF TEST RESULTS[/]",
            title_alignment="center",
            subtitle="END OF TEST RESULTS",
            subtitle_alignment="center",
            color="green",
            padding=1,
        )
    )
