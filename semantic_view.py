from connect import get_session

yaml_str = open("semantic.yaml", encoding='utf-8').read()

# print(yaml_str)

# Create session
session = get_session()

session.sql(f"""
CALL SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML(
'insurance.operations',
$$
{yaml_str}
$$
)
""").collect()