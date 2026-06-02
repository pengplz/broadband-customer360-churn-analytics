# Multiplex Bronze Design

## Project

Broadband Customer 360 & Churn Analytics

## Purpose

This document explains the Multiplex Bronze design used in Version 3.

The goal is to use one reusable Auto Loader pattern to ingest multiple source subjects into Bronze Streaming tables.

---

# What Is Multiplex Bronze?

Multiplex Bronze means the ingestion framework can process many sources using one common pattern.

Instead of writing separate ingestion code for every source, the notebook reads a config table:

```text
dev_broadband.monitoring.streaming_source_config