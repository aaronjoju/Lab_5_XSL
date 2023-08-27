from lxml import etree

# Load XML and XSL files

xml = etree.parse("ecommerce.xml")
xsl = etree.parse("ecommerce.xsl")
xsd = etree.parse("ecommerce.xsd") 


# Apply XSL transformation
transform = etree.XSLT(xsl)
html = transform(xml)
print(html)

# Save transformed HTML to a file
with open('ecommerceparse.html', 'wb') as output_file:
    output_file.write(etree.tostring(html, pretty_print=True))

# Load XSD schema
schema = etree.XMLSchema(xsd)


# Validate transformed HTML against XSD schema
validation_result = schema.validate(html)

if validation_result:
    print("Validation successful!")
else:
    # print("Validation errors:")
    print("Validation Result :",validation_result)
    print(schema.error_log)
