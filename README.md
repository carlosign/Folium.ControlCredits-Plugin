# Folium.ControlCredits-Plugin
Leaflet control credits plugin ported to Folium

"A Leaflet control for displaying credits in the corner. Displays an image/logo, and clicking that image/logo will expand to show a brief message with credits and links."
Original leaflet control from https://github.com/GreenInfo-Network/Leaflet-Control-Credits

Example of usage:
```
 from creditosfolium import Creditos
 Creditos(
    imageurl="IMG URL or Base64 IMG URI",
    imagealt="Alt Text",
    tooltip="Equipo",
    width="356px",
    height="80px",
    expandcontent= "Content. Html allowed.",
    ).add_to(m)

```
