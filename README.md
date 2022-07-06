# SBOL Examples

Welcome to SBOL Examples! Please feel free to use this repository to browse through or propose new SBOL or SBOLVisual examples.


## Repository Structure
This repository contains examples for [SBOL Data Model](https://sbolstandard.org/datamodel-about/) and [SBOL Visual](https://sbolstandard.org/visual-about/). 
For each SBOL and SBOL visual, we have three types of examples (in the respective subfolder): 
- Best Practices: These are examples or guidelines that have been examined thoroughly by the SBOL editors and the SBOL community. These types of examples and guidelines are widely recommended as community standards for representing your data in SBOL or SBOL Visual. 
- Curated Examples: These are examples that have been curated by the SBOL editors. These examples follow best practices and serve as points of reference for the community to understand how they can represent their data using SBOL. Curated examples will be well documented and would have gone through a discussion process to be considered.
- Uncurated Examples: There may not always be "one right way" to represent your data. While there the SBOL community recommends using the best practices, we don't want to restrict the way SBOL is used by the wider community. This is a place where the community can store either: 
    - SBOL (Data or Visual) files that you have created as part of your project or workflow that you would like to share with the community.
    - An SBOL file that does not follow the best practices but is still useful in your project. In such cases, we would love to understand why the best practices were not relevant or applicable for your use case.


## Submitting a new example. 
**The contents of this repository will be moderated by the SBOL editors to ensure that the examples are organized and accessible**. However, we encourage submissions from anyone in the SBOL community. 

To submit an example, please ensure you follow these steps: 
- [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the `SBOL-examples` repository. 
- Create a new folder in the `uncurated-examples` subfolder in either SBOL or SBOL-Visual depending on the type of example you would like to submit.
    - Please ensure that the name of the subfolder is short and mnemonic so that it is easy to identify your example. 
    - Please note that even if you wish to submit a single file, we recommend creating a folder and adding the file to that folder. This is so that we can add additional README documents within that folder to add documentation for your example.
    - Please note that the SBOL editors might change the name of the file or folder to make it more consistent with the rest of the examples in the repository.
    - As a general naming convention, please use the following format for both files and folders:
       - Please ensure that all names start with lower case alphabets. 
       - If your file or folder name has multiple words, please use an underscore to separate the words.
- Create a new [topic branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) for your proposed example. Again, please ensure that the topic branch has a mnemonic name. We recommend the following format: _\<name of individual or organisation\>/\<branch name\>_. 
- Submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) for your branch.

At this point, you have two options for your submitted example: 
1. If you would like your example to be considered as a **curated example** or **best practice**, please [start a new discussion](https://github.com/SynBioDex/SBOL-examples/discussions/new). 
    - During the discussion process, the SBOL editors will also examine if the example follows the recommended SBOL guidelines. If so, the example will be moved to the `curated-examples` sub-folder. 
    - If you would like your example to be considered as a **best practice**, please include a short reasoning within the discussion as to why your example should be considered as a best practice. The discussion will give the SBOL editors and the community a chance to review your example and decide whether it should be a **best practice**.   
2. If you simply wish to submit your example (where it remains in the `uncurated-examples` folder), please indicate this in the Pull Request via comments. The editors will review the PR and merge if appropriate. 
