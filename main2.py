from saxonche import *

with PySaxonProcessor(license=False) as saxon_proc:
    xslt30_processor = saxon_proc.new_xslt30_processor()

    element_names = ['foo', 'foobar']

    xslt_param = PyXdmValue()

    for name in element_names:
        xslt_param.add_xdm_item(saxon_proc.make_string_value(name))

    print(xslt_param)
    
    xslt30_processor.set_parameter('cdata-tag-names', xslt_param)

    xslt30_processor.transform_to_file(source_file='sample2.xml', stylesheet_file='serialize-wrap-in-cdata1.xsl', output_file='result-sample2.xml')