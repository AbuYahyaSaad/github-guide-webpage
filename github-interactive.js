// GitHub Guide Interactive Features

// GitHub API Demo
class GitHubDemo {
    constructor() {
        this.commands = [];
        this.currentStep = 0;
    }

    // Simulate git commands
    simulateCommand(command) {
        const output = this.getCommandOutput(command);
        this.displayInTerminal(command, output);
        this.commands.push({ command, output });
    }

    getCommandOutput(command) {
        const outputs = {
            'git init': 'Initialized empty Git repository in /project/.git/',
            'git status': `On branch main
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    index.html
    style.css
    script.js`,
            'git add .': 'Files staged for commit',
            'git commit -m "Initial commit"': '[main (root-commit) a1b2c3d] Initial commit\n 3 files changed, 150 insertions(+)',
            'git push origin main': 'Enumerating objects: 5, done.\nCounting objects: 100% (5/5), done.\nWriting objects: 100% (5/5), 1.20 KiB | 1.20 MiB/s, done.',
            'git branch': '* main\n  develop\n  feature-login',
            'git pull': 'Already up to date.'
        };
        return outputs[command] || 'Command executed successfully';
    }

    displayInTerminal(command, output) {
        const terminal = document.createElement('div');
        terminal.className = 'terminal';
        terminal.innerHTML = `
            <div class="terminal-line">
                <span class="terminal-prompt">$</span>
                <span class="terminal-command">${command}</span>
            </div>
            <div class="terminal-output">${output}</div>
        `;
        return terminal;
    }
}

// Interactive Workflow Builder
class WorkflowBuilder {
    constructor() {
        this.steps = [];
    }

    addStep(name, description, command) {
        this.steps.push({ name, description, command });
    }

    createVisualWorkflow() {
        const workflow = document.createElement('div');
        workflow.className = 'visual-workflow';
        
        this.steps.forEach((step, index) => {
            const stepElement = this.createStepElement(step, index);
            workflow.appendChild(stepElement);
            
            if (index < this.steps.length - 1) {
                const arrow = document.createElement('div');
                arrow.className = 'workflow-arrow';
                arrow.innerHTML = '→';
                workflow.appendChild(arrow);
            }
        });
        
        return workflow;
    }

    createStepElement(step, index) {
        const stepEl = document.createElement('div');
        stepEl.className = 'workflow-step';
        stepEl.innerHTML = `
            <div class="step-number">${index + 1}</div>
            <div class="step-content">
                <h4>${step.name}</h4>
                <p>${step.description}</p>
                <code>${step.command}</code>
            </div>
        `;
        return stepEl;
    }
}

// Command Palette
class CommandPalette {
    constructor() {
        this.commands = this.initializeCommands();
        this.isOpen = false;
    }

    initializeCommands() {
        return [
            { name: 'Create Repository', action: () => this.createRepo(), shortcut: 'Ctrl+N' },
            { name: 'Clone Repository', action: () => this.cloneRepo(), shortcut: 'Ctrl+Shift+C' },
            { name: 'Create Branch', action: () => this.createBranch(), shortcut: 'Ctrl+B' },
            { name: 'Commit Changes', action: () => this.commitChanges(), shortcut: 'Ctrl+K' },
            { name: 'Push to Remote', action: () => this.pushChanges(), shortcut: 'Ctrl+P' },
            { name: 'Pull from Remote', action: () => this.pullChanges(), shortcut: 'Ctrl+Shift+P' },
            { name: 'View History', action: () => this.viewHistory(), shortcut: 'Ctrl+H' },
            { name: 'Create Pull Request', action: () => this.createPR(), shortcut: 'Ctrl+Shift+R' }
        ];
    }

    open() {
        this.isOpen = true;
        this.render();
    }

    close() {
        this.isOpen = false;
        const palette = document.querySelector('.command-palette');
        if (palette) palette.remove();
    }

    render() {
        const palette = document.createElement('div');
        palette.className = 'command-palette';
        palette.innerHTML = `
            <input type="text" placeholder="Type a command..." class="command-search">
            <div class="command-list">
                ${this.commands.map(cmd => `
                    <div class="command-item" data-command="${cmd.name}">
                        <span>${cmd.name}</span>
                        <kbd>${cmd.shortcut}</kbd>
                    </div>
                `).join('')}
            </div>
        `;
        document.body.appendChild(palette);
    }

    // Command actions
    createRepo() {
        showAlert('Creating new repository...');
    }

    cloneRepo() {
        const url = prompt('Enter repository URL:');
        if (url) showAlert(`Cloning repository: ${url}`);
    }

    createBranch() {
        const name = prompt('Enter branch name:');
        if (name) showAlert(`Created branch: ${name}`);
    }

    commitChanges() {
        const message = prompt('Enter commit message:');
        if (message) showAlert(`Committed with message: "${message}"`);
    }

    pushChanges() {
        showAlert('Pushing changes to remote...');
    }

    pullChanges() {
        showAlert('Pulling latest changes...');
    }

