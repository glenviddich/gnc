# GNC Server Integration für Home Assistant

Diese Integration ermöglicht es dir, den `gn_server.jar` direkt von Home Assistant aus zu starten und zu stoppen. Du kannst die Ports dynamisch über die Home Assistant Benutzeroberfläche konfigurieren.

## Installation

1. Klone dieses Repository in deinen Home Assistant `custom_components` Ordner:
    ```bash
    git clone https://github.com/YOUR_USERNAME/gnc.git /config/custom_components/gnc
    ```

2. Starte Home Assistant neu.

3. Konfiguriere die Ports für den `gn_server.jar` Server über die Home Assistant UI.

## Dienste

Die Integration stellt zwei Dienste zur Verfügung:

- **gnc.start_server**: Startet den `gn_server.jar` mit den angegebenen Ports.
- **gnc.stop_server**: Stoppt alle laufenden Instanzen des Servers.

## Nutzung über die Home Assistant UI

### 1. Konfiguration der Ports:

Die Konfiguration der Ports erfolgt direkt über die Home Assistant Benutzeroberfläche. Nachdem die Integration hinzugefügt wurde, kannst du die Ports für den Server konfigurieren.

### 2. Server starten:

Du kannst den Server starten, indem du den **gnc.start_server** Dienst über die Home Assistant Entwicklerwerkzeuge oder Automationen aufrufst und dabei die gewünschten Ports angibst.

Beispiel-Aufruf über die Entwicklerwerkzeuge:

- **Service**: `gnc.start_server`
- **Daten**:
    ```yaml
    ports:
      - 6990
      - 6991
      - 6992
    ```

### 3. Server stoppen:

Den Server kannst du über den **gnc.stop_server** Dienst stoppen.

Beispiel-Aufruf über die Entwicklerwerkzeuge:

- **Service**: `gnc.stop_server`

### 4. Automationen:

Du kannst den Server automatisch zu bestimmten Zeiten starten und stoppen.

Beispiel für eine **Start-Automation**:

```yaml
alias: "Starte GNC Server"
trigger:
  - platform: time
    at: "07:00:00"  # Beispiel: Starten um 7:00 Uhr
action:
  - service: gnc.start_server
    data:
      ports:
        - 6990
        - 6991
        - 6992
