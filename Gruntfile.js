module.exports = function (grunt) {

    grunt.initConfig({
        cssmin: {
            options: {
                shorthandCompacting: false,
                roundingPrecision: -1
            },
            target: {
                files: {
                    'www/static/css/styles.min.css': [
                        'www/static/css/reset.css',
                        'www/static/css/grid.css',
                        'www/static/css/general.css',
                        'www/static/css/header.css',
                        'www/static/css/footer.css',
                        'www/static/css/page_content.css',
                        'www/static/css/buttons.css',
                        'www/static/css/components.css'
                    ]
                }
            }
        }
    });

    //build tasks
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.registerTask('default', ['cssmin']);
};
