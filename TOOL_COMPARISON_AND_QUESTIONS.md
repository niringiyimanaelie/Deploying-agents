# Cortex Search vs Cortex Analyst: When to Use Which Tool

## Overview

Your Snowflake Platform Health & Governance solution uses **two complementary AI tools** that work together to provide comprehensive analytics:

1. **Cortex Search Service** - Semantic search for finding specific queries
2. **Cortex Analyst** - Structured data analysis for metrics and aggregations

## Why Both Tools?

### The Problem They Solve Together

**Imagine you're investigating a performance issue:**
- **"What queries are causing memory spills in our data warehouse?"** ← This needs BOTH tools
  - **Search** finds the actual SQL queries with memory spill patterns
  - **Analyst** calculates how many queries, how much memory spilled, cost impact

**Or investigating costs:**
- **"Show me expensive ETL queries that failed last week"**
  - **Search** finds queries matching "ETL", "data pipeline", "transform" in SQL text
  - **Analyst** aggregates costs, filters by execution status, calculates trends

### Core Capabilities

| Capability | Cortex Search | Cortex Analyst | Why You Need Both |
|------------|---------------|----------------|-------------------|
| **Find specific SQL** | ✅ Best | ❌ Cannot | Search understands query content |
| **Calculate metrics** | ❌ Cannot | ✅ Best | Analyst does math & aggregations |
| **Semantic understanding** | ✅ "ETL" finds "MERGE INTO", "INSERT" | ❌ Exact matches only | Search understands SQL patterns |
| **Cost analysis** | ❌ Limited | ✅ Best | Analyst joins cost attribution data |
| **Trend analysis** | ❌ No time-series | ✅ Best | Analyst calculates trends, percentages |
| **Error investigation** | ✅ Finds error messages | ✅ Counts/groups errors | Different angles on same problem |

---

## 🔍 Cortex Search Service - "Find the Needle in the Haystack"

### What It Does
Semantic search over SQL query text and metadata. Understands **business context and SQL patterns**, not just exact keyword matches.

### Best For
- Finding specific queries by **business meaning** (not just SQL syntax)
- Investigating error messages and failure patterns
- Discovering queries that access specific tables/databases
- Finding similar queries across users/time periods
- Exploratory investigation when you don't know exact SQL

### How It Works
- Indexes: `QUERY_TEXT`, `ERROR_MESSAGE`, `QUERY_SUMMARY`, `SEARCH_METADATA`
- Returns: Actual query records with full SQL text
- Semantic matching: "ETL" finds "MERGE INTO", "INSERT", "data transformation"

---

## 📊 Cortex Analyst - "Crunch the Numbers"

### What It Does
Structured analytics over **12 ACCOUNT_USAGE tables** with semantic understanding of business metrics, costs, and governance data.

### Best For
- **Cost analysis**: Who spent what, warehouse costs, query attribution
- **Performance metrics**: Aggregations, averages, trends
- **Governance reporting**: User activity, role usage, policy compliance
- **Trend analysis**: Month-over-month, daily patterns, growth rates
- **Quantitative answers**: "How many?", "How much?", "What's the average?"

### How It Works
- Semantic model describes 12 tables, 300+ columns
- Generates SQL for aggregations, joins, filters
- Returns: Metrics, counts, sums, percentages

---

## 🎯 Decision Matrix: Which Tool to Use?

### Use **Cortex Search** When...
✅ Question contains: **"Find queries that..."**, **"Show me SQL for..."**, **"What queries..."**
✅ Looking for specific SQL patterns or business logic
✅ Investigating error messages or failure text
✅ Need to see actual query text/code
✅ Exploring without knowing exact criteria

**Examples:**
- "Find queries that join CUSTOMERS and ORDERS tables"
- "Show me SQL with subqueries on the sales database"
- "What queries are failing with timeout errors?"
- "Find data pipeline transformation queries"

---

### Use **Cortex Analyst** When...
✅ Question contains: **"How many..."**, **"What's the cost..."**, **"Show me trends..."**, **"Calculate..."**
✅ Need metrics, aggregations, statistics
✅ Analyzing costs, credits, or resource usage
✅ Want to know **who, when, how much** (not the SQL itself)
✅ Need time-based trends or comparisons

