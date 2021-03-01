from graphql.utils import schema_printer

from application.graphql.schemas import schema

fp = open("schemas.graphql", "w")
fp.write(schema_printer.print_schema(schema))
fp.close()
