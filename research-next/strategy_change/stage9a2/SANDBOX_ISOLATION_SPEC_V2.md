# CODE SANDBOX ISOLATION SPECIFICATION V2

**Date**: August 16, 2026  

---

## 1. PRECISE SANDBOX ISOLATION CONTROLS

1. **Timeout Mechanism**: `SIGKILL` hard process kill at exactly 2.0 seconds.
2. **Network Prohibition**: Socket creation disabled via unconfigured network namespace (`unshare -n`).
3. **Filesystem Isolation**: Isolated temporary directory (`/tmp/sandbox_exec_XXXX`) with read-only root system mounts.
4. **Harness Protection**: Executed in isolated child subprocess (`subprocess.Popen` with unprivileged `nobody` UID); harness memory space strictly isolated.