    viewHistory() {
        showAlert('Loading commit history...');
    }

    createPR() {
        showAlert('Opening pull request form...');
    }
}

// Learning Progress Tracker
class ProgressTracker {
    constructor() {
        this.topics = {
            basics: { completed: false, progress: 0 },
            setup: { completed: false, progress: 0 },
            commands: { completed: false, progress: 0 },
            workflow: { completed: false, progress: 0 },
            collaboration: { completed: false, progress: 0 },
            advanced: { completed: false, progress: 0 }
        };
        this.loadProgress();
    }

    updateProgress(topic, progress) {
        this.topics[topic].progress = progress;
        if (progress >= 100) {
            this.topics[topic].completed = true;
        }
        this.saveProgress();
        this.updateUI();
    }

    loadProgress() {
        const saved = localStorage.getItem('github-guide-progress');
        if (saved) {
            this.topics = JSON.parse(saved);
        }
    }

    saveProgress() {
        localStorage.setItem('github-guide-progress', JSON.stringify(this.topics));
    }

    updateUI() {
        Object.keys(this.topics).forEach(topic => {
            const progress = this.topics[topic].progress;
            const progressBar = document.querySelector(`#${topic}-progress`);
            if (progressBar) {
                progressBar.style.width = `${progress}%`;
            }
        });
    }

    getOverallProgress() {
        const total = Object.values(this.topics).reduce((sum, topic) => sum + topic.progress, 0);
        return total / Object.keys(this.topics).length;
    }
}

// Initialize features
let demo, workflowBuilder, commandPalette, progressTracker;

document.addEventListener('DOMContentLoaded', function() {
    demo = new GitHubDemo();
    workflowBuilder = new WorkflowBuilder();
    commandPalette = new CommandPalette();
    progressTracker = new ProgressTracker();

    // Setup keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'k') {
            e.preventDefault();
            commandPalette.open();
        }
        if (e.key === 'Escape' && commandPalette.isOpen) {
            commandPalette.close();
        }
    });

    // Add interactive terminal
    addInteractiveTerminal();
    
    // Add progress bars to sections
    addProgressBars();
    
    // Track section views
    trackSectionViews();
});

// Interactive Terminal
function addInteractiveTerminal() {
    const terminalContainer = document.createElement('div');
    terminalContainer.className = 'interactive-terminal-container';
    terminalContainer.innerHTML = `
        <div class="terminal">
            <div class="terminal-header">
                <span>Git Terminal</span>
                <button onclick="clearTerminal()">Clear</button>
            </div>
            <div class="terminal-body" id="terminal-output"></div>
            <div class="terminal-input">
                <span class="terminal-prompt">$</span>
                <input type="text" id="terminal-command" placeholder="Type git command...">
            </div>
        </div>
    `;
    
    // Add to commands section
    const commandsSection = document.getElementById('commands');
    if (commandsSection) {
        commandsSection.appendChild(terminalContainer);
    }
}

// Progress Bars
function addProgressBars() {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        progressBar.innerHTML = `<div class="progress-fill" id="${section.id}-progress"></div>`;
        section.insertBefore(progressBar, section.firstChild.nextSibling);
    });
}

// Track Section Views
function trackSectionViews() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.id;
                // Simulate progress increase
                setTimeout(() => {
                    progressTracker.updateProgress(sectionId, 100);
                }, 2000);
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.section').forEach(section => {
        observer.observe(section);
    });
}

// Enhanced Alert System
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-icon">${getNotificationIcon(type)}</span>
            <span class="notification-message">${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('notification-show');
    }, 100);
    
    setTimeout(() => {
        notification.classList.remove('notification-show');
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function getNotificationIcon(type) {
    const icons = {
        success: '✓',
        error: '✗',
        warning: '⚠',
        info: 'ℹ'
    };
    return icons[type] || icons.info;
}

// Command execution in terminal
document.addEventListener('keydown', function(e) {
    if (e.target.id === 'terminal-command' && e.key === 'Enter') {
        const command = e.target.value;
        if (command) {
            executeTerminalCommand(command);
            e.target.value = '';
        }
    }
});

function executeTerminalCommand(command) {
    const output = document.getElementById('terminal-output');
    const commandLine = document.createElement('div');
    commandLine.innerHTML = `<span class="terminal-prompt">$</span> <span class="terminal-command">${command}</span>`;
    output.appendChild(commandLine);
    
    const result = demo.getCommandOutput(command);
    const resultLine = document.createElement('div');
    resultLine.className = 'terminal-output';
    resultLine.textContent = result;
    output.appendChild(resultLine);
    
    output.scrollTop = output.scrollHeight;
}

function clearTerminal() {
    document.getElementById('terminal-output').innerHTML = '';
}

// Export functions for global use
window.GitHubDemo = GitHubDemo;
window.WorkflowBuilder = WorkflowBuilder;
window.CommandPalette = CommandPalette;
window.ProgressTracker = ProgressTracker;
window.showNotification = showNotification;