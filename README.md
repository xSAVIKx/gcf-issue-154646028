Example for https://issuetracker.google.com/issues/154646028
====

In order to reproduce run:

```bash
gcloud functions deploy <your-function-name> \
    --entry-point=process_request \
    --runtime=python37 \
    --trigger-http \
    --project=<your-project>
```

Such an action results in `docker_layer_cache` error, e.g.:
```
ERROR: (gcloud.functions.deploy) OperationError: code=3, message=Build failed: {"cacheStats": [{"status": "MISS", "hash": "8e51312351ee02e20ebdcdcefb100908ee770a1c81810601ddfcd599221c617b", "type": "docker_layer_cache", "level": "global"}, {"status": "HIT", "hash": "8e51312351ee02e20ebdcdcefb100908ee770a1c81810601ddfcd599221c617b", "type": "docker_layer_cache", "level": "project"}]}
```
