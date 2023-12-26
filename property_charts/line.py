import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode


def render_basic_line_chart():
    option = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
    }
    st_echarts(
        options=option, height="400px",
    )

ST_LINE_DEMOS = {
    "Line: Basic Line Chart": (
        render_basic_line_chart,
        "https://echarts.apache.org/examples/en/editor.html?c=line-simple",
    ),
}