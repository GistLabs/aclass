# Prequisites

NOTE: All applications can also be installed using [homebrew](https://brew.sh/)

### Required
* Python 3.8+ -- `python3 --version` -- https://docs.python-guide.org/starting/install3/osx/  -- `brew install python3`
* node.js v12+ -- `node --version` -- https://nodejs.org/en/download/package-manager/#macos -- `brew install node`
* Docker Desktop -- `docker --version` -- https://docs.docker.com/docker-for-mac/install/ -- `brew install --cask docker`

### Recommended
* VSCode -- `code --version` -- https://code.visualstudio.com/docs/setup/mac -- `brew install --cask visual-studio-code`

Note: Any code editor will do.  Support for python and javascript is ideal.

### Configuration

Please enable a kubernetes cluster on your local machine using the docker desktop dashboard. 

1. From the docker desktop tray select `Dashboard`
2. Select the gear icon in the upper right
3. Select `Kubernetes` from the list on the left
4. Check the `Enable Kubernetes` checkbox -- this will take a minute or two to determine if it is running.
5. Verify installation by runing `kubectl get pods --all-namespaces` and seeing output of running system containers.

If you run in to trouble no sweat.  We will have time to cover this.