# Running DataGen Python Scripts in AWS

This document outlines how to incorporate the DataGen Python scripts into an AWS environment so a mobile app (e.g. React PWA) can launch scripts, display data, and show status.

---

## Running Python on AWS – Main Options

| Option | Best for | Limits / tradeoffs |
|--------|----------|---------------------|
| **Lambda** | Short, event-driven runs (e.g. “run this script” via API). | 15 min max, limited /tmp, 10 GB memory. Good if a single DataGen run fits in time/memory. |
| **Lambda + Step Functions** | Multi-step pipeline (e.g. 1310 → 1320 → 1330 → …). | Each step can be a Lambda; orchestration and retries built-in. |
| **Fargate / ECS (container)** | Long-running or heavy runs, or a small “runner” API. | No 15 min limit; you manage scaling and cost. |
| **EC2** | Full control, existing file-based scripts with minimal change. | You manage OS, scaling, and uptime. |
| **AWS Batch** | “Submit job, get result later” with no timeout concern. | Job queue + compute; app polls or uses SNS for completion. |

“Run Python dynamically” in AWS usually means: **trigger execution from an API or event (e.g. from your mobile app), and optionally get back status and data**. All of the above can do that; the difference is **how long** the run is and **how much** you want to change the current file-based scripts.

---

## Recommended Pattern for Your Use Case

**Goal:** A page in the mobile app that can **launch** DataGen scripts, **show status**, and **display data**.

### 1. API layer the app can call

- **API Gateway + Lambda**
  - One Lambda (or several) that:
    - **Start run:** receives a request from the app, starts the DataGen run (see below), returns a `runId` or `jobId`.
    - **Status:** `GET /runs/{runId}/status` (or `/jobs/{jobId}`) returns current status (e.g. “running”, “step 1320”, “completed”, “failed”).
    - **Data:** `GET /runs/{runId}/results` (or similar) returns summary or links to generated data (e.g. S3 presigned URLs for CSVs).
- Alternatively, put a small **Flask/FastAPI app** on **EC2 or Fargate** that does the same: “start run”, “status”, “data”. The app just calls this API.

So: **one backend (Lambda + optional Step Functions, or one container) that exposes “launch”, “status”, “data”** is the right place to “incorporate” the datagen scripts.

### 2. Where Python actually runs

- **If each DataGen run is under ~15 minutes and fits in Lambda’s memory/disk:**
  - Use **Lambda** to run the Python pipeline (e.g. one Lambda that runs the main DataGen entry script, or Step Functions that call a Lambda per step).
  - “Run Python dynamically” = mobile app calls API → API invokes Lambda (or Step Functions) → Lambda runs your scripts.

- **If runs are long or need a lot of disk/memory:**
  - Use **Fargate** or **EC2** and run a small **runner service** (e.g. FastAPI) that:
    - Receives “start run” from the app.
    - Runs the DataGen scripts in a subprocess or as a background task (e.g. `subprocess.run(["python", "DataGen_1012_Main_DataGen_Delta.py"])` or equivalent).
    - Writes status to DynamoDB/S3/DB or in-memory store; “status” and “data” endpoints read from there.

- **If you prefer a job queue:**
  - **AWS Batch** (or SQS + Lambda/Fargate): app calls API → API submits a Batch job (or pushes to SQS) that runs your Python; status is tracked by Batch or your own table; “data” endpoint returns links to outputs (e.g. S3).

So the “best” way to run Python dynamically in AWS for you is: **behind an API that your mobile app calls**, with execution in **Lambda** (short runs) or **Fargate/EC2** (long/heavy runs).

---

## Fitting Your DataGen Scripts In

Your scripts are **file-based** (config, `data_results`, merged files, etc.). To use them on AWS you either:

- **Option A – Minimal change:**
  - Run the same Python in **EC2 or Fargate** with a **filesystem** (instance storage or **EFS**).
  - Config and paths stay as today; the “runner” service (or a Lambda that invokes the same code in a container) runs the scripts and reports status (e.g. by parsing log output or writing a small status file/DB).

- **Option B – More AWS-native:**
  - Store config in **S3** (or SSM Parameter Store); inputs/outputs in **S3**.
  - Adapt scripts (or a thin wrapper) to read/write S3 instead of (or in addition to) local paths.
  - Then you can run the same logic from **Lambda** (if run is short) or **Fargate/Batch** with an S3-backed filesystem or direct S3 access.

So yes: you can **incorporate these datagen Python scripts into an AWS server (or serverless)** so that a page in the mobile app can **launch** them, **see status**, and **display data**, by:

1. Exposing **“launch”, “status”, “data”** via an API (API Gateway + Lambda, or a Flask/FastAPI on EC2/Fargate).
2. Running the Python **dynamically** in response to that API using **Lambda** (short runs) or **Fargate/EC2/Batch** (long runs).
3. Having the app call that API and, for data, either get JSON from the API or presigned S3 URLs to download CSVs/reports.

If a typical DataGen run is under ~15 minutes, Lambda (or Step Functions + Lambda) is a good fit; if it’s longer or needs more disk, use Fargate or EC2 with a small runner service and EFS (or S3) for config and outputs. **DataGen_1410**, **DataGen_1420**, **DataGen_1430**, and **DataGen_1440** (REST clients to Oracle Fusion for items, customers, customer-sites, and organizations) are typically short-running and can be exposed as API actions (e.g. “Acquire items from Fusion", "Acquire customers from Fusion”).
