# CKEditor 5 configuration without special characters
customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Rojo"},
    {"color": "hsl(340, 82%, 52%)", "label": "Rosa"},
    {"color": "hsl(291, 64%, 42%)", "label": "Morado"},
    {"color": "hsl(262, 52%, 47%)", "label": "Morado Oscuro"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Azul"},
    {"color": "hsl(199, 98%, 48%)", "label": "Azul Cielo"},
    {"color": "hsl(187, 100%, 42%)", "label": "Cian"},
    {"color": "hsl(174, 100%, 29%)", "label": "Verde Azulado"},
    {"color": "hsl(120, 100%, 25%)", "label": "Verde"},
    {"color": "hsl(60, 100%, 50%)", "label": "Amarillo"},
    {"color": "hsl(45, 100%, 51%)", "label": "Naranja"},
    {"color": "hsl(0, 0%, 0%)", "label": "Negro"},
    {"color": "hsl(0, 0%, 50%)", "label": "Gris"},
    {"color": "hsl(0, 0%, 100%)", "label": "Blanco"},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'underline', 'strikethrough', 'link',
                   'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', '|',
                   'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                   'alignment', '|', 'horizontalLine', '|', 'removeFormat', 'insertTable', '|',
                   'undo', 'redo'],
        'fontSize': {
            'options': [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 36, 40, 48, 56, 64, 72]
        },
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Lucida Sans Unicode, Lucida Grande, sans-serif',
                'Tahoma, Geneva, sans-serif',
                'Times New Roman, Times, serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif'
            ]
        },
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                       'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|',
                       'linkImage'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ],
            'upload': {
                'types': ['jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'svg'],
            }
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                              'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Parrafo', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Titulo 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Titulo 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Titulo 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Titulo 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Titulo 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Titulo 6', 'class': 'ck-heading_heading6'}
            ]
        },
        'link': {
            'decorators': {
                'addTargetToExternalLinks': True,
                'defaultProtocol': 'https://',
                'toggleDownloadLink': {
                    'mode': 'manual',
                    'label': 'Descargar archivo',
                    'attributes': {
                        'download': 'file'
                    }
                }
            }
        }
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3', 'heading4', 'heading5', 'heading6',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote', 'codeBlock',
            '|',
            'insertTable',
        ],
        'toolbar': [
            'heading', '|', 
            'outdent', 'indent', '|', 
            'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', '|',
            'link', 'uploadImage', '|',
            'bulletedList', 'numberedList', '|',
            'blockQuote', 'codeBlock', '|',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
            'alignment', '|', 
            'horizontalLine', 'specialCharacters', '|',
            'removeFormat', '|',
            'insertTable', '|',
            'undo', 'redo', '|',
            'sourceEditing'
        ],
        'fontSize': {
            'options': [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 36, 40, 48, 56, 64, 72]
        },
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Lucida Sans Unicode, Lucida Grande, sans-serif',
                'Tahoma, Geneva, sans-serif',
                'Times New Roman, Times, serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif'
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 
                'imageStyle:alignLeft', 'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|',
                'linkImage', '|',
                'resizeImage'
            ],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ],
            'upload': {
                'types': ['jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'svg'],
            },
            'resizeOptions': [
                {
                    'name': 'resizeImage:original',
                    'value': None,
                    'label': 'Original'
                },
                {
                    'name': 'resizeImage:50',
                    'value': '50',
                    'label': '50%'
                },
                {
                    'name': 'resizeImage:75',
                    'value': '75',
                    'label': '75%'
                }
            ],
            'resizeUnit': '%'
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells',
                'tableProperties', 'tableCellProperties', '|',
                'toggleTableCaption'
            ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Parrafo', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Titulo 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Titulo 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Titulo 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Titulo 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Titulo 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Titulo 6', 'class': 'ck-heading_heading6'}
            ]
        },
        'link': {
            'decorators': {
                'addTargetToExternalLinks': True,
                'defaultProtocol': 'https://',
                'toggleDownloadLink': {
                    'mode': 'manual',
                    'label': 'Descargar archivo',
                    'attributes': {
                        'download': 'file'
                    }
                }
            }
        },
        'codeBlock': {
            'languages': [
                {'language': 'css', 'label': 'CSS'},
                {'language': 'html', 'label': 'HTML'},
                {'language': 'javascript', 'label': 'JavaScript'},
                {'language': 'php', 'label': 'PHP'},
                {'language': 'python', 'label': 'Python'},
                {'language': 'java', 'label': 'Java'},
                {'language': 'csharp', 'label': 'C#'},
                {'language': 'cpp', 'label': 'C++'},
                {'language': 'c', 'label': 'C'},
                {'language': 'sql', 'label': 'SQL'},
                {'language': 'bash', 'label': 'Bash'},
                {'language': 'json', 'label': 'JSON'},
                {'language': 'xml', 'label': 'XML'},
                {'language': 'yaml', 'label': 'YAML'},
                {'language': 'markdown', 'label': 'Markdown'},
                {'language': 'plaintext', 'label': 'Texto plano'}
            ]
        }
    }
} 