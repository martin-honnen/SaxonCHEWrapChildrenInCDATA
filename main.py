from saxonche import *

with PySaxonProcessor(license=False) as saxon_proc:
    xslt30_processor = saxon_proc.new_xslt30_processor()

    xslt30_processor.transform_to_file(source_file='sample1.xml', stylesheet_file='serialize-wrap-in-cdata1.xsl', output_file='result-sample1.xml')

