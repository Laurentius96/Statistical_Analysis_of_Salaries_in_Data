"""
Interactive dashboard: salaries in data science.
Built with Plotly Dash and Dash Bootstrap Components.

Run from the repository root:  python salary_dashboard.py  (then open http://127.0.0.1:8050)
"""

from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, dcc, html

DATA_PATH = Path(__file__).parent / "data" / "data_science_salaries.csv"
df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df):,} records from {DATA_PATH.name}")

# Numeric columns for the correlation chart
if "experience_level_num" not in df.columns:
    level_map = {"EN": 1, "MI": 2, "SE": 3, "EX": 4}
    df["experience_level_num"] = df["experience_level"].map(level_map)

if "company_size_num" not in df.columns:
    size_map = {"S": 1, "M": 2, "L": 3}
    df["company_size_num"] = df["company_size"].map(size_map)

# Readable labels
experience_labels = {"EN": "Entry", "MI": "Mid", "SE": "Senior", "EX": "Executive"}
size_labels = {"S": "Small", "M": "Medium", "L": "Large"}

df["experience_label"] = df["experience_level"].map(experience_labels)
df["size_label"] = df["company_size"].map(size_labels)


# ============================================================================
# KPIs
# ============================================================================

total_records = len(df)
mean_salary = df["salary_in_usd"].mean()
median_salary = df["salary_in_usd"].median()
total_titles = df["job_title"].nunique()
total_countries = df["employee_residence"].nunique() if "employee_residence" in df.columns else 0

# CAGR of the mean salary
years = sorted(df["work_year"].unique())
if len(years) > 1:
    first_mean = df[df["work_year"] == years[0]]["salary_in_usd"].mean()
    last_mean = df[df["work_year"] == years[-1]]["salary_in_usd"].mean()
    n_years = years[-1] - years[0]
    cagr = ((last_mean / first_mean) ** (1 / n_years) - 1) * 100
else:
    cagr = 0

# ============================================================================
# DASH APP
# ============================================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

app.title = "Data Science Salaries Dashboard"

# ============================================================================
# COLOR PALETTE
# ============================================================================

COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "danger": "#d62728",
    "warning": "#ff9800",
    "info": "#17a2b8",
    "dark": "#2c3e50",
    "light": "#ecf0f1",
    "background": "#f8f9fa",
    "card": "#ffffff"
}

# ============================================================================
# COMPONENTS
# ============================================================================

def create_kpi_card(title, value, icon, color):
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                html.H3(value, style={"color": color, "fontWeight": "bold", "marginBottom": "5px"}),
                html.P(title, style={"color": "#6c757d", "marginBottom": "0", "fontSize": "0.9rem"})
            ], style={"textAlign": "center"})
        ]),
        style={
            "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
            "borderRadius": "10px",
            "border": "none",
            "height": "100%",
            "background": f"linear-gradient(135deg, {color}15 0%, {color}05 100%)"
        }
    )

# ============================================================================
# LAYOUT
# ============================================================================

