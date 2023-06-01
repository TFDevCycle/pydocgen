import inspect
import os
import re
import glob

class generatedoc():
    
    """
    A class for generating HTML documentation for Python modules, classes, and methods.

    Args:
        directory (str): The directory path containing the Python modules.
        output_dir (str): The output directory where the generated documentation will be saved.

    Methods:
        __init__(self, directory, output_dir):
            Initializes the generatedoc object and starts the documentation generation process.

        escape_html(text):
            Escapes special characters in the given text.

        startgenerate():
            Starts the documentation generation process.

    Example usage:
        directory = "."  # Replace with the desired directory path
        output_dir = "docs"
        generatedoc(directory, output_dir)
    """

    def __init__(self, directory, output_dir):
        os.makedirs(output_dir, exist_ok=True)

        files = glob.glob(os.path.join(directory, "*.py"))
        module_docs = []

        for file_path in files:
            module_name = os.path.basename(file_path)[:-3]
            module = __import__(module_name)

            docstring = module.__doc__ if module.__doc__ else ""
            module_output_file = os.path.join(output_dir, f"{module_name}_doc.html")
            module_docs.append((module_name, module_output_file))

            with open(module_output_file, "w") as f:
                f.write("<html>\n")
                f.write("<head>\n")
                f.write('<link rel="stylesheet" type="text/css" href="../style.css">\n')  # Add stylesheet link
                f.write("</head>\n")
                f.write("<body>\n")

                # Add back and home buttons
                f.write('<div class="button-container">')
                f.write('<a class="home-button" href="../index.html">Home</a> &nbsp;&nbsp;')
                f.write('<a class="back-button" href="javascript:history.back()">Back</a>')
                f.write('</div>\n')

                f.write(f"<h1>{module_name} Documentation</h1>\n")
                f.write("<hr>\n")
                if docstring:
                    f.write(f"<pre>{escape_html(docstring)}</pre>\n")
                else:
                    f.write("<p>No module-level docstring.</p>\n")
                f.write("<hr>\n")

                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj):
                        class_docstring = obj.__doc__ if obj.__doc__ else ""
                        if class_docstring:
                            class_output_file = os.path.join(output_dir, f"{module_name}.{name}_doc.html")
                            with open(class_output_file, "w") as f_class:
                                f_class.write("<html>\n")
                                f_class.write("<head>\n")
                                f_class.write('<link rel="stylesheet" type="text/css" href="../../../style.css">\n')  # Add stylesheet link
                                f_class.write("</head>\n")
                                f_class.write("<body>\n")

                                # Add back and home buttons
                                f_class.write('<div class="button-container">')
                                f_class.write('<a class="home-button" href="../../../index.html">Home</a> &nbsp;&nbsp;')
                                f_class.write('<a class="back-button" href="javascript:history.back()">Back</a>')
                                f_class.write('</div>\n')

                                f_class.write(f"<h1>{module_name}.{name} Class Documentation</h1>\n")
                                f_class.write("<hr>\n")
                                if class_docstring:
                                    f_class.write(f"<pre>{escape_html(class_docstring)}</pre>\n")
                                else:
                                    f_class.write("<p>No class docstring.</p>\n")
                                f_class.write("<hr>\n")

                                # Add class documentation to the module page
                                cof = class_output_file.replace("docs\\", "")
                                f.write(f'<p><a href="{cof}">{name}</a></p>\n')

                                for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                                    method_docstring = method.__doc__ if method.__doc__ else ""
                                    if method_docstring:
                                        method_output_file = os.path.join(output_dir, f"{module_name}.{name}.{method_name}_doc.html")
                                        with open(method_output_file, "w") as f_method:
                                            f_method.write("<html>\n")
                                            f_method.write("<head>\n")
                                            f_method.write('<link rel="stylesheet" type="text/css" href="../../../style.css">\n')  # Add stylesheet link
                                            f_method.write("</head>\n")
                                            f_method.write("<body>\n")

                                            # Add back and home buttons
                                            f_method.write('<div class="button-container">')
                                            f_method.write('<a class="home-button" href="../../../../index.html">Home</a> &nbsp;&nbsp;')
                                            f_method.write('<a class="back-button" href="javascript:history.back()">Back</a>')
                                            f_method.write('</div>\n')

                                            f_method.write(f"<h1>{module_name}.{name}.{method_name} Method Documentation</h1>\n")
                                            f_method.write("<hr>\n")
                                            if method_docstring:
                                                f_method.write(f"<pre>{escape_html(method_docstring)}</pre>\n")
                                            else:
                                                f_method.write("<p>No method docstring.</p>\n")
                                            f_method.write("<hr>\n")

                                            # Add method documentation to the class page
                                            mof = method_output_file.replace("docs\\", "")
                                            f_class.write(f'<p><a href="{mof}">{method_name}</a></p>\n')
                # Generate style.css
                style_file_path = os.path.join("style.css")
                with open(style_file_path, "w") as f_style:
                    f_style.write("/* style.css */\n")
                    f_style.write("\n")
                    f_style.write("body {\n")
                    f_style.write("    font-family: Arial, sans-serif;\n")
                    f_style.write("    margin: 20px;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write("h1 {\n")
                    f_style.write("    color: #333;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write("pre {\n")
                    f_style.write("    background-color: #f5f5f5;\n")
                    f_style.write("    padding: 10px;\n")
                    f_style.write("    border-radius: 5px;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write(".button-container {\n")
                    f_style.write("    margin-bottom: 10px;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write(".home-button, .back-button {\n")
                    f_style.write("    display: inline-block;\n")
                    f_style.write("    padding: 5px 10px;\n")
                    f_style.write("    background-color: #007bff;\n")
                    f_style.write("    color: #fff;\n")
                    f_style.write("    text-decoration: none;\n")
                    f_style.write("    border-radius: 3px;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write(".home-button:hover, .back-button:hover {\n")
                    f_style.write("    background-color: #0056b3;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write("ul {\n")
                    f_style.write("    list-style-type: none;\n")
                    f_style.write("    padding: 0;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write("ul li {\n")
                    f_style.write("    margin-bottom: 5px;\n")
                    f_style.write("}\n")
                    f_style.write("\n")
                    f_style.write("a {\n")
                    f_style.write("    text-decoration: none;\n")
                    f_style.write("    color: #007bff;\n")
                    f_style.write("}\n")
                    f_style.write("a:hover {\n")
                    f_style.write("    text-decoration: underline;\n")
                    f_style.write("}\n")
                    f_style.write("\n")

                # Generate index.html
                index_file_path = os.path.join("index.html")
                with open(index_file_path, "w") as f_index:
                    f_index.write("<html>\n")
                    f_index.write("<head>\n")
                    f_index.write('<link rel="stylesheet" type="text/css" href="style.css">\n')  # Add stylesheet link
                    f_index.write("</head>\n")
                    f_index.write("<body>\n")
                    f_index.write("<h1>Documentation Index</h1>\n")
                    f_index.write("<ul>\n")
                    for module_name, module_file in module_docs:
                        print(module_file)
                        f_index.write(f'<li><a href="{module_file}">{module_name}</a></li>\n')
                    f_index.write("</ul>\n")
                    f_index.write("</body>\n")
                    f_index.write("</html>\n")

def escape_html(text):
    """Escape special characters in the given text."""
    return re.sub(r"[<>&]", lambda m: {"<": "&lt;", ">": "&gt;", "&": "&amp;"}[m.group()], str(text))

def startgenerate():
    # Example usage
    directory = "."  # Replace with the desired directory path
    output_dir = "docs"
    generatedoc(directory, output_dir)
