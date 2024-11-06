import openai
import requests
import pandas as pd
from datetime import datetime
import logging
from typing import Dict
import os

# Fixed tokens - you should store these securely in practice
GITHUB_TOKEN = "ghp_YourGitHubTokenHere"  # Replace with your actual token
OPENAI_API_KEY = "sk-YourOpenAIKeyHere"   # Replace with your actual key

# Target repository to analyze
TARGET_REPO = "tensorflow/tensorflow"  # We'll analyze TensorFlow as an example

class RepoAnalyzer:
    def __init__(self):
        """Initialize the analyzer with preset API keys."""
        self.github_token = GITHUB_TOKEN
        openai.api_key = OPENAI_API_KEY
        self.headers = {'Authorization': f'token {self.github_token}'}
        self.setup_logging()
        
    def setup_logging(self):
        """Set up basic logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            filename='tensorflow_analysis.txt'
        )
        
    def analyze(self) -> Dict:
        """
        Analyze the TensorFlow repository.
        """
        try:
            # Extract owner and repo name
            owner, repo = TARGET_REPO.split('/')
            
            # Get repository data
            repo_data = self._get_basic_metrics(owner, repo)
            
            # Get Python files for analysis
            code_samples = self._get_code_samples(owner, repo)
            
            # Use AI to analyze code
            ai_analysis = self._analyze_with_ai(code_samples)
            
            # Combine results
            analysis_result = {
                'repository': TARGET_REPO,
                'metrics': repo_data,
                'ai_insights': ai_analysis,
                'timestamp': datetime.now().isoformat()
            }
            
            # Save to CSV
            self._save_to_csv(analysis_result)
            
            return analysis_result
            
        except Exception as e:
            logging.error(f"Error analyzing repository: {str(e)}")
            return {"error": str(e)}
    
    def _get_basic_metrics(self, owner: str, repo: str) -> Dict:
        """Get basic repository metrics."""
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        
        return {
            'stars': data.get('stargazers_count', 0),
            'forks': data.get('forks_count', 0),
            'open_issues': data.get('open_issues_count', 0),
            'created_at': data.get('created_at', ''),
            'last_updated': data.get('updated_at', '')
        }
    
    def _get_code_samples(self, owner: str, repo: str) -> str:
        """Get content of key Python files."""
        # We'll analyze the main README and a core Python file
        files_to_analyze = ['README.md', 'tensorflow/python/framework/ops.py']
        combined_content = ""
        
        for filename in files_to_analyze:
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filename}"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                content_url = response.json()['download_url']
                code_response = requests.get(content_url)
                combined_content += f"\n\n=== {filename} ===\n"
                combined_content += code_response.text[:2000]  # First 2000 chars only
                
        return combined_content or "No code files found"
    
    def _analyze_with_ai(self, code: str) -> Dict:
        """Analyze code using OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You are an expert code reviewer. Analyze the TensorFlow "
                        "repository content and provide insights about code quality, "
                        "architecture, and potential improvements."
                    )},
                    {"role": "user", "content": f"Analyze this TensorFlow code:\n\n{code}"}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            analysis = response.choices[0].message.content
            
            # Get a summary
            summary_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "Summarize the following TensorFlow code analysis into 3-5 "
                        "key bullet points, focusing on architecture and quality."
                    )},
                    {"role": "user", "content": analysis}
                ],
                max_tokens=200,
                temperature=0.3
            )
            
            return {
                'detailed_review': analysis,
                'key_points': summary_response.choices[0].message.content.split('\n')
            }
            
        except Exception as e:
            logging.error(f"Error in AI analysis: {str(e)}")
            return {"error": "AI analysis failed"}
    
    def _save_to_csv(self, analysis_result: Dict):
        """Save analysis results."""
        df = pd.DataFrame([{
            'repository': analysis_result['repository'],
            'stars': analysis_result['metrics']['stars'],
            'forks': analysis_result['metrics']['forks'],
            'open_issues': analysis_result['metrics']['open_issues'],
            'key_insights': str(analysis_result['ai_insights'].get('key_points', [])),
            'timestamp': analysis_result['timestamp']
        }])
        
        csv_path = 'tensorflow_analysis.csv'
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_path, index=False)

def main():
    """Main function to run the analysis."""
    print("\n=== Starting TensorFlow Repository Analysis ===")
    
    analyzer = RepoAnalyzer()
    result = analyzer.analyze()
    
    print("\n=== Analysis Results ===")
    print(f"\nRepository: {result['repository']}")
    
    print("\nMetrics:")
    for key, value in result['metrics'].items():
        print(f"{key}: {value}")
    
    print("\nAI Insights:")
    if 'key_points' in result['ai_insights']:
        for point in result['ai_insights']['key_points']:
            print(f"- {point}")
    
    print("\nDetailed Review:")
    if 'detailed_review' in result['ai_insights']:
        print(result['ai_insights']['detailed_review'])
    
    print("\nResults have been saved to:")
    print("- tensorflow_analysis.csv (metrics and key insights)")
    print("- tensorflow_analysis.txt (detailed logs)")

if __name__ == "__main__":
    main()