app.layout = dbc.Container([
    
    # HEADER
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("📊 Data Science Salaries Dashboard", 
                       style={"color": "white", "fontWeight": "bold", "marginBottom": "10px"}),
                html.P("Interactive analysis of salary trends, drivers and correlations (2020–2023)",
                      style={"color": "rgba(255,255,255,0.9)", "fontSize": "1.1rem", "marginBottom": "0"})
            ], style={
                "textAlign": "center",
                "padding": "30px 20px",
                "background": f"linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['info']} 100%)",
                "borderRadius": "10px",
                "marginBottom": "30px"
            })
        ], width=12)
    ]),
    
    # KPI CARDS
    dbc.Row([
        dbc.Col(create_kpi_card("Records", f"{total_records:,}", "database", COLORS["primary"]), 
                width=12, md=6, lg=2, className="mb-3"),
        dbc.Col(create_kpi_card("Mean salary", f"${mean_salary:,.0f}", "dollar-sign", COLORS["success"]), 
                width=12, md=6, lg=2, className="mb-3"),
        dbc.Col(create_kpi_card("Median salary", f"${median_salary:,.0f}", "chart-line", COLORS["info"]), 
                width=12, md=6, lg=2, className="mb-3"),
        dbc.Col(create_kpi_card("CAGR", f"{cagr:+.1f}%", "arrow-trend-up", COLORS["warning"]), 
                width=12, md=6, lg=2, className="mb-3"),
        dbc.Col(create_kpi_card("Job titles", f"{total_titles}", "briefcase", COLORS["secondary"]), 
                width=12, md=6, lg=2, className="mb-3"),
        dbc.Col(create_kpi_card("Countries", f"{total_countries}", "globe", COLORS["danger"]), 
                width=12, md=6, lg=2, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # FILTERS
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🔍 Filters", style={"marginBottom": "20px", "color": COLORS["dark"]}),
                    
                    html.Label("Year:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filter-year",
                        options=[{"label": "All", "value": "all"}] + 
                                [{"label": str(y), "value": y} for y in sorted(df["work_year"].unique())],
                        value="all",
                        clearable=False,
                        style={"marginBottom": "15px"}
                    ),
                    
                    html.Label("Experience level:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filter-level",
                        options=[{"label": "All", "value": "all"}] + 
                                [{"label": experience_labels[exp], "value": exp} 
                                 for exp in sorted(df["experience_level"].unique())],
                        value="all",
                        clearable=False,
                        style={"marginBottom": "15px"}
                    ),
                    
                    html.Label("Company size:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filter-size",
                        options=[{"label": "All", "value": "all"}] + 
                                [{"label": size_labels[size], "value": size} 
                                 for size in sorted(df["company_size"].unique())],
                        value="all",
                        clearable=False,
                        style={"marginBottom": "15px"}
                    ),
                    
                    html.Label("Country of residence:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filter-country",
                        options=[{"label": "All", "value": "all"}] + 
                                [{"label": c, "value": c} 
                                 for c in sorted(df["employee_residence"].unique())],
                        value="all",
                        clearable=False,
                        placeholder="Select a country..."
                    ),
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px", "height": "100%"})
        ], width=12, lg=3, className="mb-3"),
        
        # CHART: salary distribution
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("📊 Salary distribution", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="chart-distribution", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=9, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # CHARTS - ROW 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("📈 Mean salary by year and experience level", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="chart-trend", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("💼 Top 10 best-paid job titles", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    html.P("(Mean salary, job titles with at least 3 records)", 
                           style={"fontSize": "0.85rem", "color": "#6c757d", "marginBottom": "10px"}),
                    dcc.Graph(id="chart-top-titles", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # CHARTS - ROW 2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🔗 Correlation matrix", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="chart-correlation", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🏢 Mean salary by company size", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="chart-company-size", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # FOOTER
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("Built with Plotly Dash · Data: Data Science Salaries (Kaggle), adapted for the DNC School challenge", 
                      style={"marginBottom": "5px", "color": "#6c757d"}),
                html.P("Lorenzo C. Bianchi · github.com/Laurentius96", 
                      style={"marginBottom": "0", "color": "#adb5bd", "fontSize": "0.9rem"})
            ], style={"textAlign": "center", "padding": "20px"})
        ])
    ])
    
], fluid=True, style={"backgroundColor": COLORS["background"], "padding": "20px"})

# ============================================================================
# CALLBACKS
# ============================================================================

