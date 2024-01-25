import { ComfyApp } from '../scripts/app';
import { ComfyNode } from '../scripts/comfyNode';
import { ComfyExtension } from '../types/comfy';

const ext: ComfyExtension = {
    // Unique name for the extension
    name: 'Example.LoggingExtension',
    async init(app: ComfyApp) {
        // Any initial setup to run as soon as the page loads
        console.log('[logging]', 'extension init');
    },
    async setup(app: ComfyApp) {
        // Any setup to run after the app: ComfyApp is created
        console.log('[logging]', 'extension setup');
    },
    async addCustomNodeDefs(defs, app) {
        // Add custom node definitions
        // These definitions will be configured and registered automatically
        // defs is a lookup core nodes, add yours into this
        console.log('[logging]', 'add custom node definitions', 'current nodes:', Object.keys(defs));
    },
    async getCustomWidgets(app) {
        // Return custom widget types
        // See ComfyWidgets for widget examples
        console.log('[logging]', 'provide custom widgets');
        return {};
    },
    async beforeRegisterNodeDef(nodeType, nodeData: any, app: ComfyApp) {
        // Run custom logic before a node definition is registered with the graph
        console.log('[logging]', 'before register node: ', nodeType, nodeData);

        // This fires for every node definition so only log once
        delete ext.beforeRegisterNodeDef;
    },
    async registerCustomNodes(app) {
        // Register any custom node implementations here allowing for more flexability than a custom node def
        console.log('[logging]', 'register custom nodes');
    },
    async loadedGraphNode(node, app) {
        // Fires for each node when loading/dragging/etc a workflow json or png
        // If you break something in the backend and want to patch workflows in the frontend
        // This is the place to do this
        console.log('[logging]', 'loaded graph node: ', node);

        // This fires for every node on each load so only log once
        delete ext.loadedGraphNode;
    },
    async nodeCreated(node, app) {
        // Fires every time a node is constructed
        // You can modify widgets/add handlers/etc here
        console.log('[logging]', 'node created: ', node);

        // This fires for every node so only log once
        delete ext.nodeCreated;
    },
};

// TO DO: do we want this to be a class or instance method?
// ComfyApp.registerExtension(ext);
// OR
// const app = new ComfyApp();
// app.registerExtension(ext);