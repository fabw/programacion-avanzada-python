# README

## 1. ¿Qué diferencia notaste entre `write()` y `append()`?

La diferencia principal es que `write()` en modo `"w"` escribe el contenido desde cero y reemplaza lo que había antes en el archivo. En cambio, `append()` en modo `"a"` agrega nueva información al final sin borrar el contenido existente.

## 2. ¿Qué ventaja tiene usar `with open(...)` frente a abrir y cerrar manualmente?

La principal ventaja de usar `with open(...)` es que el archivo se cierra automáticamente al terminar el bloque, incluso si ocurre un error. Esto hace el código más seguro, más limpio y más fácil de mantener.
