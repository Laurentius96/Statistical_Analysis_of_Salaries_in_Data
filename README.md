<div align="center">
  <h1>📊 Statistical Analysis of Salaries in Data Science</h1>
  <p><i>Comprehensive statistical analysis and interactive dashboard for Data Science salary trends worldwide</i></p>
</div>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-objective">Objective</a> •
  <a href="#-technologies-used">Technologies</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-development-methodology">Methodology</a> •
  <a href="#-implemented-features">Features</a> •
  <a href="#-interactive-dashboard">Interactive Dashboard</a> •
  <a href="#-insights-and-results">Insights & Results</a> •
  <a href="#-how-to-use">How to Use</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

## 🔍 Overview

This project presents a complete **statistical analysis** of salaries in the Data Science field, combining exploratory data analysis (EDA) in Jupyter Notebook with an **interactive dashboard** developed in Plotly Dash. The solution enables data-driven insights about salary trends, experience levels, geographic distribution, and market evolution.

<details>
<summary><b>🎯 Problem Solved</b> (Click to expand)</summary>

Understanding salary dynamics in Data Science is crucial for:
- **Professionals**: Career planning and salary negotiation
- **Companies**: Competitive compensation strategies
- **Students**: Career expectations and specialization decisions
- **Recruiters**: Market positioning and talent attraction

This project transforms raw salary data into actionable insights through:
- ✅ Comprehensive statistical analysis
- ✅ Interactive visualizations
- ✅ Temporal trend analysis
- ✅ Geographic and experience-based segmentation

</details>

---

## 🎯 Objective

Develop a complete analytical solution that:

1. **Explores** salary patterns across different dimensions (experience, location, company size)
2. **Identifies** trends and correlations in compensation data
3. **Visualizes** insights through an interactive dashboard
4. **Enables** data-driven decision making for career and business strategies

<details>
<summary><b>Key Questions Answered</b> (Click to expand)</summary>

- 📈 How have salaries evolved over time?
- 🌍 Which countries offer the highest compensation?
- 💼 What are the highest-paid roles in Data Science?
- 🏢 How does company size impact salaries?
- 📊 What correlations exist between experience, location, and compensation?

</details>

---

## 🛠️ Technologies Used

<details>
<summary><b>Data Analysis & Visualization</b> (Click to expand)</summary>

- **Python 3.11+** - Core programming language
- **Pandas 2.1.4** - Data manipulation and analysis
- **NumPy 1.26.2** - Numerical computing
- **Matplotlib 3.8.2** - Static visualizations
- **Seaborn 0.13.0** - Statistical data visualization

</details>

<details>
<summary><b>Interactive Dashboard</b> (Click to expand)</summary>

- **Plotly 5.18.0** - Interactive charts
- **Dash 2.14.2** - Web application framework
- **Dash Bootstrap Components 1.5.0** - Responsive UI components

</details>

<details>
<summary><b>Development Environment</b> (Click to expand)</summary>

- **Jupyter Notebook** - Exploratory data analysis
- **VS Code** - Code editor
- **Git/GitHub** - Version control

</details>

---

## 📁 Project Structure

<details>
<summary><b>View Project Structure</b> (Click to expand)</summary>

```
Statistical_Analysis_of_Salaries_in_Data/
│
├── Data/
│   └── salario_profissionais_dados.csv    # Dataset with salary information
│
├── main.ipynb                              # Exploratory data analysis notebook
│   ├── Data loading and cleaning
│   ├── Descriptive statistics
│   ├── Correlation analysis
│   ├── Temporal trends
│   ├── Geographic analysis
│   └── Statistical visualizations
│
├── dashboard_salarios.py                   # Interactive Dash dashboard
│   ├── Multi-filter system
│   ├── 5 dynamic visualizations
│   ├── KPI cards
│   └── Responsive layout
│
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
└── LICENSE.md                              # CC BY-NC-ND 4.0 License
```

</details>

---

## 🔄 Development Methodology

<details>
<summary><b>1️⃣ Data Understanding & Preparation</b> (Click to expand)</summary>

- **Dataset exploration**: 3,755 records across multiple years
- **Data cleaning**: Handling missing values and outliers
- **Feature engineering**: Creating categorical mappings and numerical encodings

