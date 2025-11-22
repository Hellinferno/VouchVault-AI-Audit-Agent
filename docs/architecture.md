```mermaid
graph TD
    User[User / CLI] -->|Input| Manager[Manager Agent]
    Manager -->|Delegates| Analyst[Analyst Agent]
    Analyst -->|Uses| TaxTool[Tool: Tax Compliance]
    Analyst -->|Uses| MatchTool[Tool: Vendor Matching]
    TaxTool --> Analyst
    MatchTool --> Analyst
    Analyst -->|Report| Manager
    Manager -->|Result| Output[Audit Report]
```
