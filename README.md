# example_kb_sdk_app

This repo demonstrates some best practices for writing KBase Apps

We aim to demonstrate various practicies, such as

### Organization
* Code is organized inside helper classes outside of the impl file. We avoid writing most code in the impl file
* Dependency injection

### Testing
* Unit tests
* Tests running in github actions. (See the [.github](.github) directory)

### Logging
* Use of the logger instead of prints

### Experimental Features
* Usage of KBase Template
* New Base Image



## TODO

- Non KBase tests with mocks
- Update UI spec with correct parameters
- Test optional parameters
- Refine KBase tests, perhaps with assert statements
- Add comments to explain what is going on and why things are done this way.
- See also [Chris' code][chris-code]

[chris-code]: https://github.com/ModelSEED/MetabolicModelGapfilling/blob/master/lib/MetabolicModelGapfilling/core/basemodule.py

## Running Unit Tests

To run the unit tests for this app ensure the image is built by running
`kb-sdk test` once, then run:
```
make docker-unit
```
NOTE: Tests are automatically run via github actions, so you can check to see if your PR passes tests on github

## KB SDK

This is a [KBase](https://kbase.us) module generated by the
[KBase Software Development Kit (SDK)][kb_sdk].

[kb_sdk]: https://github.com/kbase/kb_sdk

You will need to have the SDK installed to use this module.
[Learn more about the SDK and how to use it](https://kbase.github.io/kb_sdk_docs/).

You can also learn more about the apps implemented in this module from its
[catalog page](https://narrative.kbase.us/#catalog/modules/example_kb_sdk_app)
or its [spec file]($module_name.spec).

# Setup and test

Add your KBase developer token to `test_local/test.cfg` and run the following:

```bash
$ make
$ kb-sdk test
```

After making any additional changes to this repo, run `kb-sdk test` again to
verify that everything still works.

# Installation from another module

To use this code in another SDK module, call
`kb-sdk install example_kb_sdk_app`
in the other module's root directory.

# Help

You may find the answers to your questions in our
[FAQ](https://kbase.github.io/kb_sdk_docs/references/questions_and_answers.html)
or [Troubleshooting Guide][troubleshooting-guide].

# example_sdk_app

[troubleshooting-guide]: https://kbase.github.io/kb_sdk_docs/references/troubleshooting.html
