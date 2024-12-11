
1. **Understand the requirements** of the story, work item, or feature that you are working on.
1. **Red: Create a test and make it fail.**
    1. Imagine how the new code should be called and write the test as if the code already existed.
    1. Create the new production code stub. Write just enough code so that it compiles.
    1. Run the test. It should fail. This is a calibration measure to ensure that your test is calling the correct code and that the code is not working by accident. This is a meaningful failure, and you expect it to fail.
1. **Green: Make the test pass by any means necessary.**
    1. Write the production code to make the test pass. Keep it simple.
    1. Some advocate the hard-coding of the expected return value first to verify that the test correctly detects success. This varies from practitioner to practitioner.
    1. If you've written the code so that the test passes as intended, you are finished. You do not have to write more code speculatively. The test is the objective definition of "done." If new functionality is still needed, then another test is needed. Make this one test pass and continue.
    1. When the test passes, you might want to run all tests up to this point to build confidence that everything else is still working.
1. **Refactor: Change the code to remove duplication in your project and to improve the design while ensuring that all tests still pass.**
    1. Remove duplication caused by the addition of the new functionality.
    1. Make design changes to improve the overall solution.
    1. After each refactoring, rerun all the tests to ensure that they all still pass.
1. **Repeat the cycle.** Each cycle should be very short, and a typical hour should contain many Red/Green/Refactor cycles.
