from connect import get_session

yaml_str = open("agent.yaml").read()

# Create session
session = get_session()

session.sql(f"""
CREATE OR REPLACE AGENT agent3
FROM SPECIFICATION
$$
{yaml_str}
$$;
""").collect()