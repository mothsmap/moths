{
	"includes": [
		    '../3rd/skia/gyp/common.gypi',
		    ],
    'targets': [
        {
            'target_name': 'mapping',
            'type': 'static_library',
            'includes': [
                'mapping.gypi'
                ],
            'sources': [
                'mapping.gypi'
                ],

             'dependencies': [
                    '../3rd/skia/gyp/etc1.gyp:libetc1',
                    '../3rd/skia/gyp/flags.gyp:flags',
                    '../3rd/skia/gyp/jsoncpp.gyp:jsoncpp',
                    '../3rd/skia/gyp/pdf.gyp:pdf',
                    '../3rd/skia/gyp/skia_lib.gyp:skia_lib',
                    '../3rd/skia/gyp/tools.gyp:crash_handler',
                    '../3rd/skia/gyp/tools.gyp:gm_expectations',
                    '../3rd/skia/gyp/tools.gyp:proc_stats',
                    '../3rd/skia/gyp/tools.gyp:resources',
                    '../3rd/skia/gyp/tools.gyp:sk_tool_utils',
                    ],

    #        'direct_dependent_settings': {
                'include_dirs': [
                    '../../g-map/src/mapping_core/',
                    '../3rd/rapidjson/include/',
                    '../3rd/agg/include/',
                    '../3rd/skia/src/core',
                    '../3rd/skia/src/effects',
                    '../3rd/skia/src/images',
                    '../3rd/skia/src/pipe/utils',
                    '../3rd/skia/src/utils',
                    ],
                'defines': [
                    '_USE_MATH_DEFINES',
                    ],
#                },

            'link_settings': {
                "ldflags": [
                    '-lgeos_c',
                    '-lgdal',
                    '-L/usr/local/lib',
                    '-lprotobuf-lite',
                    '-L/home/xuxiang/Documents/boost_1_56_0/stage/lib/',
                    '-lboost_system',
                    '-lboost_thread',
                    '-lboost_filesystem',
                    ],
                },
            },
        ],
    }
