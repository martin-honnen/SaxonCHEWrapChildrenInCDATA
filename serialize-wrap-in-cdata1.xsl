<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	exclude-result-prefixes="#all"
	expand-text="yes"
	version="3.0">

  <xsl:param name="cdata-tag-names" as="xs:string*" static="yes" select="'tag'"/>

  <xsl:mode on-no-match="shallow-copy"/>

  <xsl:output method="xml" _cdata-section-elements="{$cdata-tag-names}"/>

  <xsl:template _match="{$cdata-tag-names => string-join(' | ')}">
    <xsl:copy>{serialize(node())}</xsl:copy>
  </xsl:template>

</xsl:stylesheet>