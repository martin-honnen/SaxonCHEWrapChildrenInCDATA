from saxonche import *

with PySaxonProcessor(license=False) as saxon_proc:
    xslt30_processor = saxon_proc.new_xslt30_processor()

    element_names = ['foo', 'foobar']
    xdm_array = saxon_proc.make_array([saxon_proc.make_string_value(name) for name in element_names])

    xpath_processor = saxon_proc.new_xpath_processor()
    xpath_processor.set_context(xdm_item=xdm_array)

    xslt_param = xpath_processor.evaluate('?*')

    print(xslt_param)

    xslt30_processor.set_parameter('cdata-tag-names', xslt_param)

    xslt30_executable = xslt30_processor.compile_stylesheet(stylesheet_file='serialize-wrap-in-cdata1.xsl')

    xslt30_executable.transform_to_file(source_file='sample2.xml', output_file='result-sample2.xml')