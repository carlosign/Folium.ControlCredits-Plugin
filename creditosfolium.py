#Original plugin for Leaflet by GreenInfo-Network
#Port to folium by Carlos Charletti
from branca.element import MacroElement
from jinja2 import Template

from folium.elements import JSCSSMixin
from folium.utilities import parse_options


class Creditos(JSCSSMixin, MacroElement):
 

    _template = Template(
        """
        {% macro script(this, kwargs) %}
            L.controlCredits(
                {{ this.options|tojson }}
            ).addTo({{this._parent.get_name()}});
        {% endmacro %}
        """
    )  # noqa

    default_js = [
        (
            "leaflet-control-credits.js",
            "https://cdn.jsdelivr.net/gh/carlosign/Folium.ControlCredits-Plugin@main/js/leaflet-control-credits.js",
        )
    ]
    default_css = [
        (
            "leaflet-control-credits.css",
            "https://cdn.jsdelivr.net/gh/carlosign/Folium.ControlCredits-Plugin@main/js/leaflet-control-credits.css",
        )
    ]

    def __init__(
        self,
        imageurl="",
        imagealt="",
        tooltip="",
        width="45px",
        height="45px",
        expandcontent= "",
        **kwargs
    ):
        super().__init__()
        self._name = "Creditos"
        self.options = parse_options(
            imageurl=imageurl,
            imagealt=imagealt,
            tooltip=tooltip,
            width=width,
            height=height,
            expandcontent=expandcontent,
            **kwargs
        )