**Examples:**
- "How many queries ran yesterday?"
- "What's the total cost by warehouse this month?"
- "Show me average query execution time by user"
- "Which database has the most activity?"

---

### Use **BOTH Tools Together** When...
✅ Question has **both qualitative and quantitative aspects**
✅ Need to find specific queries AND calculate their impact
✅ Investigating issues that require context + metrics

**Examples:**
- "Find expensive ETL queries and calculate their total cost" 
  - Search: Find ETL pattern queries
  - Analyst: Sum costs for those query IDs
  
- "Show me queries with memory spills and their performance impact"
  - Search: Find queries with spill patterns
  - Analyst: Calculate total spilled bytes, execution times

- "What failed queries are costing us the most?"
  - Search: Find queries with specific error patterns
  - Analyst: Aggregate costs for failed queries

---

## 📝 Sample Questions by Category

## Category 1: 🔍 CORTEX SEARCH ONLY
*Finding specific queries by content, pattern, or business logic*

### Finding SQL by Business Logic
1. "Find queries that join the ORDERS and CUSTOMERS tables"
2. "Show me SQL that contains MERGE statements"
3. "Find queries performing full table scans on large tables"
4. "What queries are using window functions like ROW_NUMBER?"
5. "Show me queries with CTEs (WITH clauses) in the sales database"
6. "Find queries that use COPY INTO for data loading"
7. "Show me SQL with subqueries accessing the products table"
8. "Find queries that create or refresh dynamic tables"
9. "What queries are using external functions?"
10. "Show me queries with UNION or UNION ALL operations"

### Error & Failure Investigation
11. "Find queries that failed with 'compilation error'"
12. "Show me SQL that timed out in the last 24 hours"
13. "Find queries with 'object does not exist' errors"
14. "What queries failed due to insufficient privileges?"
15. "Show me queries that hit warehouse resource limits"
16. "Find SQL with syntax errors in the WHERE clause"
17. "What queries failed due to lock timeout?"
18. "Show me queries that encountered memory errors"

### Data Pipeline & ETL Queries
19. "Find ETL transformation queries in the staging database"
20. "Show me data loading queries using COPY command"
21. "Find queries that truncate and reload tables"
22. "What queries are part of our nightly batch jobs?"
23. "Show me queries tagged as 'data pipeline' or 'scheduled'"
24. "Find queries that write to the analytics database"
25. "Show me SQL for incremental data loads"

### Performance Pattern Searches
26. "Find queries with large table scans (no WHERE clause)"
27. "Show me queries that spill data to disk"
28. "Find queries with poor filter selectivity"
29. "What queries scan more than 1TB of data?"
30. "Show me queries using expensive aggregations"
31. "Find queries with Cartesian joins"
32. "What queries bypass the result cache?"

### User & Role Activity
33. "Find queries run by specific role ACCOUNTADMIN"
34. "Show me queries from user John tagged as 'exploratory'"
35. "Find queries run by service accounts"
36. "What queries are users running on production data?"

---

## Category 2: 📊 CORTEX ANALYST ONLY
*Calculating metrics, costs, trends, and aggregations*

### Cost Analysis & Attribution
1. "What's the total credit consumption by warehouse this month?"
2. "Show me the top 10 most expensive queries by cost"
3. "Calculate per-user query costs for the last 30 days"
4. "What's our warehouse idle time cost vs compute cost?"
5. "Show me query acceleration spend trends month-over-month"
6. "What's the average cost per query by warehouse size?"
7. "Calculate total serverless credits used this quarter"
8. "Show me cost efficiency: compute credits per GB scanned"
9. "What warehouses have the highest cost per hour?"
10. "Calculate our cloud services credit consumption rate"

### Performance Metrics & Trends
11. "What's the average query execution time by warehouse?"
12. "Show me cache hit rate percentage over the last week"
13. "Calculate the percentage of queries that queue"
14. "What's the trend in query throughput per hour?"
15. "Show me average compilation time by query type"
16. "Calculate median bytes scanned per query"
17. "What's our query failure rate by day?"
18. "Show me warehouse utilization percentage hourly"

