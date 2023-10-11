# Contributing Guidelines

Thank you for your interest in contributing to our repository! Whether it's a bug report, new feature, or question, we greatly value feedback and contributions from our community. Read through this document before submitting any issues or pull requests to ensure we have all the necessary information to effectively respond to your bug report or contribution.

In addition to this document, review our [Code of Conduct](CODE_OF_CONDUCT.md). For any code of conduct questions or comments, send an email to [oss@splunk.com](oss@splunk.com).

## Contributor License Agreement

Before contributing, you must sign the [Splunk Contributor License Agreement (CLA)](https://www.splunk.com/en_us/form/contributions.html).

## Contributing to the Observability Workshop

When working on the workshop, we advise that you review your changes locally before committing them, although we prefer Pull Requests. Use the `hugo server` command to live preview your changes (as you type) on your local machine.

## Install Go & Hugo

``` bash
cd ~
```

``` bash
brew install go
```

``` bash
brew install hugo
```

## Cloning the repository

``` bash
git clone https://github.com/splunk/f1-simulator
```

``` bash
cd f1-simulator
```

``` bash
hugo server
```

## Running the docs server

In most cases, the default settings with `hugo server` work well, and Hugo is available at `http://localhost:1313`. If you need to change the port, you can do so by passing the `--port` flag e.g. `hugo server --port=1314`. The documentation built from your current branch is then accessible through your favorite browser at e.g. `http://localhost:1314`.
