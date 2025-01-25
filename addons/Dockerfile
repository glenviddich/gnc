ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM $BUILD_FROM

# Labels
LABEL maintainer="Glenviddich <dennis.reiss@gmail.com>"
LABEL description="GN Server Add-on"

# Installiere Java
RUN apk add --no-cache openjdk17 curl

# Arbeitsverzeichnis erstellen
WORKDIR /usr/share/gn_server

# Lade die .jar-Datei herunter
RUN curl -o gn_server.jar -L "https://gn.link/jar"

# Startbefehl
CMD ["java", "-jar", "/usr/share/gn_server/gn_server.jar"]
