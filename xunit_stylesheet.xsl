<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="xml" indent="yes"/>

    <!-- /dev/null for these attributes -->
    <xsl:template match="//testcase/@file"/>
    <xsl:template match="//testcase/@line"/>
    <xsl:template match="//testcase/@timestamp"/>

    <!-- copy the rest -->
    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates select="node()|@*"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>