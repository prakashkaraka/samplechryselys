# Sample Pharma Forecasting App

This repository contains a minimal example of a pharma forecasting application.
It uses a simple moving-average approach as a stand in for Prophet and applies a
randomised what-if simulation to demonstrate generative behaviour.

## Structure

- `backend/` – Python package with forecasting and simulation utilities and a
  tiny HTTP server.
- `frontend/` – Static HTML UI.
- `data/` – Synthetic sample sales data.

## Running

From the repository root, run:

```bash
python3 -m backend.server
```

Then open `http://localhost:8000` in a browser.