### Governance & Security Metrics
19. "How many users are active per role?"
20. "What's our MFA adoption rate across all users?"
21. "Show me login activity by user type (PERSON vs SERVICE)"
22. "Calculate the number of databases with row access policies"
23. "What percentage of tables have data retention policies?"
24. "Show me privileged role usage frequency"
25. "How many views are configured as secure views?"
26. "Calculate role assignment changes this month"

### Resource Utilization
27. "What's the total number of queries by database?"
28. "Show me warehouse credit usage distribution"
29. "Calculate average bytes spilled per warehouse"
30. "What's the total data scanned across all queries today?"
31. "Show me the number of tables created vs dropped this week"
32. "Calculate storage usage by database"

### User Activity & Patterns
33. "How many queries did each user run yesterday?"
34. "What's the average number of queries per user per day?"
35. "Show me top 5 most active users by query count"
36. "Calculate query volume by hour of day (peak hours)"
37. "What users haven't logged in for 90 days?"
38. "Show me query count by user type and role"

### Operational Health
39. "What's the percentage of failed queries vs successful?"
40. "Show me the number of queries with optimization insights"
41. "Calculate average queue wait time by warehouse"
42. "What's the count of queries using Query Acceleration Service?"
43. "Show me the number of long-running queries (>5 minutes)"
44. "Calculate warehouse provisioning delay frequency"

### Time-Based Analysis
45. "Show me daily credit consumption trends for the past month"
46. "What's the week-over-week growth in query volume?"
47. "Calculate peak usage hours by warehouse"
48. "Show me weekend vs weekday query patterns"
49. "What's the month-over-month change in average query cost?"
50. "Calculate query volume by day of week"

---

## Category 3: 🔍📊 BOTH TOOLS TOGETHER
*Questions requiring both semantic search AND quantitative analysis*

### Cost Optimization Investigations
1. **"Find expensive ETL queries and calculate their total monthly cost"**
   - **Search:** Find queries matching ETL patterns (MERGE, INSERT, COPY)
   - **Analyst:** Sum CREDITS_ATTRIBUTED_COMPUTE for those query IDs
   
2. **"Show me queries with memory spills and calculate the performance impact"**
   - **Search:** Find queries with spill patterns in SQL text
   - **Analyst:** Calculate total BYTES_SPILLED, avg execution time
   
3. **"Find queries on the SALES database and show cost trends by user"**
   - **Search:** Find queries accessing SALES database tables
   - **Analyst:** Group costs by user, calculate trends

4. **"What failed queries cost us the most last week?"**
   - **Search:** Find queries with failure errors
   - **Analyst:** Sum credits, group by error type

5. **"Find full table scan queries and calculate their cost vs optimized queries"**
   - **Search:** Find queries without WHERE clauses
   - **Analyst:** Compare avg cost to queries with good filters

### Performance Troubleshooting
6. **"Find queries that timeout and analyze their common patterns"**
   - **Search:** Find timeout error messages
   - **Analyst:** Count by user, warehouse, time of day

7. **"Show me queries with poor cache utilization and their performance metrics"**
   - **Search:** Find queries with cache miss patterns
   - **Analyst:** Calculate avg cache hit %, execution time, bytes scanned

8. **"Find queries with Cartesian joins and calculate their resource consumption"**
   - **Search:** Find CROSS JOIN patterns in SQL
   - **Analyst:** Sum bytes scanned, execution time, credits used

9. **"What queries are causing warehouse queuing issues?"**
   - **Search:** Find long-running query patterns
   - **Analyst:** Calculate avg queue wait time, identify peak hours

10. **"Find queries on large tables without clustering keys"**
    - **Search:** Find full scan patterns on specific tables
    - **Analyst:** Calculate scan efficiency, cost per GB

### Governance & Compliance
11. **"Find queries accessing PII data and track user access patterns"**
    - **Search:** Find queries accessing customer/user tables
    - **Analyst:** Count by user, role, calculate access frequency