@app.callback(
    [
        Output("chart-distribution", "figure"),
        Output("chart-trend", "figure"),
        Output("chart-top-titles", "figure"),
        Output("chart-correlation", "figure"),
        Output("chart-company-size", "figure")
    ],
    [
        Input("filter-year", "value"),
        Input("filter-level", "value"),
        Input("filter-size", "value"),
        Input("filter-country", "value")
    ]
)
def update_graphs(year, level, size, country):
    
    filtered = df.copy()
    
    if year != "all":
        filtered = filtered[filtered["work_year"] == year]
    
    if level != "all":
        filtered = filtered[filtered["experience_level"] == level]
    
    if size != "all":
        filtered = filtered[filtered["company_size"] == size]
    
    if country != "all":
        filtered = filtered[filtered["employee_residence"] == country]
    
    # No data for the selected filters
    if len(filtered) == 0:
        fig_empty = go.Figure()
        fig_empty.add_annotation(
            text="No data for the selected filters",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color="gray")
        )
        fig_empty.update_layout(template="plotly_white", height=300)
        return fig_empty, fig_empty, fig_empty, fig_empty, fig_empty
    
    # CHART 1: salary distribution
    fig_dist = go.Figure()
    
    fig_dist.add_trace(go.Histogram(
        x=filtered["salary_in_usd"],
        nbinsx=20,
        marker_color=COLORS["primary"],
        opacity=0.75,
        name="Records"
    ))
    
    mean_value = filtered["salary_in_usd"].mean()
    median_value = filtered["salary_in_usd"].median()
    
    fig_dist.add_vline(
        x=mean_value,
        line_dash="dash",
        line_color="red",
        line_width=2,
        annotation_text=f"Mean: ${mean_value:,.0f}",
        annotation_position="top right",
        annotation=dict(
            font=dict(size=11, color="red"),
            bgcolor="rgba(255,255,255,0.8)"
        )
    )
    
    fig_dist.add_vline(
        x=median_value,
        line_dash="dash",
        line_color="navy",
        line_width=2,
        annotation_text=f"Median: ${median_value:,.0f}",
        annotation_position="top left",
        annotation=dict(
            font=dict(size=11, color="navy"),
            bgcolor="rgba(255,255,255,0.8)"
        )
    )
    
    fig_dist.update_layout(
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        xaxis_title="Salary (USD)",
        yaxis_title="Records",
        bargap=0.05,
        xaxis=dict(
            tickformat="$,.0f",
            tickmode="linear",
            dtick=50000
        )
    )
    
    # CHART 2: trend by experience level
    trend_data = filtered.groupby(["work_year", "experience_label"])["salary_in_usd"].mean().reset_index()
    fig_temporal = px.line(
        trend_data,
        x="work_year",
        y="salary_in_usd",
        color="experience_label",
        labels={"work_year": "Year", "salary_in_usd": "Mean salary (USD)", "experience_label": "Experience"},
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_temporal.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title="")
    )
    fig_temporal.update_xaxes(dtick=1, tickformat="d")
    
    # CHART 3: top 10 job titles (at least 3 records)
    title_stats = filtered.groupby("job_title").agg({
        "salary_in_usd": ["mean", "count"]
    }).reset_index()
    title_stats.columns = ["job_title", "salary_mean", "count"]
    
    title_stats = title_stats[title_stats["count"] >= 3]
    
    top_titles = title_stats.nlargest(10, "salary_mean").sort_values("salary_mean")
    
    fig_titles = px.bar(
        top_titles,
        x="salary_mean",
        y="job_title",
        orientation="h",
        labels={"salary_mean": "Mean salary (USD)", "job_title": ""},
        color="salary_mean",
        color_continuous_scale="Blues",
        hover_data={"count": True, "salary_mean": ":.2f"}
    )
    fig_titles.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        coloraxis_showscale=False
    )
    
    # CHART 4: correlation matrix
    numeric_cols = ["work_year", "salary_in_usd", "experience_level_num", "company_size_num"]
    available_cols = [col for col in numeric_cols if col in filtered.columns]
    df_corr = filtered[available_cols].corr()
    
    labels_corr = {
        "work_year": "Year",
        "salary_in_usd": "Salary",
        "experience_level_num": "Experience",
        "company_size_num": "Company size"
    }
    
    fig_corr = go.Figure(data=go.Heatmap(
        z=df_corr.values,
        x=[labels_corr.get(col, col) for col in df_corr.columns],
        y=[labels_corr.get(col, col) for col in df_corr.index],
        colorscale="RdBu",
        zmid=0,
        text=np.round(df_corr.values, 2),
        texttemplate="%{text}",
        textfont={"size": 12},
        colorbar=dict(title="r")
    ))
    fig_corr.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    # CHART 5: mean salary by company size
    size_data = filtered.groupby("size_label")["salary_in_usd"].mean().reset_index()
    size_order = {"Small": 1, "Medium": 2, "Large": 3}
    size_data["order"] = size_data["size_label"].map(size_order)
    size_data = size_data.sort_values("order")
    
    fig_size = px.bar(
        size_data,
        x="size_label",
        y="salary_in_usd",
        labels={"size_label": "Company size", "salary_in_usd": "Mean salary (USD)"},
        color="salary_in_usd",
        color_continuous_scale="Greens"
    )
    fig_size.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        coloraxis_showscale=False
    )
    
    return fig_dist, fig_temporal, fig_titles, fig_corr, fig_size

# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8050)
