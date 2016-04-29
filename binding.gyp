{
    "targets": [
        {
            "target_name": "anitomy-js",
            "sources": [
                "lib/anitomy/anitomy/anitomy.cpp",
                "lib/anitomy/anitomy/anitomy.h",
                "lib/anitomy/anitomy/element.cpp",
                "lib/anitomy/anitomy/element.h",
                "lib/anitomy/anitomy/keyword.cpp",
                "lib/anitomy/anitomy/keyword.h",
                "lib/anitomy/anitomy/options.h",
                "lib/anitomy/anitomy/parser.cpp",
                "lib/anitomy/anitomy/parser.h",
                "lib/anitomy/anitomy/parser_helper.cpp",
                "lib/anitomy/anitomy/parser_number.cpp",
                "lib/anitomy/anitomy/string.cpp",
                "lib/anitomy/anitomy/string.h",
                "lib/anitomy/anitomy/token.cpp",
                "lib/anitomy/anitomy/token.h",
                "lib/anitomy/anitomy/tokenizer.cpp",
                "lib/anitomy/anitomy/tokenizer.h",
                "src/anitomy_js.h",
                "src/anitomy_js.cpp",
                "src/worker.h",
                "src/worker.cpp",
                "src/addon.cpp"
            ],
            "conditions": [
                [
                    'OS!="win"',
                    {
                        "cflags+": [
                            "-std=c++11"
                        ],
                        "cflags_c+": [
                            "-std=c++11"
                        ],
                        "cflags_cc+": [
                            "-std=c++11"
                        ],
                    }
                ],
                [
                    'OS=="mac"',
                    {
                        "xcode_settings": {
                            "OTHER_CPLUSPLUSFLAGS": [
                                "-std=c++11",
                                "-stdlib=libc++"
                            ],
                            "OTHER_LDFLAGS": [
                                "-stdlib=libc++"
                            ],
                            "MACOSX_DEPLOYMENT_TARGET": "10.7"
                        },
                    }
                ],
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "lib/anitomy"
            ]
        }
    ]
}