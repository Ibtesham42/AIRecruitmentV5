def create_resume_scorecard(analysis: dict, position: str, position_config: dict) -> str:
    """Generate HTML scorecard for email"""
    return f"""
    <html>
      <body>
        <h3>Resume Analysis Report</h3>
        <p>Compatibility Score: {analysis['resume_score']}%</p>
        <p>Required Skills Found: {len(analysis['required_matches'])}/{len(position_config[position]['required_skills'])}</p>
        <p>Preferred Skills Found: {len(analysis['preferred_matches'])}</p>
        <p>Detected Experience: {analysis['experience']} years</p>
      </body>
    </html>
    """