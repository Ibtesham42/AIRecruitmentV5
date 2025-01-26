import os
import json
from typing import Dict

def load_positions() -> Dict:
    """Load position configurations from JSON file"""
    positions_file = "data/positions/positions.json"
    os.makedirs(os.path.dirname(positions_file), exist_ok=True)
    
    if not os.path.exists(positions_file):
        with open(positions_file, 'w') as f:
            json.dump(default_positions(), f)
    
    with open(positions_file, 'r') as f:
        return json.load(f)

def default_positions() -> Dict:
    """Return default position configurations"""
    return {
        "Data Scientist": {
            "required_skills": ["Python", "SQL", "Machine Learning", "Statistics", "Data Visualization"],
            "preferred_skills": ["TensorFlow", "PyTorch", "Big Data", "Cloud Computing"],
            "technical": [
                ["Explain bias-variance tradeoff", ["bias", "variance", "overfitting"]],
                ["Handle missing data techniques", ["imputation", "deletion", "modeling"]],
                ["Cross-validation methods", ["k-fold", "stratified", "time-series"]]
            ],
            "behavioral": [
                ["Describe complex data analysis project", ["process", "tools", "results"]],
                ["Stay updated with DS trends", ["courses", "research", "experiments"]],
                ["Handle tight deadlines", ["prioritization", "communication", "tools"]]
            ],
            "experience_threshold": 2
        },
        "Software Engineer": {
            "required_skills": ["Java", "Python", "System Design", "Algorithms", "Databases"],
            "preferred_skills": ["Microservices", "AWS", "Docker", "Kubernetes"],
            "technical": [
                ["SOLID principles explanation", ["single responsibility", "open-closed", "interface"]],
                ["Database optimization strategies", ["indexing", "normalization", "sharding"]],
                ["REST API best practices", ["stateless", "versioning", "documentation"]],
                ["Debugging complex systems", ["logging", "testing", "monitoring"]]
            ],
            "behavioral": [
                ["Handle conflicting requirements", ["communication", "prioritization", "documentation"]],
                ["Code review process", ["checklist", "automation", "feedback"]],
                ["Manage technical debt", ["refactoring", "documentation", "tooling"]]
            ],
            "experience_threshold": 3
        }
    }