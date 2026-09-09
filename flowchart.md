# System Flowchart

```text
START
  |
  v
Collect DLP / user-activity records
  |
  v
Validate input
  |
  v
Preprocess data
  |
  v
Extract behavioural/contextual features
  |
  v
Run detection model
  |
  v
Suspicious activity?
  |                 |
 NO                YES
  |                 |
  v                 v
Log normal       Calculate risk
activity             |
  |                  v
  |              Generate alert
  |                  |
  +---------> Store result
                 |
                 v
             Evaluate model
                 |
                 v
                END
```