12. **"Show me admin role queries and their activity trends"**
    - **Search:** Find queries run by ACCOUNTADMIN/SECURITYADMIN
    - **Analyst:** Group by user, calculate daily activity trends

13. **"Find queries modifying production tables and calculate data change volume"**
    - **Search:** Find INSERT/UPDATE/DELETE/MERGE in prod database
    - **Analyst:** Sum BYTES_WRITTEN, ROWS_INSERTED/UPDATED/DELETED

14. **"What queries are bypassing row access policies?"**
    - **Search:** Find queries with policy-exempt patterns
    - **Analyst:** Count violations by user, calculate compliance rate

### Operational Intelligence
15. **"Find scheduled job queries and analyze their reliability"**
    - **Search:** Find queries tagged as scheduled/batch jobs
    - **Analyst:** Calculate success rate, avg runtime, cost per job

16. **"Show me queries from BI tools and their impact on warehouse performance"**
    - **Search:** Find queries from Tableau/PowerBI (via QUERY_TAG)
    - **Analyst:** Calculate warehouse load, avg query time, credits used

17. **"Find queries using external functions and calculate their cost efficiency"**
    - **Search:** Find external function calls in SQL
    - **Analyst:** Sum external function bytes sent/received, calculate cost

18. **"What development queries are running in production?"**
    - **Search:** Find ad-hoc/exploratory query patterns
    - **Analyst:** Count by user, calculate resource consumption

### Capacity Planning
19. **"Find peak hour queries and predict warehouse sizing needs"**
    - **Search:** Identify heavy query patterns during peak
    - **Analyst:** Calculate query volume, avg concurrency, resource usage trends

20. **"Show me queries by department and calculate fair chargeback allocation"**
    - **Search:** Find queries by department tags/roles
    - **Analyst:** Sum credits per department, calculate percentages

---

## 🎯 Pro Tips for Using Both Tools

### 1. **Start with Search, Finish with Analyst**
**Workflow:**
```
User: "Find expensive data pipeline queries"
↓
Agent: [Search] → Finds ETL/pipeline queries
Agent: [Analyst] → Calculates costs for those queries
↓
Response: "Found 47 ETL queries. Total cost: 234.56 credits. Top 3..."
```

### 2. **Use Search for "What", Analyst for "How Much"**
- Search: **WHAT** queries match my criteria?
- Analyst: **HOW MUCH** did they cost/scan/run?

### 3. **Iterate and Refine**
```
1. Search → Get query IDs that match pattern
2. Analyst → Calculate metrics for those IDs
3. Search → Drill into specific high-cost queries
4. Analyst → Compare trends over time
```

### 4. **Combine for Root Cause Analysis**
- **Symptom** (Analyst): "Warehouse costs up 40% this week"
- **Investigation** (Search): "Find new or changed queries"
- **Impact** (Analyst): "Calculate cost delta by query"
- **Solution** (Search): "Identify optimization opportunities"

---

## 🚀 Quick Reference Card

| Your Question Contains... | Use This Tool |
|---------------------------|---------------|
| "Find queries...", "Show SQL..." | **Search** |
| "How many...", "What's the cost...", "Calculate..." | **Analyst** |
| "Find expensive..." | **BOTH** (Search finds, Analyst calculates) |
| "Show me trends...", "Average...", "Total..." | **Analyst** |
| "What queries with [pattern]..." | **Search** |
| "Which users...", "By warehouse..." | **Analyst** |
| SQL keywords (JOIN, MERGE, SELECT) | **Search** |
| Numbers, metrics, percentages | **Analyst** |
| Error messages, failure text | **Search** |
| Cost optimization, performance tuning | **BOTH** |

---

## Summary

**Cortex Search = Your Detective** 🔍
- Finds the needle in the haystack
- Understands business context
- Shows you the actual SQL

**Cortex Analyst = Your Data Scientist** 📊
- Crunches the numbers
- Calculates trends and metrics
- Answers "how much" questions

**Together = Complete Platform Intelligence** 🎯
- Search finds the problems
- Analyst quantifies the impact
- You get actionable insights

Use them together for comprehensive Snowflake platform management!