</details>

<details>
<summary><b>2️⃣ Exploratory Data Analysis (EDA)</b> (Click to expand)</summary>

- **Descriptive statistics**: Mean, median, standard deviation, quartiles
- **Distribution analysis**: Salary histograms and density plots
- **Correlation analysis**: Relationships between variables
- **Temporal trends**: Year-over-year salary evolution
- **Segmentation**: Analysis by experience level, company size, and location

</details>

<details>
<summary><b>3️⃣ Interactive Dashboard Development</b> (Click to expand)</summary>

- **Architecture design**: Modular callback structure
- **UI/UX design**: Professional color palette and responsive layout
- **Filter implementation**: Year, experience, company size, and country
- **Visualization optimization**: Performance and readability

</details>

<details>
<summary><b>4️⃣ Insights & Documentation</b> (Click to expand)</summary>

- **Key findings**: Statistical insights and business recommendations
- **Technical documentation**: Code comments and README
- **Reproducibility**: Clear instructions for setup and execution

</details>

---

## ✨ Implemented Features

<details>
<summary><b>📊 Jupyter Notebook Analysis</b> (Click to expand)</summary>

- ✅ **Data profiling**: Complete dataset overview
- ✅ **Statistical summaries**: Descriptive statistics by segments
- ✅ **Correlation matrix**: Heatmap of variable relationships
- ✅ **Distribution plots**: Histograms with mean/median reference lines
- ✅ **Top jobs analysis**: Highest-paid roles with filtering
- ✅ **Temporal trends**: Salary evolution over years
- ✅ **Geographic insights**: Country-level salary comparison

</details>

<details>
<summary><b>🎛️ Interactive Dashboard</b> (Click to expand)</summary>

- ✅ **Multi-filter system**: Year, experience level, company size, country
- ✅ **Real-time updates**: All charts respond to filter changes
- ✅ **6 KPI cards**: Total records, average/median salary, CAGR, unique jobs, countries
- ✅ **5 dynamic visualizations**:
  - 📊 Salary distribution histogram (20 bins with mean/median lines)
  - 📈 Temporal evolution by experience level
  - 💼 Top 10 highest-paid jobs (minimum 3 records filter)
  - 🔗 Correlation matrix heatmap
  - 🏢 Salary by company size
- ✅ **Responsive design**: Bootstrap-based layout for all screen sizes
- ✅ **Professional UI**: Gradient KPI cards and modern color scheme

</details>

---

## 🖥️ Interactive Dashboard

<details>
<summary><b>🔍 Advanced Filtering System</b> (Click to expand)</summary>

```
Filters Available:
├── Year (2020-2024)
├── Experience Level (Entry, Mid, Senior, Executive)
├── Company Size (Small, Medium, Large)
└── Country (50+ countries)
```

</details>

<details>
<summary><b>📊 Visualizations</b> (Click to expand)</summary>

1. **Salary Distribution**
   - 20-bin histogram for optimal granularity
   - Mean and median reference lines
   - Matches notebook analysis standards

2. **Temporal Evolution**
   - Line chart with experience level segmentation
   - Year-over-year trends
   - Interactive hover details

3. **Top 10 Jobs**
   - Horizontal bar chart
   - Filtered by minimum 3 records (outlier protection)
   - Hover shows record count

4. **Correlation Matrix**
   - Heatmap with color scale
   - Variables: Year, Salary, Experience, Company Size
   - Correlation coefficients displayed

5. **Company Size Analysis**
   - Bar chart comparing Small, Medium, Large companies
   - Average salary by segment

</details>

<details>
<summary><b>🎨 UI/UX Highlights</b> (Click to expand)</summary>

- **Color Palette**: Professional blue gradient theme
- **Layout**: Responsive grid system (Bootstrap)
- **Typography**: Clear hierarchy and readability
- **Interactions**: Smooth transitions and hover effects

</details>

---

## 💡 Insights and Results

<details>
<summary><b>📈 Key Findings</b> (Click to expand)</summary>

