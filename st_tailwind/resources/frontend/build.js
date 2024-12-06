const esbuild = require('esbuild');

esbuild.build({
    entryPoints: ['init.js'],
    bundle: true,
    outdir: './',
    entryNames: '[name].min',
    minify: true,
    format: 'iife',
    platform: 'browser',
    target: ['es2020'],
    external: [],
    sourcemap: true,
}).then(() => {
    console.log('Build complete! Created bundle.min.js');
}).catch((error) => {
    console.error('Build failed:', error);
    process.exit(1);
});