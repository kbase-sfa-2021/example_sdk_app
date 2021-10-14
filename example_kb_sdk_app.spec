/*
A KBase module: example_kb_sdk_app
*/

module example_kb_sdk_app {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_example_kb_sdk_app(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