#### 1. Salary Trends
- **Average Salary**: $137,570 USD
- **Median Salary**: $135,000 USD
- **CAGR**: Positive growth trend (varies by filter)
- **Distribution**: Right-skewed with concentration around median

#### 2. Experience Level Impact
- **Executive**: Highest average compensation
- **Senior**: Strong salary progression
- **Mid-level**: Competitive market positioning
- **Entry**: Growing demand with competitive entry salaries

#### 3. Geographic Insights
- **Top-paying countries**: Analysis reveals geographic salary disparities
- **Remote work impact**: Location flexibility affects compensation
- **Regional trends**: Emerging markets vs. established tech hubs

#### 4. Company Size Correlation
- **Large companies**: Higher average salaries and benefits
- **Medium companies**: Balanced compensation and growth opportunities
- **Small companies**: Competitive for specialized roles

#### 5. Top-Paying Roles
- **Principal Data Scientist**: Premium compensation
- **Director of Data Science**: Leadership premium
- **Specialized roles**: Machine Learning Engineers, Data Architects
- **Emerging roles**: AI/ML specialists commanding high salaries

</details>

<details>
<summary><b>🎯 Business Recommendations</b> (Click to expand)</summary>

**For Professionals:**
- 📚 Invest in advanced skills (ML, AI, Cloud)
- 🌍 Consider geographic mobility for salary optimization
- 📈 Target senior/leadership roles for maximum compensation
- 🔄 Continuous learning to stay competitive

**For Companies:**
- 💰 Benchmark salaries against market data
- 🎯 Competitive compensation for retention
- 📊 Data-driven salary structures
- 🌟 Invest in employee development

</details>

---

## 🚀 How to Use

<details>
<summary><b>Prerequisites</b> (Click to expand)</summary>

- Python 3.11 or higher
- pip (Python package manager)
- Git (for cloning the repository)

</details>

<details>
<summary><b>Installation</b> (Click to expand)</summary>

1. **Clone the repository**
```bash
git clone https://github.com/Laurentius96/Statistical_Analysis_of_Salaries_in_Data.git
cd Statistical_Analysis_of_Salaries_in_Data
```

