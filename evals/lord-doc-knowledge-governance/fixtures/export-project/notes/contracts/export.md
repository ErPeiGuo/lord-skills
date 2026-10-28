# 工单 export contract

Approved: synchronous CSV export with at most 20,000 rows; reject larger requests. The finite limit bounds memory for one request.

An asynchronous queue was rejected because background work is not required. XLSX is a proposal and has not been adopted. Timezone remains unresolved; do not assume UTC.

For observed source behavior and runtime verification, read [evidence](export-evidence.md).
