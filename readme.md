# TensorFlow Repository AI Analyzer

## Overview
An automated AI-powered tool that analyzes TensorFlow's GitHub repository to provide architectural insights, code quality metrics, and development patterns. The tool leverages OpenAI's GPT-3.5 to perform deep-learning framework analysis and generate actionable insights.

## Key Features
- 🤖 AI-powered code analysis using OpenAI GPT-3.5
- 📊 Repository metrics tracking (stars, forks, issues)
- 📝 Automated architectural insights generation
- 📈 CSV export for trend analysis
- 📋 Detailed logging system

## Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/tensorflow-analyzer
cd tensorflow-analyzer

# Install dependencies
pip install -r requirements.txt

# Replace API tokens in main.py
# GITHUB_TOKEN = "your_github_token"
# OPENAI_API_KEY = "your_openai_api_key"

# Run the analyzer
python main.py
```

## Output Files
- `tensorflow_analysis.csv`: Repository metrics and key insights
- `tensorflow_analysis.txt`: Detailed logs and analysis history

## Sample Output
```
=== Analysis Results ===

Repository: tensorflow/tensorflow

Metrics:
stars: 178234
forks: 89123
open_issues: 2341
created_at: 2015-11-07T01:19:20Z
last_updated: 2024-11-06T15:30:45Z

AI Insights:
- Modular architecture with clear separation of concerns
- Extensive use of Python C++ bindings for performance
- Comprehensive error handling and input validation
```

## Requirements
- Python 3.8+
- OpenAI API key
- GitHub personal access token
- Required packages:
  - openai>=1.0.0
  - requests>=2.28.0
  - pandas>=1.3.0

## Getting API Keys
1. GitHub Token:
   - Go to https://github.com/settings/tokens
   - Generate new token with 'repo' access
   - Copy token to `GITHUB_TOKEN` in main.py

2. OpenAI API Key:
   - Visit https://platform.openai.com/api-keys
   - Create new API key
   - Copy key to `OPENAI_API_KEY` in main.py

## Features in Detail

### Repository Metrics
- Star count
- Fork count
- Open issues
- Creation date
- Last update time

### AI Analysis
- Code architecture review
- Quality assessment
- Best practices evaluation
- Improvement suggestions

### Data Export
- CSV format for metrics
- Timestamped entries
- Historical tracking

## Use Cases
- Deep learning framework analysis
- Architecture review
- Code quality monitoring
- Development pattern analysis
- Technical documentation generation

## Limitations
- API rate limits apply
- Analysis limited to public repositories
- Sample size limited to key files

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
MIT License - feel free to use this tool for any purpose

## Acknowledgments
- TensorFlow team for maintaining an open-source deep learning framework
- OpenAI for providing the GPT-3.5 API
- GitHub for their comprehensive API

## Contact
Your Name - your.email@example.com
Project Link: https://github.com/yourusername/tensorflow-analyzer

## Disclaimer
This tool is not officially associated with TensorFlow or Google. It's an independent analysis tool created for educational and research purposes.
