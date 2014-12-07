{
    'targets': [
        {
            'target_name': 'cache',
            'type': 'executable',
            'sources': [
                '../../g-map/src/tools/cache/cache.cpp',
                ],
            'dependencies': [
                'mapping.gyp:*',
                ],

            'include_dirs': [
                '../../g-map/src/mapping_core',
                '../3rd/rapidjson/include/',
                '../3rd/agg/include/',
                '../3rd/skia/include/core',
                '../3rd/skia/include/image',
                '../3rd/skia/include/effects',
                '../3rd/skia/include/config',
                '../3rd/skia/include/utils',
                '../3rd/skia/include/pathops',
                ]
            },
        ],
    }
