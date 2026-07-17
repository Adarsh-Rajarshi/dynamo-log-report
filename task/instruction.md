# Access Log Report

An Apache-style access log is located at `/app/access.log` in your working directory.
Parse it and write a JSON report to `/app/report.json`.

The report must be a single JSON object with exactly these three keys:

- `total_requests` (integer) — the number of request lines in the log. Ignore blank lines.
- `unique_ips` (integer) — the number of distinct client IP addresses. The client IP is the
  first whitespace-separated field on each line.
- `top_path` (string) — the request path that appears most often. The path is the second
  token inside the quoted request, i.e. the `<path>` in `"<METHOD> <path> <PROTOCOL>"`.

Example line and how to read it:

```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

Here the client IP is `192.168.0.1`, the method is `GET`, and the path is `/index.html`.

## Success criteria

1. A file `/app/report.json` exists and contains a single valid JSON object.
2. `total_requests` equals the exact number of request lines in `/app/access.log`.
3. `unique_ips` equals the exact number of distinct client IP addresses.
4. `top_path` equals the most frequently requested path (ties broken by first occurrence).
