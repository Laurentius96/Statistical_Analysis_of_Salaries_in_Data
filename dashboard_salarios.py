"""
Dashboard Interativo - Análise Salarial em Data Science
Desenvolvido com Plotly Dash
Versão com detecção automática de arquivo
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import os
import glob

# ============================================================================
# CARREGAMENTO E PREPARAÇÃO DOS DADOS (COM DETECÇÃO AUTOMÁTICA)
# ============================================================================

print("\n" + "="*70)
print("🔍 LOCALIZANDO ARQUIVO salaries.csv")
print("="*70)

# Função para encontrar o arquivo
def encontrar_arquivo_csv(nome_arquivo="salaries.csv"):
    """
    Procura o arquivo CSV em múltiplos locais possíveis
    """
    # Lista de caminhos possíveis
    caminhos_possiveis = [
        nome_arquivo,                          # Diretório atual
        f"data/{nome_arquivo}",                # Pasta data
        f"../{nome_arquivo}",                  # Um nível acima
        f"../../{nome_arquivo}",               # Dois níveis acima
        f"datasets/{nome_arquivo}",            # Pasta datasets
        f"../data/{nome_arquivo}",             # data um nível acima
    ]
    
    # Verifica cada caminho
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho):
            caminho_completo = os.path.abspath(caminho)
            print(f"✅ Arquivo encontrado: {caminho}")
            print(f"📁 Caminho completo: {caminho_completo}")
            return caminho
    
    # Se não encontrou, procura recursivamente
    print("\n🔎 Procurando recursivamente...")
    arquivos_encontrados = glob.glob(f"**/{nome_arquivo}", recursive=True)
    
    if arquivos_encontrados:
        caminho = arquivos_encontrados[0]
        caminho_completo = os.path.abspath(caminho)
        print(f"✅ Arquivo encontrado: {caminho}")
        print(f"📁 Caminho completo: {caminho_completo}")
        return caminho
    
    # Se ainda não encontrou, mostra erro detalhado
    print("\n❌ ARQUIVO NÃO ENCONTRADO!")
    print(f"📁 Diretório atual: {os.getcwd()}")
    print("\n📄 Arquivos CSV disponíveis no diretório:")
    
    todos_csv = glob.glob("**/*.csv", recursive=True)
    if todos_csv:
        for i, arquivo in enumerate(todos_csv[:10], 1):  # Mostra até 10
            print(f"   {i}. {arquivo}")
        if len(todos_csv) > 10:
            print(f"   ... e mais {len(todos_csv) - 10} arquivos")
    else:
        print("   (Nenhum arquivo CSV encontrado)")
    
    print("\n💡 SOLUÇÕES:")
    print("   1. Coloque 'salaries.csv' no diretório atual")
    print("   2. Ou digite o caminho completo do arquivo abaixo:")
    
    caminho_manual = input("\n📝 Digite o caminho do arquivo (ou Enter para sair): ").strip()
    
    if caminho_manual and os.path.exists(caminho_manual):
        print(f"✅ Usando: {caminho_manual}")
        return caminho_manual
    
    raise FileNotFoundError(
        f"\n❌ Não foi possível localizar '{nome_arquivo}'.\n"
        f"📁 Diretório atual: {os.getcwd()}\n"
        "💡 Certifique-se de que o arquivo existe e está acessível."
    )

# Carregar o dataset
try:
    caminho_arquivo = encontrar_arquivo_csv("salaries.csv")
    df = pd.read_csv(caminho_arquivo)
    print(f"\n✅ Dataset carregado com sucesso!")
    print(f"📊 Total de registros: {len(df):,}")
    print(f"📋 Colunas: {', '.join(df.columns.tolist())}")
    print("="*70 + "\n")
except Exception as e:
    print(f"\n❌ ERRO ao carregar o dataset: {e}")
    print("\n🛑 O dashboard não pode ser iniciado sem o arquivo de dados.")
    raise

# Criando colunas numéricas para análises
if "experience_level_num" not in df.columns:
    experiencia_map = {"EN": 1, "MI": 2, "SE": 3, "EX": 4}
    df["experience_level_num"] = df["experience_level"].map(experiencia_map)
    print("✅ Coluna 'experience_level_num' criada")

if "company_size_num" not in df.columns:
    tamanho_map = {"S": 1, "M": 2, "L": 3}
    df["company_size_num"] = df["company_size"].map(tamanho_map)
    print("✅ Coluna 'company_size_num' criada")

# Mapeamento de labels legíveis
experience_labels = {"EN": "Entry", "MI": "Mid", "SE": "Senior", "EX": "Executive"}
size_labels = {"S": "Small", "M": "Medium", "L": "Large"}

df["experience_label"] = df["experience_level"].map(experience_labels)
df["size_label"] = df["company_size"].map(size_labels)

print("✅ Preparação dos dados concluída\n")

# ============================================================================
# CÁLCULOS DE KPIs
# ============================================================================

total_registros = len(df)
salario_medio = df["salary_in_usd"].mean()
salario_mediano = df["salary_in_usd"].median()
total_cargos = df["job_title"].nunique()
total_paises = df["employee_residence"].nunique() if "employee_residence" in df.columns else 0

# CAGR (Crescimento Anual Composto)
anos_ordenados = sorted(df["work_year"].unique())
if len(anos_ordenados) > 1:
    salario_inicial = df[df["work_year"] == anos_ordenados[0]]["salary_in_usd"].mean()
    salario_final = df[df["work_year"] == anos_ordenados[-1]]["salary_in_usd"].mean()
    num_anos = anos_ordenados[-1] - anos_ordenados[0]
    cagr = ((salario_final / salario_inicial) ** (1 / num_anos) - 1) * 100
else:
    cagr = 0

# ============================================================================
# CONFIGURAÇÃO DO APP DASH
# ============================================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

app.title = "Dashboard - Salários Data Science"

# ============================================================================
# PALETA DE CORES PROFISSIONAL
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
# COMPONENTES DO DASHBOARD
# ============================================================================

# Cards de KPIs
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
# LAYOUT DO DASHBOARD
# ============================================================================

app.layout = dbc.Container([
    
    # HEADER
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("📊 Dashboard - Análise Salarial em Data Science", 
                       style={
                           "color": "white",
                           "fontWeight": "bold",
                           "marginBottom": "10px"
                       }),
                html.P("Análise interativa de tendências salariais, correlações e insights estratégicos",
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
    
    # KPIs PRINCIPAIS
    dbc.Row([
        dbc.Col(create_kpi_card(
            "Total de Registros",
            f"{total_registros:,}",
            "database",
            COLORS["primary"]
        ), width=12, md=6, lg=2, className="mb-3"),
        
        dbc.Col(create_kpi_card(
            "Salário Médio",
            f"${salario_medio:,.0f}",
            "dollar-sign",
            COLORS["success"]
        ), width=12, md=6, lg=2, className="mb-3"),
        
        dbc.Col(create_kpi_card(
            "Salário Mediano",
            f"${salario_mediano:,.0f}",
            "chart-line",
            COLORS["info"]
        ), width=12, md=6, lg=2, className="mb-3"),
        
        dbc.Col(create_kpi_card(
            "CAGR",
            f"{cagr:+.1f}%",
            "arrow-trend-up",
            COLORS["warning"]
        ), width=12, md=6, lg=2, className="mb-3"),
        
        dbc.Col(create_kpi_card(
            "Cargos Únicos",
            f"{total_cargos}",
            "briefcase",
            COLORS["secondary"]
        ), width=12, md=6, lg=2, className="mb-3"),
        
        dbc.Col(create_kpi_card(
            "Países",
            f"{total_paises}",
            "globe",
            COLORS["danger"]
        ), width=12, md=6, lg=2, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # FILTROS INTERATIVOS
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🔍 Filtros Interativos", style={"marginBottom": "20px", "color": COLORS["dark"]}),
                    
                    html.Label("Ano:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filtro-ano",
                        options=[{"label": "Todos", "value": "all"}] + 
                                [{"label": str(ano), "value": ano} for ano in sorted(df["work_year"].unique())],
                        value="all",
                        clearable=False,
                        style={"marginBottom": "15px"}
                    ),
                    
                    html.Label("Nível de Experiência:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filtro-experiencia",
                        options=[{"label": "Todos", "value": "all"}] + 
                                [{"label": experience_labels[exp], "value": exp} 
                                 for exp in sorted(df["experience_level"].unique())],
                        value="all",
                        clearable=False,
                        style={"marginBottom": "15px"}
                    ),
                    
                    html.Label("Tamanho da Empresa:", style={"fontWeight": "bold", "color": COLORS["dark"]}),
                    dcc.Dropdown(
                        id="filtro-tamanho",
                        options=[{"label": "Todos", "value": "all"}] + 
                                [{"label": size_labels[size], "value": size} 
                                 for size in sorted(df["company_size"].unique())],
                        value="all",
                        clearable=False
                    ),
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px", "height": "100%"})
        ], width=12, lg=3, className="mb-3"),
        
        # GRÁFICO: Distribuição Salarial
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("📊 Distribuição Salarial", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="grafico-distribuicao", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=9, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # GRÁFICOS PRINCIPAIS - LINHA 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("📈 Evolução Temporal por Experiência", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="grafico-temporal", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("💼 Top 10 Cargos Mais Bem Pagos", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="grafico-top-cargos", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # GRÁFICOS PRINCIPAIS - LINHA 2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🔗 Matriz de Correlação", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="grafico-correlacao", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("🏢 Salários por Tamanho de Empresa", style={"marginBottom": "15px", "color": COLORS["dark"]}),
                    dcc.Graph(id="grafico-empresa", config={"displayModeBar": False})
                ])
            ], style={"boxShadow": "0 4px 6px rgba(0,0,0,0.1)", "borderRadius": "10px"})
        ], width=12, lg=6, className="mb-3"),
    ], style={"marginBottom": "30px"}),
    
    # FOOTER
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("Dashboard desenvolvido com Plotly Dash | Análise de Dados em Data Science", 
                      style={"marginBottom": "5px", "color": "#6c757d"}),
                html.P("© 2024 - Projeto de Portfólio", 
                      style={"marginBottom": "0", "color": "#adb5bd", "fontSize": "0.9rem"})
            ], style={"textAlign": "center", "padding": "20px"})
        ])
    ])
    
], fluid=True, style={"backgroundColor": COLORS["background"], "padding": "20px"})

# ============================================================================
# CALLBACKS (INTERATIVIDADE)
# ============================================================================

@app.callback(
    [
        Output("grafico-distribuicao", "figure"),
        Output("grafico-temporal", "figure"),
        Output("grafico-top-cargos", "figure"),
        Output("grafico-correlacao", "figure"),
        Output("grafico-empresa", "figure")
    ],
    [
        Input("filtro-ano", "value"),
        Input("filtro-experiencia", "value"),
        Input("filtro-tamanho", "value")
    ]
)
def update_graphs(ano_selecionado, exp_selecionada, tamanho_selecionado):
    
    # Filtrando dados
    df_filtrado = df.copy()
    
    if ano_selecionado != "all":
        df_filtrado = df_filtrado[df_filtrado["work_year"] == ano_selecionado]
    
    if exp_selecionada != "all":
        df_filtrado = df_filtrado[df_filtrado["experience_level"] == exp_selecionada]
    
    if tamanho_selecionado != "all":
        df_filtrado = df_filtrado[df_filtrado["company_size"] == tamanho_selecionado]
    
    # Verificação de dados vazios
    if len(df_filtrado) == 0:
        # Retorna gráficos vazios com mensagem
        fig_vazio = go.Figure()
        fig_vazio.add_annotation(
            text="Nenhum dado disponível para os filtros selecionados",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color="gray")
        )
        fig_vazio.update_layout(template="plotly_white", height=300)
        return fig_vazio, fig_vazio, fig_vazio, fig_vazio, fig_vazio
    
    # GRÁFICO 1: Distribuição Salarial (Histograma)
    fig_dist = px.histogram(
        df_filtrado,
        x="salary_in_usd",
        nbins=50,
        labels={"salary_in_usd": "Salário (USD)", "count": "Frequência"},
        color_discrete_sequence=[COLORS["primary"]]
    )
    fig_dist.update_layout(
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )
    
    # GRÁFICO 2: Evolução Temporal
    temporal_data = df_filtrado.groupby(["work_year", "experience_label"])["salary_in_usd"].mean().reset_index()
    fig_temporal = px.line(
        temporal_data,
        x="work_year",
        y="salary_in_usd",
        color="experience_label",
        labels={"work_year": "Ano", "salary_in_usd": "Salário Médio (USD)", "experience_label": "Experiência"},
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_temporal.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=""
        )
    )
    
    # GRÁFICO 3: Top 10 Cargos
    top_cargos = df_filtrado.groupby("job_title")["salary_in_usd"].mean().nlargest(10).reset_index()
    top_cargos = top_cargos.sort_values("salary_in_usd")  # Ordenar para melhor visualização
    
    fig_cargos = px.bar(
        top_cargos,
        x="salary_in_usd",
        y="job_title",
        orientation="h",
        labels={"salary_in_usd": "Salário Médio (USD)", "job_title": ""},
        color="salary_in_usd",
        color_continuous_scale="Blues"
    )
    fig_cargos.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        coloraxis_showscale=False
    )
    
    # GRÁFICO 4: Matriz de Correlação
    colunas_numericas = ["work_year", "salary_in_usd", "experience_level_num", "company_size_num"]
    colunas_disponiveis = [col for col in colunas_numericas if col in df_filtrado.columns]
    df_corr = df_filtrado[colunas_disponiveis].corr()
    
    labels_corr = {
        "work_year": "Ano",
        "salary_in_usd": "Salário",
        "experience_level_num": "Experiência",
        "company_size_num": "Tamanho"
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
        colorbar=dict(title="Correlação")
    ))
    fig_corr.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    # GRÁFICO 5: Salários por Tamanho de Empresa
    empresa_data = df_filtrado.groupby("size_label")["salary_in_usd"].mean().reset_index()
    # Ordenar por tamanho lógico
    ordem_tamanho = {"Small": 1, "Medium": 2, "Large": 3}
    empresa_data["ordem"] = empresa_data["size_label"].map(ordem_tamanho)
    empresa_data = empresa_data.sort_values("ordem")
    
    fig_empresa = px.bar(
        empresa_data,
        x="size_label",
        y="salary_in_usd",
        labels={"size_label": "Tamanho da Empresa", "salary_in_usd": "Salário Médio (USD)"},
        color="salary_in_usd",
        color_continuous_scale="Greens"
    )
    fig_empresa.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        coloraxis_showscale=False
    )
    
    return fig_dist, fig_temporal, fig_cargos, fig_corr, fig_empresa

# ============================================================================
# EXECUTAR O APP
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 INICIANDO DASHBOARD INTERATIVO")
    print("="*70)
    print("\n📊 Dashboard disponível em: http://127.0.0.1:8050/")
    print("\n💡 Pressione CTRL+C para encerrar")
    print("="*70 + "\n")
    
    app.run(debug=True, port=8050, host='127.0.0.1')

