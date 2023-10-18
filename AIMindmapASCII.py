def print_mind_map(node, prefix='', is_last=True):
    print(prefix, end='')
    if is_last:
        print('└──', end='')
        prefix += '    '
    else:
        print('├──', end='')
        prefix += '│   '

    print(node['label'])

    children = node.get('children', [])
    count = len(children)

    for i, child in enumerate(children):
        is_last = i == count - 1
        print_mind_map(child, prefix, is_last)


mind_map = {
    'label': 'Artificial Intelligence (AI)',
    'children': [
        {
            'label': 'Branches of AI',
            'children': [
                {
                    'label': 'Machine Learning',
                    'children': [
                        {'label': 'Supervised Learning'},
                        {'label': 'Unsupervised Learning'},
                        {'label': 'Reinforcement Learning'},
                        {'label': 'Deep Learning'}
                    ]
                },
                {
                    'label': 'Natural Language Processing (NLP)',
                    'children': [
                        {'label': 'Text Classification'},
                        {'label': 'Sentiment Analysis'},
                        {'label': 'Named Entity Recognition'},
                        {'label': 'Machine Translation'}
                    ]
                },
                {
                    'label': 'Computer Vision',
                    'children': [
                        {'label': 'Image Classification'},
                        {'label': 'Object Detection'},
                        {'label': 'Image Segmentation'},
                        {'label': 'Facial Recognition'}
                    ]
                },
                {
                    'label': 'Robotics',
                    'children': [
                        {'label': 'Autonomous Vehicles'},
                        {'label': 'Industrial Robots'},
                        {'label': 'Humanoid Robots'},
                        {'label': 'Surgical Robots'}
                    ]
                }
            ]
        },
        {
            'label': 'AI Techniques',
            'children': [
                {'label': 'Neural Networks'},
                {'label': 'Decision Trees'},
                {'label': 'Support Vector Machines (SVM)'},
                {'label': 'Bayesian Networks'},
                {'label': 'Genetic Algorithms'}
            ]
        },
        {
            'label': 'AI Applications',
            'children': [
                {
                    'label': 'Healthcare',
                    'children': [
                        {'label': 'Disease Diagnosis'},
                        {'label': 'Medical Imaging Analysis'},
                        {'label': 'Drug Discovery'},
                        {'label': 'Personalized Medicine'}
                    ]
                },
                {
                    'label': 'Finance',
                    'children': [
                        {'label': 'Fraud Detection'},
                        {'label': 'Algorithmic Trading'},
                        {'label': 'Credit Scoring'},
                        {'label': 'Risk Assessment'}
                    ]
                },
                {
                    'label': 'Transportation',
                    'children': [
                        {'label': 'Traffic Optimization'},
                        {'label': 'Autonomous Vehicles'},
                        {'label': 'Route Planning'},
                        {'label': 'Predictive Maintenance'}
                    ]
                },
                {
                    'label': 'Customer Service',
                    'children': [
                        {'label': 'Chatbots'},
                        {'label': 'Sentiment Analysis'},
                        {'label': 'Recommendation Systems'},
                        {'label': 'Voice Assistants'}
                    ]
                },
                {
                    'label': 'Education',
                    'children': [
                        {'label': 'Intelligent Tutoring Systems'},
                        {'label': 'Personalized Learning'},
                        {'label': 'Automated Grading'},
                        {'label': 'Adaptive Assessments'}
                    ]
                }
            ]
        },
        {
            'label': 'AI Ethics and Challenges',
            'children': [
                {'label': 'Bias and Fairness'},
                {'label': 'Privacy and Security'},
                {'label': 'Job Displacement'},
                {'label': 'Human-AI Collaboration'},
                {'label': 'Ethical Decision Making'}
            ]
        }
    ]
}

print_mind_map(mind_map)