2. **Create a virtual environment** (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

</details>

<details>
<summary><b>Running the Project</b> (Click to expand)</summary>

#### Option 1: Jupyter Notebook Analysis
```bash
jupyter notebook main.ipynb
```
- Explore the complete statistical analysis
- Run cells sequentially to reproduce results
- Modify parameters for custom analysis

#### Option 2: Interactive Dashboard
```bash
python dashboard_salarios.py
```
- Access the dashboard at: `http://127.0.0.1:8050/`
- Use filters to explore different segments
- Export visualizations as needed

</details>

<details>
<summary><b>📊 Dataset Information</b> (Click to expand)</summary>

**File**: `Data/salario_profissionais_dados.csv`

**Columns**:
- `work_year`: Year of salary data
- `experience_level`: EN (Entry), MI (Mid), SE (Senior), EX (Executive)
- `job_title`: Specific role title
- `salary_in_usd`: Annual salary in USD
- `employee_residence`: Employee's country of residence
- `company_location`: Company's country location
- `company_size`: S (Small), M (Medium), L (Large)
- `country`: Country name
- `region`: Geographic region
- `years_of_experience`: Years of professional experience

</details>

---

## 🤝 Contributing

Contributions are welcome! This project can be enhanced in multiple ways:

<details>
<summary><b>🌟 How to Contribute</b> (Click to expand)</summary>

#### 1. Report Issues
Found a bug or have a suggestion?
- Open an [Issue](https://github.com/Laurentius96/Statistical_Analysis_of_Salaries_in_Data/issues)
- Describe the problem or enhancement clearly
- Include screenshots if applicable

#### 2. Propose New Features
Ideas for improvement:
- 📊 Additional visualizations (scatter plots, box plots, violin plots)
- 🔍 Advanced filtering options (multiple country selection, salary ranges)
- 📈 Predictive models (salary prediction based on features)
- 🌍 Geographic maps (choropleth maps for salary distribution)
- 📱 Mobile-responsive improvements
- 🎨 Dark mode theme
- 📥 Export functionality (PDF reports, CSV data)
- 🔄 Real-time data updates
- 🤖 Machine Learning insights (clustering, classification)

#### 3. Submit Pull Requests

**Step-by-step guide:**

```bash
# 1. Fork the repository (click "Fork" on GitHub)

# 2. Clone your fork
git clone https://github.com/Laurentius96/Statistical_Analysis_of_Salaries_in_Data.git
cd Statistical_Analysis_of_Salaries_in_Data

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes
# - Add new features
# - Fix bugs
# - Improve documentation

# 5. Test your changes
python dashboard_salarios.py  # Test dashboard
jupyter notebook main.ipynb   # Test notebook

# 6. Commit with clear messages
git add .
git commit -m "feat: add new visualization for salary trends"

# 7. Push to your fork
git push origin feature/your-feature-name

# 8. Open a Pull Request on GitHub
# - Describe your changes
# - Reference related issues
# - Include screenshots if applicable
```

#### 4. Improve Documentation
- 📝 Fix typos or clarify instructions
- 🌐 Translate README to other languages
- 📚 Add code comments and docstrings
- 🎓 Create tutorials or guides

</details>

<details>
<summary><b>📋 Contribution Guidelines</b> (Click to expand)</summary>

#### Code Standards
- Follow PEP 8 style guide for Python
- Add comments for complex logic
- Include docstrings for functions
- Test your code before submitting

#### Commit Message Format
Use [Conventional Commits](https://www.conventionalcommits.org/):
```
feat: add new feature
fix: correct bug
docs: update documentation
style: format code
refactor: restructure code
test: add tests
chore: update dependencies
```

#### Pull Request Checklist
- [ ] Code follows project style
- [ ] Tests pass successfully
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

</details>

<details>
<summary><b>🎯 Priority Areas for Contribution</b> (Click to expand)</summary>

1. **Data Analysis Enhancements**
   - Statistical tests (t-tests, ANOVA)
   - Time series forecasting
   - Outlier detection algorithms

2. **Dashboard Improvements**
   - Additional chart types
   - Enhanced interactivity
   - Performance optimization

3. **Machine Learning Integration**
   - Salary prediction models
   - Job role classification
   - Clustering analysis

4. **Documentation**
   - Video tutorials
   - API documentation
   - Use case examples

</details>

---

## 🌍 Community & Support

<details>
<summary><b>💬 Get in Touch</b> (Click to expand)</summary>

- **Issues**: [GitHub Issues](https://github.com/Laurentius96/Statistical_Analysis_of_Salaries_in_Data/issues)
- **Pull Requests**: [Contribute directly](https://github.com/Laurentius96/Statistical_Analysis_of_Salaries_in_Data/pulls)

</details>

<details>
<summary><b>🙏 Acknowledgments</b> (Click to expand)</summary>

- Dataset source: [Kaggle/Data Science Salaries]
- Inspiration: Data Science community
- Contributors: See [CONTRIBUTORS.md](CONTRIBUTORS.md)

</details>

<details>
<summary><b>⭐ Show Your Support</b> (Click to expand)</summary>

If this project helped you, please consider:
- ⭐ Starring the repository
- 🍴 Forking for your own analysis
- 📢 Sharing with the community
- 💬 Providing feedback

</details>

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)**.

<details>
<summary><b>License Summary</b> (Click to expand)</summary>

### You are free to:
- ✅ **Share** — copy and redistribute the material in any medium or format

### Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **NonCommercial** — You may not use the material for commercial purposes
- **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material
- **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits

### Full License
For complete license details, see [LICENSE.md](LICENSE.md) or visit:
- English: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
- Português: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.pt

</details>

---

## 🔗 Related Projects

- [DNC Data Science Repository](https://github.com/Laurentius96/DNC-DataScience)
- [Stock Management System](https://github.com/Laurentius96/Structuring_Company-s_Stock)
- [Colab Preparation Agent](https://github.com/Laurentius96/IA-Colab_Preparation_Agent)

---

<div align="center">
  <p>Made with ❤️ and ☕ by <a href="https://github.com/Laurentius96">Lorenzo C. Bianchi</a></p>
  <p>
    <a href="#top">⬆️ Back to top</a>
  </p>
</div>
