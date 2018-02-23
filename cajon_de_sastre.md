# CAJON DE SASTRE
## PARA LUEGO PASAR A LIMPIO

### 2 Reglas TDD
- Escribir código si y solo si, hay un test ya en rojo. (test primero, codigo despues).
- Elimnar duplicación (cuando estés en verde).
- NO USAR CONTROL DE FLUJO!!! (IF), SE HACEN 2 TEST Y LISTO
i

### Primer Kata:

El tema de los Katas, es practicar algo sencillo, tantas veces que se convierte en algo natural (memoria muscular)
- Shohatto (kata de karate) -> String Calculator (Al código)


Fases TDD:
- Preparación
- Ejecución
- Aserción
- TEAR DOWN <<<<--- Dejarlo todo como estaba


## Test de integración:
- Estrechos: Con mocks aka doubles
- Anchos: Prueban partes mas completas, en vez de mock, el repository.

### Dobles:
- Dummy
- Stub (cargas respuesta y la devuelve)
- Spy (Verifica las llamadas)
- Mock (configuras las llamadas y verificas que son llamadas como esperas)


## Test Estrecho:
- Test de contrato:
    - Prueban el sistema al completo, ejemplo, correo electrónico... Se manda un correo y se mira la bandeja de entrada (automaticamente)


## Escuela Detroit o London

## Property Based Testing??!!!


# servicios

- Servicios de Dominio (gestionan las entidades de negocio)
- Servicios de Infraestructura... mailers, mapeadores, reload-rasterisk
- Servicios de Aplicación (actions)

    EJEMPLO:

    http -> habla con el servicio de aplicación (acciones) -> entran al dominio -> estructura


# Respecto a MOCS:

- Necesito doblar un objeto que no puedo reemplazar
- Los logs son una funcionalidad
- Doblar clases concretas
- No se doblan valores

