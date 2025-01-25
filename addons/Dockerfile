ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM $BUILD_FROM

# Labels
LABEL maintainer="Denis <dennis.reiss@gmail.com>"
LABEL description="GN Server Add-on"

# Installiere Java
RUN apk add --no-cache openjdk17

# Arbeitsverzeichnis erstellen
WORKDIR /usr/share/gn_server

# Kopiere die JAR-Datei ins Add-on
COPY gn_server.jar /usr/share/gn_server/gn_server.jar

# Startbefehl
CMD ["java", "-jar", "/usr/share/gn_server/gn_server.jar"]
