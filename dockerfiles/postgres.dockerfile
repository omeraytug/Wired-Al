FROM postgres:16-alpine

EXPOSE 5432

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=5 \
    CMD pg_isready -h 127.0.0.1 -p 5432 || exit 1
