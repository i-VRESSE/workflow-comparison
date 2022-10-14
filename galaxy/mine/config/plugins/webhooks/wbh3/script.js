window.showWorkflowBuilder = (options) => {
    console.log(options);
    // openHaddock3Tool()
    // TODO wait for tool form to be visible
    // TODO render workflow builder that on run will upload a zip file, fill the galaxy form and execute the tool
    openHaddock3Visualization()
}

function openHaddock3Tool() {
    Galaxy.router.push("/", {
        tool_id: 'haddock3zip',
        version: '1.0.0',
    });
}

function openHaddock3Visualization() {
    Galaxy.router.push("/plugins/visualizations/haddock3/show");
}