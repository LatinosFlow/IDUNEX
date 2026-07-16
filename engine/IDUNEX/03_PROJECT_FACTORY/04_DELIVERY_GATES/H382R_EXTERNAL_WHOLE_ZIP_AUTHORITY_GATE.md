# H382R_EXTERNAL_WHOLE_ZIP_AUTHORITY_GATE

El SHA256 integral y los bytes absolutos del ZIP final tienen autoridad externa. Las superficies internas no intentan materializar el hash integral del contenedor que las contiene, porque eso introduce autorreferencia no certificable.

Campos obligatorios en superficies internas:

- WHOLE_ZIP_SHA256_AUTHORITY=EXTERNAL_COMPANION
- WHOLE_ZIP_BYTES_AUTHORITY=EXTERNAL_RELEASE_SURFACE
- TOP_LEVEL_COMPANION_FILE_MATCHES_REOPENED_ZIP=PASS

El finalizer converge sobre entry_count, file_count, directories, stored_count, CRC/testzip, compression policy, duplicate groups, allowlist, ledgers, runtime 10+N y prompt packs A-J.
